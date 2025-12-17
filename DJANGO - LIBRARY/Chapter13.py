"""
====================================
CHAPTER 13: CELERY & BACKGROUND TASKS
====================================

Celery Is A Distributed Task Queue System For Processing Time-Consuming Operations
Asynchronously. Learn To Offload Heavy Tasks From Your Web Requests To Background Workers.

Topics Covered:
1. Introduction To Celery
2. Installation And Setup
3. Creating Tasks
4. Task Execution Patterns
5. Periodic Tasks (Celery Beat)
6. Task Management And Monitoring
7. Advanced Features
8. Best Practices And Production Tips
"""

#==============================================================================
# 1. INTRODUCTION TO CELERY
#==============================================================================

"""
WHAT IS CELERY?

Celery Is An Asynchronous Task Queue/Job Queue Based On Distributed Message Passing.
It's Focused On Real-Time Operation But Also Supports Scheduling.

WHY USE CELERY?

✅ Offload Time-Consuming Tasks From Web Requests
✅ Process Tasks Asynchronously
✅ Schedule Periodic Tasks
✅ Distribute Work Across Multiple Workers
✅ Retry Failed Tasks Automatically
✅ Monitor Task Execution

COMMON USE CASES:

1. Sending Emails
2. Processing Uploaded Files (Images, Videos, Documents)
3. Generating Reports
4. Data Synchronization With External APIs
5. Database Cleanup And Maintenance
6. Batch Processing
7. Periodic Data Aggregation
8. Web Scraping
9. Video/Audio Transcoding
10. Machine Learning Model Training

ARCHITECTURE:

Client (Django) → Message Broker (Redis/RabbitMQ) → Worker(s)
                                                      ↓
                                                   Results Backend
 """

#==============================================================================
# 2. INSTALLATION AND SETUP
#==============================================================================

"""
STEP 1: Install Celery And Message Broker

# Install Celery
pip install celery

# Install Redis (Recommended Broker)
pip install redis

# Or install RabbitMQ (Alternative Broker)
pip install amqp

# Install Django-Celery-Beat (For Periodic Tasks)
pip install django-celery-beat

# Install Flower (For Monitoring)
pip install flower


STEP 2: Install Redis Server

# On Ubuntu/Debian
sudo apt-get install redis-server

# On macOS
brew install redis

# On Windows
# Download from https://github.com/microsoftarchive/redis/releases


STEP 3: Create Celery Configuration
"""

# myproject/celery.py
import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Create Celery instance
app = Celery('myproject')

# Load config from Django settings with CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-Discover Tasks From All Registered Django Apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """Debug Task To Test Celery Setup."""
    print(f'Request: {self.request!r}')


# myproject/__init__.py
"""
Ensure Celery App Is Imported When Django Starts.
"""
from .celery import app as celery_app

__all__ = ('celery_app',)


# settings.py
"""
Add Celery Configuration To Django Settings.
"""

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis As Broker
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Redis As Result Backend

# Alternative: RabbitMQ
# CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# CELERY_RESULT_BACKEND = 'rpc://'

# Celery Settings
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60  # 30 Minutes

# Celery Beat (Periodic Tasks)
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


"""
STEP 4: Start Celery Worker

# Development (Single Worker)
celery -A myproject worker -l info

# Development (With Beat For Periodic Tasks)
celery -A myproject worker -B -l info

# Production (Multiple Workers)
celery -A myproject worker --concurrency=4 -l info

# Start Celery Beat Separately (Production)
celery -A myproject beat -l info

# Start Flower (Monitoring)
celery -A myproject flower
"""


#==============================================================================
# 3. CREATING TASKS
#==============================================================================

"""
Tasks Are Functions Decorated With @app.task Or @shared_task.
"""

from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
import time


# Basic Task
@shared_task
def add(x, y):
    """Simple Addition Task."""
    return x + y


# Task With Django Models
@shared_task
def send_welcome_email(user_id):
    """
    Send Welcome Email To New User.
    """
    try:
        user = User.objects.get(id=user_id)
        send_mail(
            subject='Welcome!',
            message=f'Hello {user.username}, Welcome To Our Platform!',
            from_email='noreply@example.com',
            recipient_list=[user.email],
            fail_silently=False,
        )
        return f'Email Sent To {user.email}'
    except User.DoesNotExist:
        return f'User {user_id} Not Found'


