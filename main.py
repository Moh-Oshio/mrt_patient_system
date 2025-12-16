from random import randint
from datetime import datetime, date
import os

# Storage for running card numbers
card_nums = []


class Reception:
    """This class helps the Reception section store information relevant to a patient such as name, address, age, phone number etc. It also provides methods for creating anew card, accessing a patient's card and recording vital signs"""

    def __init__(self):
        try:
            with open("file_numbers.txt", "r") as file:
                for line in file:
                    number = line.strip()
                    if number and number not in card_nums:
                        card_nums.append(number)
        except FileNotFoundError:
            pass

        self.folder = "patients"

        os.makedirs(self.folder, exist_ok=True)

    def num_gen(self):
        rand_num = str(randint(100, 5000))
        def_len = 6
        new_num = ((def_len - len(rand_num)) * "0") + rand_num

        card_nums.append(new_num)

        with open("file_numbers.txt", "a") as file:
            file.write(f"{new_num}\n")

        return new_num

    def create_card(self):
        file_no = card_nums[-1]

        name = input("Enter patient's name: \n\n").upper()
        sex = input("Male or Female? \n\n").title()
        dob = input("\nEnter date of birth in the format: dd/mm/yyyy: \n\n")
        dob_date = datetime.strptime(dob, "%d/%m/%Y").date()

        today = date.today()
        age = today.year - dob_date.year

        if (today.month, today.day) < (dob_date.month, dob_date.day):
            age -= 1

        address = input("\nEnter address: \n\n")
        phone_number = input("\nEnter phone number: \n\n")

        file_path = os.path.join(self.folder, f"{file_no}.txt")

        with open(file_path, "a") as file:
            file.write(
                f"--- PATIENT CARD CREATED ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n"
            )
            file.write(f"File Number: {file_no}\n")
            file.write(f"Name of Patient: {name}\n")
            file.write(f"Sex: {sex}\n")
            file.write(f"Age: {age} years\n")
            file.write(f"Address: {address}\n")
            file.write(f"Phone: {phone_number}\n")

    def check_patient_file(self, card_number):
        file_path = os.path.join(self.folder, f"{card_number}.txt")

        if os.path.exists(file_path):
            print(f"\n---- Patient Record ({card_number}) ----\n")
            with open(file_path, "r") as file:
                print(file.read())
            print("------------------------\n")
            return True
        else:
            print(f"\nPatient file does not exist.\n")
            return False

    def vital_signs(self, card_no):
        file_path = os.path.join(self.folder, f"{card_no}.txt")

        if not os.path.exists(file_path):
            print("\nPatient file not found.")
            return

        print("\nEnter vital signs:\n")
        temp = input("Temperature (°C): ")
        bp = input("Blood Pressure (mmHg): ")
        pulse = input("Pulse (bpm): ")

        with open(file_path, "a") as file:
            file.write(
                f"\n--- VITAL SIGNS ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n"
            )
            file.write(f"Temperature: {temp}°C\n")
            file.write(f"Blood Pressure: {bp}mmHg\n")
            file.write(f"Pulse: {pulse} bpm\n")

        print("\nVital signs recorded successfully!\n")

    def all_records(self):
        return card_nums


class Doctor:
    """This class helps the Doctor record observations of the patient, diagnosis, prescription and additional notes."""

    folder = "patients"

    def enter_report(self, card_no):
        file_path = os.path.join(self.folser, f"{card_no}.txt")

        if not os.path.exists(file_path):
            print("\nPatient file not found")
            return

        print("\nEnter doctor's report:\n")
        diagnosis = input("Diagnosis: ")
        prescription = input("Prescription: ")
        notes = input("Additional Notes: ")

        # Appends the doctor's report to the patient file.
        with open(file_path, "a") as file:
            file.write(
                f"\n--- DOCTOR'S REPORT ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n"
            )
            file.write(f"Diagnosis: {diagnosis}\n")
            file.write(f"Prescription: {prescription}\n")
            file.write(f"Notes: {notes}\n")

        print("\nDoctor's report added successfully!\n")

    # Reads and displays the full text content of a patient file (Duplicate of Reception's method).
    def check_patient_file(self, card_number):
        file_path = os.path.join(self.folder, f"{card_number}.txt")

        if os.path.exists(file_path):
            print(f"\n---- Patient Record ({card_number}) ----\n")
            with open(file_path, "r") as file:
                print(file.read())
            print("------------------------\n")
            return True
        else:
            print(f"\nPatient file does not exist.\n")
            return False


class Nurse:
    """Helps the Nurse record observations and take notes about a patient"""

    folder = "patients"

    def enter_notes(self, card_no):
        file_path = os.path.join(self.folder, f"{card_no}.txt")

        if not os.path.exists(file_path):
            print("\nPatient file not found.")
            return

        print("\nEnter nurse's notes:\n")
        observations = input("Observations: ")
        care = input("Care given: ")

        # Appends the nurse's notes to the patient file.
        with open(file_path, "a") as file:
            file.write(
                f"\n--- NURSE'S NOTES ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n"
            )
            file.write(f"Observations: {observations}\n")
            file.write(f"Care: {care}\n")

        print("\nNurse's notes added successfully!\n")
