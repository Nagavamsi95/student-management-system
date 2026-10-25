\# Student Management System (Python + JSON)



A command-line application for managing student records. Students, course details, and grades are stored in a JSON file, so data persists between runs.



\## Features



\- Add, view, find, update, and delete student records

\- Record grades per student and generate an average grade report

\- Data is saved to `students.json` after every change and reloaded on startup



\## Tech Stack



\- \*\*Python 3\*\* (standard library only: `json`, `os`)

\- \*\*JSON\*\* for file-based data storage

\- \*\*PowerShell / Terminal\*\* for running the application



\## Project Structure



```

student\_management/

├── student\_manager.py   # Main application: menu, CRUD operations, grades

├── students.json        # Data file (created and updated by the app)

└── README.md

```



\## Getting Started



\### Prerequisites



\- Python 3.8 or newer



Check your version:



```bash

python --version

```



\### Run the application



```bash

python student\_manager.py

```



\## Usage



When the program starts, you see a menu:



```

===== Student Management System =====

1\. Add student

2\. View all students

3\. Find student

4\. Update student

5\. Delete student

6\. Add / update grade

7\. Show average report

0\. Exit

```



Example session:



```

Choose an option: 1

Student ID: S101

Name: Asha Reddy

Course: Computer Science

Student 'Asha Reddy' added.



Choose an option: 6

Student ID: S101

Subject: Python

Grade (0-100): 88.5

Saved Python: 88.5



Choose an option: 7

ID        Name                Average

\---------------------------------------------

S101      Asha Reddy          88.50

```



\## Data Format



Each student is stored under a unique ID:



```json

{

&#x20;   "S101": {

&#x20;       "name": "Asha Reddy",

&#x20;       "course": "Computer Science",

&#x20;       "grades": {

&#x20;           "Python": 88.5,

&#x20;           "Databases": 91.0

&#x20;       }

&#x20;   }

}

```



\## What I Learned



\- Reading and writing structured data with Python's `json` module

\- Using dictionaries for fast lookup by student ID

\- Building a menu-driven loop with separate functions for each operation

\- Handling user input and invalid values

\- Organizing code so each feature can be tested and changed independently



\## Possible Improvements



\- Reject empty name and course fields during input validation

\- Add unit tests with `pytest`

\- Export the average report to CSV

\- Containerize the app with Docker

\- Replace JSON storage with SQLite



\## Author



Naga Vamsi Kolakani

GitHub: \[@Nagavamsi95](https://github.com/Nagavamsi95)