# Task With Parameters
@shared_task
def process_uploaded_file(file_path, user_id):
    """
    Process An Uploade  d File.
    """
    # Simulate Processing
    time.sleep(5)
    
    # Process File
    # ... Your Processing Logic ...
    
    return f'File {file_path} Processed For User {user_id}'


# Task With Retry
@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def fetch_data_from_api(self, api_url):
    """
    Fetch Data From External API With Retry Logic.
    """
    import requests
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        # Retry After Delay
        raise self.retry(exc=exc, countdown=60)


# Task With Multiple Steps
@shared_task
def generate_report(report_id):
    """
    Generate A Complex Report With Multiple Steps.
    """
    from .models import Report
    
    report = Report.objects.get(id=report_id)
    report.status = 'processing'
    report.save()
    
    try:
        # Step 1: Gather Data
        data = gather_report_data(report)
        
        # Step 2: Process Data
        processed_data = process_report_data(data)
        
        # Step 3: Generate PDF
        pdf_path = generate_pdf(processed_data)
        
        # Step 4: Upload To Storage
        report.file = pdf_path
        report.status = 'completed'
        report.save()
        
        return f'Report {report_id} completed'
    except Exception as e:
        report.status = 'failed'
        report.error_message = str(e)
        report.save()
        raise


# Task With Custom Options
@shared_task(
    name='custom.task.name',  # Custom Task Name
    bind=True,  # Pass Task Instance As First Argument
    max_retries=5,
    default_retry_delay=30,
    rate_limit='10/m',  # Max 10 Per Minute
    time_limit=300,  # 5 Minutes Max Execution Time
    soft_time_limit=240,  # Soft Limit Before Hard Limit
)
def complex_task(self, data):
    """Task With Custom Configuration."""
    # Task Implementation
    pass


#==============================================================================
# 4. TASK EXECUTION PATTERNS
#==============================================================================

"""
Different Ways To Execute Celery Tasks.
"""

# Calling Tasks In Views
from django.shortcuts import render, redirect
from django.contrib import messages
from .tasks import send_welcome_email, process_uploaded_file


# 1. Asynchronous Execution (Delay)
def register_user(request):
    """
    Register User And Send Welcome Email Asynchronously.
    """
    # Create User
    user = User.objects.create_user(
        username=request.POST['username'],
        email=request.POST['email'],
        password=request.POST['password']
    )
    
    # Send Welcome Email Asynchronously
    send_welcome_email.delay(user.id)
    
    messages.success(request, 'Account Created! Check Your Email.')
    return redirect('home')


# 2. Delayed Execution (apply_async)
def upload_file(request):
    """
    Upload File And Process It Asynchronously.
    """
    uploaded_file = request.FILES['file']
    
    # Save File
    file_path = save_uploaded_file(uploaded_file)
    
    # Process File After 10 Seconds
    process_uploaded_file.apply_async(
        args=[file_path, request.user.id],
        countdown=10  # Delay 10 Seconds
    )
    
    messages.success(request, 'File Uploaded! Processing Will Start Shortly.')
    return redirect('dashboard')


# 3. Scheduled Execution (eta)
from datetime import datetime, timedelta

def schedule_email(request):
    """
    Schedule Email To Be Sent At Specific Time.
    """
    # Schedule For Tomorrow At 9 AM
    tomorrow_9am = datetime.now() + timedelta(days=1)
    tomorrow_9am = tomorrow_9am.replace(hour=9, minute=0, second=0)
    
    send_welcome_email.apply_async(
        args=[request.user.id],
        eta=tomorrow_9am  # Execute At Specific Time
    )
    
    messages.success(request, 'Email Scheduled For Tomorrow At 9 AM')
    return redirect('home')


# 4. Task Chaining (Execute In Sequence)
from celery import chain

def process_and_notify(request):
    """
    Process File Then Send Notification.
    """
    file_path = request.POST['file_path']
    user_id = request.user.id
    
    # Create Task Chain
    workflow = chain(
        process_uploaded_file.s(file_path, user_id),
        send_notification.s(user_id)  # Receives Result From Previous Task
    )
    
    workflow.apply_async()
    
    return redirect('dashboard')


