# ╔═══════════════════════════════════════════════════════════════╗
# ║                 CHAPTER 22: JSON HANDLING                     ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. What Is JSON?                                             ║
# ║  2. Python To JSON (Serialization)                            ║
# ║     - json.dumps() - Python Object → JSON String              ║
# ║     - json.dump() - Python Object → JSON File                 ║
# ║                                                               ║
# ║  3. JSON To Python (Deserialization)                          ║
# ║     - json.loads() - JSON String → Python Object              ║
# ║     - json.load() - JSON File → Python Object                 ║
# ║                                                               ║
# ║  4. Pretty Printing (indent Parameter)                        ║
# ║  5. Error Handling (JSONDecodeError)                          ║
# ║  6. Custom Object Serialization                               ║
# ║  7. Supported Data Types                                      ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
╔════════════════════════════════════════════════════════╗
║              JSON ↔ PYTHON CONVERSION                  ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  Python Dict       json.dumps()      JSON String       ║
║  {'key': 'val'} ─────────────────> {"key": "val"}      ║
║                                                        ║
║  Python Dict       json.loads()      JSON String       ║
║  {'key': 'val'} <───────────────── {"key": "val"}      ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""

# Chapter 22: JSON Handling
"""
JSON (JavaScript Object Notation) Is A LightWeight Data Format For Exchanging Data.
Python's Json Module Converts Between Python Objects And JSON Strings.

How It Works:
- json.dumps() - Convert Python Object To JSON String
- json.loads() - Convert JSON String To Python Object
- json.dump() / json.load() - For Files
- JSON Supports: Dict, List, Str, Int, Float, Bool, None
- Keys Must Be Strings, No Comments Allowed
"""

import json

# Python Data To JSON
data = {
    "name": "Anubhav",
    "age": 21,
    "skills": ["Python", "JavaScript", "SQL"],
    "is_student": True,
    "projects": [
        {"name": "Game", "language": "Python"},
        {"name": "Website", "language": "HTML"}
    ]
}

# Convert To JSON String
json_string = json.dumps(data, indent=4)  # Indent For Pretty Printing
print("JSON String:")
print(json_string)

# Convert Back To Python
python_data = json.loads(json_string)
print("\nBack To Python:")
print("Name:", python_data["name"])
print("Skills:", python_data["skills"])

# Working With Files
# Writing To JSON File
with open("OuputFolder/Text.json", "w") as file:
    json.dump(data, file, indent=4)
print("\nData Written To Text.json")

# Reading From JSON File
with open("OuputFolder/Text.json", "r") as file:
    loaded_data = json.load(file)
print("\nData Loaded From Text.json:")
print("Age:", loaded_data["age"])

# Handling JSON Errors
try:
    invalid_json = '{"name": "Anubhav", "age":}'  # Missing Value
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"\nJSON Error: {e}")

# Custom Objects (Advanced)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def Person_To_Dict(obj):
    """Convert Person Object To Dict For JSON"""
    return {"name": obj.name, "age": obj.age}

def Dict_To_Person(d):
    """Convert Dict Back To Person"""
    return Person(d["name"], d["age"])

person = Person("Anubhav", 21)
# Serialize
person_json = json.dumps(person, default=Person_To_Dict)
print(f"\nPerson As JSON: {person_json}")

# Deserialize (Would Need Custom Decoder For Full Objects)
person_dict = json.loads(person_json)
print(f"Back To Dict: {person_dict}")

print("\nJSON Is Widely Used For APIs, Config Files, And Data Exchange.")