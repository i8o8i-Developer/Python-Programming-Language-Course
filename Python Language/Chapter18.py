# ╔═══════════════════════════════════════════════════════════════╗
# ║                 CHAPTER 18: TIME MODULE                       ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. time() - Current Time As Timestamp                        ║
# ║  2. ctime() - Formatted Time String                           ║
# ║  3. Time Conversion (gmtime, localtime)                       ║
# ║  4. strftime() - Format Time Strings                          ║
# ║  5. sleep() - Pause Execution                                 ║
# ║  6. Performance Timing                                        ║
# ║     - perf_counter() - High Resolution Timer                  ║
# ║     - monotonic() - Monotonic Timer                           ║
# ║     - process_time() - CPU Time                               ║
# ║  7. asctime() - Convert struct_time To String                 ║
# ║  8. Formatting Directives (%Y, %m, %d, %H, %M, %S)            ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: time() - Current Time As Timestamp
# ═══════════════════════════════════════════════════════════════

# Extra Knowledge

# Time Module
import time as Time

"Time.Time() Returns The Current Time As A Floating Point Number" # Seconds
H = Time.time() # Calculate Tiime From 1 January 1970

"Time.ctime() Returns The Current Time As A String"
H1 = Time.ctime()

# Converting TimeStamp :
UTC = Time.gmtime(H) # Current Time To UTC By gmtime()
Local = Time.localtime(H) # Current Time To Local-Time By localtime()

# Formating Time : strftime()

Formatted_Time = Time.strftime("%Y-%m-%d %H:%M:%S", Local)
print(Formatted_Time)  # Prints in format like 2024-07-10 14:30:00

# Sleep Function
Time.sleep(5)  # Pauses Execution For 5 Seconds

# Performance Time Counter : perf_counter()
Start_Time = Time.perf_counter()
'Some Task'
End_Time = Time.perf_counter()
Execution_Time = End_Time - Start_Time
print(f"Execution Time : {Execution_Time} Seconds")

# Presize Timing : monotonic()
Start = Time.monotonic()
'Some Task'
End = Time.monotonic()
Elapsed = End - Start
print(f"Elapsed Time : {Elapsed} seconds")

# CPU TIME USED : process_time()
Start_Cpu = Time.process_time()
# Perform some CPU-intensive task
for i in range(1000000):
    _ = i * i
# End measuring CPU time
End_Cpu = Time.process_time()
Elapsed_Cpu = End_Cpu - Start_Cpu
print(f"CPU Time Used : {Elapsed_Cpu} Seconds")

# Convert struct_time object to a formatted string
Formatted_Time = Time.asctime(Local)
print("Formatted Time :", Formatted_Time)

# Formatting Directives (strftime and strptime) :
# %Y: Year (4 digits)
# %m: Month (01-12)
# %d: Day of the month (01-31)
# %H: Hour (00-23)
# %M: Minute (00-59)
# %S: Second (00-59)


""" DateTime Module """

import datetime as DateTime

# --- Date class ---
# Represents A Date (Year, Month, Day).
# Constructor To Create A Date Object.
# Date(Year, Month, Day)
D = DateTime.date(2024, 7, 10)

# Returns The Current Local Date.
# date.today()
Current_Date = DateTime.date.today()

# Returns A Date From An ISO Format String ('YYYY-MM-DD').
# date.fromisoformat(Date_String)
Iso_Date = DateTime.date.fromisoformat('2024-07-10')

# --- Time class ---
# Represents A Time (Hour, Minute, Second, Microsecond).
# Constructor To Create A Time Object.
# time(Hour, Minute, Second, Microsecond)
T = DateTime.time(14, 30, 0)

# Returns A Time From An ISO Format String ('HH:MM:SS').
# time.fromisoformat(Time_String)
Iso_Time = DateTime.time.fromisoformat('14:30:00')

# --- DateTime class ---
# Represents A Combination Of Date And Time.
# Constructor To Create A DateTime Object.
# DateTime(Year, Month, Day, Hour=0, Minute=0, Second=0, Microsecond=0)
DT = DateTime.datetime(2024, 7, 10, 0, 0, 0, 0)

# Returns The Current Local DateTime.
# datetime.now()
Current_DateTime = DateTime.datetime.now()

# Returns The Current UTC DateTime.
# datetime.utcnow()
Current_UTC_DateTime = DateTime.datetime.utcnow()

# Returns A DateTime From An ISO Format String ('YYYY-MM-DDTHH:MM:SS').
# datetime.fromisoformat(datetime_string)
Iso_DateTime = DateTime.datetime.fromisoformat('2024-07-10T14:30:00')

# --- Timedelta class ---
# Represents A Duration or difference between two dates or times.
# Used For Arithmetic Operations On Dates/Times (+, -).
# DateTime.timedelta

# --- Common Methods For Date, Time, And DateTime Objects ---
# Accessors For Individual Components.
# .Year, .Month, .Day, .Hour, .Minute, .Second, .Microsecond
Year = DT.year
Month = DT.month
Day = DT.day
Hour = DT.hour
Minute = DT.minute
Second = DT.second
Microsecond = DT.microsecond

# Returns The Day Of The Week As An Integer (Monday is 0).
# .weekday()
Weekday = DT.weekday()

# Returns A string Representation Based On Format.
# .strftime(Format)
Formatted_DateTime = DT.strftime('%Y-%m-%d %H:%M:%S')

# --- Utility Functions ---
# Parses A String Representing A Date/Time Into A DateTime Object.
# datetime.strptime(Date_String, Format)
Parsed_DateTime = DateTime.datetime.strptime('2024-07-10 14:30:00', '%Y-%m-%d %H:%M:%S')

# Converts A POSIX Timestamp into A DateTime.date.
# DateTime.date.fromtimestamp(timestamp)
Posix_Date = DateTime.date.fromtimestamp(1625896800)  # Example TimeStamp

# Converts A POSIX TimeStamp Into A DateTime.datetime.
# DateTime.datetime.fromtimestamp(timestamp)
Posix_DateTime = DateTime.datetime.fromtimestamp(1625896800)  # Example TimeStamp

# Returns The POSIX TimeStamp For A DateTime.datetime.
# DateTime.datetime.timestamp()
Posix_TimeStamp = DT.timestamp()

# Printing examples for demonstration
print(f'D: {D}')
print(f'Current_Date: {Current_DateTime}')
print(f'Iso_Date: {Iso_Date}')
print(f'T: {T}')
print(f'Iso_Time: {Iso_Time}')
print(f'Dt: {DT}')
print(f'Current_DateTime: {Current_DateTime}')
print(f'Current_Utc_DateTime: {Current_UTC_DateTime}')
print(f'Iso_DateTime: {Iso_DateTime}')
print(f'Year: {Year}, Month: {Month}, Day: {Day}, Hour: {Hour}, Minute: {Minute}, Second: {Second}, Microsecond: {Microsecond}')
print(f'Weekday: {Weekday}')
print(f'Formatted_DateTime: {Formatted_DateTime}')
print(f'Parsed_DateTime: {Parsed_DateTime}')
print(f'Posix_Date: {Posix_Date}')
print(f'Posix_DateTime: {Posix_DateTime}')
print(f'Posix_Timestamp: {Posix_TimeStamp}')