# 5. Task Groups (Execute In Parallel)
from celery import group

def batch_process(request):
    """
    Process Multiple Files In Parallel.
    """
    file_paths = request.POST.getlist('files')
    user_id = request.user.id
    
    # Create Task Group
    job = group(
        process_uploaded_file.s(path, user_id)
        for path in file_paths
    )
    
    result = job.apply_async()
    
    messages.success(request, f'Processing {len(file_paths)} Files')
    return redirect('dashboard')


# 6. Task With Callback
def process_with_callback(request):
    """
    Process File And Execute Callback On Success.
    """
    file_path = request.POST['file_path']
    
    process_uploaded_file.apply_async(
        args=[file_path, request.user.id],
        link=send_notification.s(request.user.id),  # Callback On Success
        link_error=handle_error.s()  # Callback On Error
    )
    
    return redirect('dashboard')


# 7. Getting Task Results
from celery.result import AsyncResult

def check_task_status(request, task_id):
    """
    Check Status Of Running Task.
    """
    result = AsyncResult(task_id)
    
    response_data = {
        'task_id': task_id,
        'status': result.status,
        'result': result.result if result.ready() else None,
    }
    
    return JsonResponse(response_data)


#==============================================================================
# 5. PERIODIC TASKS (CELERY BEAT)
#==============================================================================

"""
Schedule Tasks To Run Periodically Using Celery Beat.
"""

from celery.schedules import crontab


# Define Periodic Tasks In settings.py
"""
CELERY_BEAT_SCHEDULE = {
    # Execute Every 30 Seconds
    'add-every-30-seconds': {
        'task': 'myapp.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
    
    # Execute Every Monday Morning At 7:30 AM
    'send-weekly-report': {
        'task': 'myapp.tasks.send_weekly_report',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
    },
    
    # Execute Daily At Midnight
    'cleanup-old-data': {
        'task': 'myapp.tasks.cleanup_old_data',
        'schedule': crontab(hour=0, minute=0),
    },
    
    # Execute Every Hour
    'sync-external-data': {
        'task': 'myapp.tasks.sync_external_data',
        'schedule': crontab(minute=0),  # Every Hour At Minute 0
    },
    
    # Execute On 15th Day Of Every Month
    'monthly-report': {
        'task': 'myapp.tasks.generate_monthly_report',
        'schedule': crontab(hour=0, minute=0, day_of_month=15),
    },
}
"""


# Periodic Task Examples
@shared_task
def cleanup_old_data():
    """
    Clean Up Old Data Daily.
    """
    from datetime import timedelta
    from django.utils import timezone
    from .models import TempData
    
    cutoff_date = timezone.now() - timedelta(days=30)
    deleted_count = TempData.objects.filter(
        created_at__lt=cutoff_date
    ).delete()[0]
    
    return f'Deleted {deleted_count} Old Records'

@shared_task
def send_weekly_report():
    """
    Generate And Send Weekly Report.    
    """
    # Generate Report
    report_data = generate_weekly_statistics()
    
    # Send To All Admins
    admins = User.objects.filter(is_staff=True)
    for admin in admins:
        send_mail(
            subject='Weekly Report',
            message=report_data,
            from_email='noreply@example.com',
            recipient_list=[admin.email],
        )
    
    return f'Weekly Report Sent To {admins.count()} Admins'


@shared_task
def sync_external_data():
    """
    Sync Data With External API Every Hour.
    """
    import requests
    from .models import ExternalData
    
    response = requests.get('https://api.example.com/data')
    data = response.json()
    
    for item in data:
        ExternalData.objects.update_or_create(
            external_id=item['id'],
            defaults={'data': item}
        )
    
    return f'Synced {len(data)} items'


# Using django-celery-beat for dynamic scheduling
"""
# Add to INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'django_celery_beat',
]

# Run migrations
python manage.py migrate django_celery_beat

# Now You Can Manage Periodic Tasks From Django Admin Or Programmatically:
"""

from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

def create_periodic_task_dynamically():
    """
    Create Periodic Task Programmatically.
    """
    # Create Schedule
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )
    
    # Create Periodic Task
    PeriodicTask.objects.create(
        interval=schedule,
        name='Import Contacts Every 10 Seconds',
        task='myapp.tasks.import_contacts',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({'be_careful': True}),
    )


