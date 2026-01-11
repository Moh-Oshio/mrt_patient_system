# MRT Patient Recording System

A Python-based Command Line Interface (CLI) application for hospital management, utilizing Object-Oriented Programming (OOP) to handle medical records across different staff roles.

# Key Features
- **Role-Based Access Control:** Distinct workflows for Records, Doctors, and Nurses.
- **Inheritance-Based Architecture:** Uses a `HospitalStaff` base class to manage shared file operations, adhering to DRY (Don't Repeat Yourself) principles.
- **Unique ID Generation:** Automatically generates and tracks 6-digit patient card numbers.
- **Persistent Data Storage:** Saves patient history, vitals, and reports to local text files.

## Implementation
This project was built to demonstrate clean code practices in Python, specifically:
- **Inheritance & Polymorphism:** Roles inherit common functionality from a parent class.
- **File I/O:** Reading and appending to structured text files.
- **Error Handling:** Managing invalid inputs and date formatting issues.

## How to Run
1. Ensure you have Python 3.x installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/Moh-Oshio/mrt_patient_system.git
