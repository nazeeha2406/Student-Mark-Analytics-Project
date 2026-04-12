# 🎓 Student Mark Analysis System

A menu-driven Python application to manage and analyze student academic records using binary file handling.

---

## 📌 About the Project

This project stores, retrieves, and analyzes the mark details of **124 students** across 6 subjects using Python's `pickle` module for binary file handling. It is designed as a multi-module system where each module handles a specific task independently.

---

## 📂 Project Structure

```
student-mark-analysis/
│
├── module1_insert.py        # Insert 124 student records into binary file
├── module2_display.py       # Display all student records with total, average, cutoffs
├── module3_search.py        # Search student by register number
├── module4_add.py           # Add new student records
├── module5_add_validation.py# Add with duplicate register number validation
├── module6_analysis.py      # Data analysis menu (pass/fail %, avg, max, min)
│
├── Studentdata.dat          # Binary data file (auto-created by module1)
└── README.md
```

---

## 📋 Modules Overview

### Module 1 — Insert Data
- Stores 124 student records as a 2D list into `Studentdata.dat` using `pickle`
- Each record contains: Name, Register No, Tamil, English, Maths, Physics, Chemistry, Biology

### Module 2 — Display All Records
- Reads and displays all student records one by one
- Shows Total, Average, Result (Pass/Fail), Engineering Cutoff, Medical Cutoff

### Module 3 — Search by Register Number
- Accepts a register number as input
- If found → displays full student details
- If not found → displays appropriate message

### Module 4 — Add New Student
- Accepts new student details as input
- Supports adding multiple students using Y/N prompt

### Module 5 — Add with Validation
- Same as Module 4 but with duplicate register number check
- If register number already exists → asks to enter again
- If new → adds student record to the file

### Module 6 — Data Analysis *(in progress)*
- Menu-driven analysis module
- Options include:
  - Pass percentage and Fail percentage
  - Subject-wise fail count
  - Average marks (overall and subject-wise)
  - Maximum marks
  - Minimum marks
  - Number of students failed per subject
- Output exported to CSV file

---

## 🧪 Sample Data

```python
["A. ARAVIND", "23226er001", 92, 91, 78, 77, 79, 80]
["B. JANANI",  "23226er022", 91, 94, 88, 100, 94, 88]   # Centum in Physics
["I. KATHIR",  "23226er028", 91, 98, 99, 100, 91, 92]   # Centum in Physics
```

- Total Students : 124
- Pass           : 100 (80.65%)
- Fail           : 24  (19.35%)
- Centum Scorers : 3

---

## 📊 Data Format

| Index | Field     |
|-------|-----------|
| [0]   | Name      |
| [1]   | Regno     |
| [2]   | Tamil     |
| [3]   | English   |
| [4]   | Maths     |
| [5]   | Physics   |
| [6]   | Chemistry |
| [7]   | Biology   |

---

## ⚙️ Technologies Used

- **Language** — Python 3
- **File Handling** — pickle (binary .dat file)
- **Data Structure** — 2D List
- **Export** — CSV (Module 6)

---

## ▶️ How to Run

1. Clone the repository
```bash
git clone https://github.com/nazeeha2406/Student-Mark-Analytics-Project.git
cd student-mark-analysis
```

2. Run Module 1 first to create the data file
```bash
python module1_insert.py
```

3. Run any other module
```bash
python module2_display.py
python module3_search.py
```

---

## 👩‍💻 Author

**A. Nazeeha**
Final Year BSc Computer Science
AWS Certified Cloud Practitioner | Python | SQL | Data Engineering

🔗 [LinkedIn](https://www.linkedin.com/in/a-nazeeha)
🐙 [GitHub](https://github.com/nazeeha2406/Student-Mark-Analytics-Project)