#==============================================================================
# 6. TASK MANAGEMENT AND MONITORING
#==============================================================================

"""
Monitor And Manage Celery Tasks.
"""

# Task State And Results
@shared_task(bind=True)
def long_running_task(self):
    """
    Task That Reports Progress.
    """
    total = 100
    
    for i in range(total):
        # Simulate Work
        time.sleep(0.1)
        
        # Update Task State
        self.update_state(
            state='PROGRESS',
            meta={
                'current': i,
                'total': total,
                'percent': int((i / total) * 100)
            }
        )
    
    return {'current': total, 'total': total, 'percent': 100}


# View To Check Task Progress
def task_progress(request, task_id):
    """
    Get Task Progress.
    """
    result = AsyncResult(task_id)
    
    if result.state == 'PROGRESS':
        response = {
            'state': result.state,
            'current': result.info.get('current', 0),
            'total': result.info.get('total', 1),
            'percent': result.info.get('percent', 0),
        }
    elif result.state == 'SUCCESS':
        response = {
            'state': result.state,
            'current': result.info.get('current', 100),
            'total': result.info.get('total', 100),
            'percent': 100,
            'result': result.result,
        }
    else:
        response = {
            'state': result.state,
            'status': str(result.info),  # Error Message
        }
    
    return JsonResponse(response)


# Revoking Tasks
def cancel_task(request, task_id):
    """
    Cancel A Running Task.
    """
    from celery import current_app
    
    current_app.control.revoke(task_id, terminate=True)
    
    messages.success(request, f'Task {task_id} Cancelled')
    return redirect('task_list')


# Inspecting Workers
@shared_task
def get_worker_stats():
    """
    Get Statistics About Celery Workers.
    """
    from celery import current_app
    
    # Get Active Tasks
    active = current_app.control.inspect().active()
    
    # Get Registered Tasks
    registered = current_app.control.inspect().registered()
    
    # Get Worker Stats
    stats = current_app.control.inspect().stats()
    
    return {
        'active_tasks': active,
        'registered_tasks': registered,
        'stats': stats,
    }


# Using Flower For Monitoring
"""
Flower Is A Web-Based Tool For Monitoring Celery Tasks.

Installation:
pip install flower

Start Flower:
celery -A myproject flower

Access at: http://localhost:5555

Features:
- Real-Time Task Monitoring
- Task History
- Worker Statistics
- Task Rate Charts
- Broker Monitoring
- Configuration Viewer
"""


#==============================================================================
# 7. ADVANCED FEATURES
#==============================================================================

"""
Advanced Celery Features And Patterns.
"""

# Task Routing (Different Queues)
"""
# settings.py
CELERY_TASK_ROUTES = {
    'myapp.tasks.send_email': {'queue': 'emails'},
    'myapp.tasks.process_image': {'queue': 'images'},
    'myapp.tasks.generate_report': {'queue': 'reports'},
}

# Start Workers For Specific Queues
celery -A myproject worker -Q emails -l info
celery -A myproject worker -Q images -l info
celery -A myproject worker -Q reports -l info
"""


# Task Priority
@shared_task
def high_priority_task():
    """High Priority Task."""
    pass

# Execute With Priority
high_priority_task.apply_async(priority=9)  # 0-9, 9 Is Highest


# Task Result Expiration
@shared_task(result_expires=3600)  # Results Expire After 1 Hour
def temporary_result_task():
    """Task With Expiring Results."""
    return "This result will expire"


# Task With Timeout
from celery.exceptions import SoftTimeLimitExceeded

@shared_task(soft_time_limit=60, time_limit=65)
def task_with_timeout():
    """
    Task With Time Limit.
    """
    try:
        # Long Running Operation
        time.sleep(100)
    except SoftTimeLimitExceeded:
        # Clean Up
        return "Task Timeout - Cleaning Up"


# Canvas - Complex workflows
from celery import chain, group, chord

# Chain - Execute Tasks In Sequence
workflow = chain(
    task1.s(),
    task2.s(),
    task3.s()
)
workflow.apply_async()


# Group - Execute Tasks In Parallel
job = group(
    task1.s(1),
    task1.s(2),
    task1.s(3)
)
result = job.apply_async()


# Chord - Group With Callback
callback = chord(
    group(task1.s(i) for i in range(10)),
    aggregate_results.s()  # Called With Results From Group
)
callback.apply_async()


# Map - Apply Task To Iterable
from celery import starmap

result = task1.starmap([(i,) for i in range(10)])


#==============================================================================
# 8. BEST PRACTICES AND PRODUCTION TIPS
#==============================================================================

"""
BEST PRACTICES:

1. Keep Tasks Idempotent
   - Tasks Should Produce Same Result When Executed Multiple Times
   - Important For Retries

2. Use Task IDs For Tracking
   - Store Task IDs In Database
   - Allow Users To Check Task Status

3. Handle Failures Gracefully
   - Use max_retries
   - Log Errors
   - Send Notifications For Critical Failures

4. Don't Pass Django Model Instances
   - Pass IDs Instead
   - Fetch Fresh Data In Task

5. Set Timeouts
   - Prevent Tasks From Running Forever
   - Use soft_time_limit And time_limit

6. Monitor Your Workers
   - Use Flower Or Similar Tools
   - Set Up Alerts For Failures

7. Use Appropriate Serializers
   - JSON Is Recommended
   - Avoid Pickle For Security

8. Separate Queues For Different Task Types
   - Prevents Slow Tasks From Blocking Fast Ones
   - Better Resource Allocation
"""


# Good Practices Example
@shared_task(
    bind=True,
    max_retries=3,
    default_retry_delay=60,
    soft_time_limit=300,
    time_limit=330
)
def well_designed_task(self, user_id):
    """
    Example Of Well-Designed Task.
    """
    import logging
    logger = logging.getLogger(__name__)
    
    try:
        # Fetch Fresh Data (Don't Pass Model Instances)
        user = User.objects.get(id=user_id)
        
        # Perform Operation
        result = perform_operation(user)
        
        # Log Success
        logger.info(f'Task Completed For User {user_id}')
        
        return result
        
    except User.DoesNotExist:
        logger.error(f'User {user_id} Not Found')
        return None
        
    except Exception as exc:
        # Log Error
        logger.error(f'Task Failed: {exc}', exc_info=True)
        
        # Retry
        raise self.retry(exc=exc, countdown=60)


# Production Settings
"""
# settings.py - Production Configuration

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

# Reliability
CELERY_TASK_ACKS_LATE = True  # Acknowledge Task After Execution
CELERY_WORKER_PREFETCH_MULTIPLIER = 1  # One Task At A Time Per Worker

# Results
CELERY_RESULT_EXPIRES = 3600  # Results Expire After 1 Hour
# Serialization
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Monitoring
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_SEND_SENT_EVENT = True

# Error handling
CELERY_TASK_IGNORE_RESULT = False
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True

# Security
CELERY_TASK_REJECT_ON_WORKER_LOST = True
"""


# Supervisor Configuration For Production
"""
# /etc/supervisor/conf.d/celery.conf

[program:celery]
command=/path/to/venv/bin/celery -A myproject worker -l info
directory=/path/to/project
user=www-data
numprocs=1
stdout_logfile=/var/log/celery/worker.log
stderr_logfile=/var/log/celery/worker.log
autostart=true
autorestart=true
startsecs=10
stopwaitsecs=600
priority=998

[program:celerybeat]
command=/path/to/venv/bin/celery -A myproject beat -l info
directory=/path/to/project
user=www-data
numprocs=1
stdout_logfile=/var/log/celery/beat.log
stderr_logfile=/var/log/celery/beat.log
autostart=true
autorestart=true
startsecs=10
priority=999
"""


"""
SUMMARY:

Celery Provides:
✅ Asynchronous Task Execution
✅ Distributed Task Processing
✅ Scheduled/Periodic Tasks
✅ Task Retry And Error Handling
✅ Monitoring And Management Tools
✅ Scalable Architecture

Remember:
- Use Celery For Time-Consuming Operations
- Keep Tasks Simple And Idempotent
- Handle Errors Gracefully
- Monitor Your Workers
- Use Appropriate Queues
- Set Timeouts
- Test Tasks Thoroughly
"""

# End of Chapter 13: Celery & Background Tasks