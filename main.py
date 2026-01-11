from random import randint
from datetime import datetime, date
import os

# Storage for running card numbers
card_nums = []


class HospitalStaff:

    def __init__(self):
        self.folder = "patients"
        os.makedirs(self.folder, exist_ok=True)

    def check_patient_file(self, card_number):
        """Reads and displays the full text content of a patient file."""
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


class Reception(HospitalStaff):
    """Handles patient registration, card creation, and vital signs."""

    def __init__(self):
        super().__init__()  # Calls the __init__ of HospitalStaff
        try:
            with open("file_numbers.txt", "r") as file:
                for line in file:
                    number = line.strip()
                    if number and number not in card_nums:
                        card_nums.append(number)
        except FileNotFoundError:
            pass

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

        try:
            dob_date = datetime.strptime(dob, "%d/%m/%Y").date()
            today = date.today()
            age = today.year - dob_date.year
            if (today.month, today.day) < (dob_date.month, dob_date.day):
                age -= 1
        except ValueError:
            print("Invalid date format. Card created with age unknown.")
            age = "Unknown"

        address = input("\nEnter address: \n\n")
        phone_number = input("\nEnter phone number: \n\n")

        file_path = os.path.join(self.folder, f"{file_no}.txt")
        with open(file_path, "a") as file:
            file.write(
                f"--- PATIENT CARD CREATED ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"File Number: {file_no}\n")
            file.write(f"Name of Patient: {name}\n")
            file.write(f"Sex: {sex}\n")
            file.write(f"Age: {age} years\n")
            file.write(f"Address: {address}\n")
            file.write(f"Phone: {phone_number}\n")

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
                f"\n--- VITAL SIGNS ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"Temperature: {temp}°C\n")
            file.write(f"Blood Pressure: {bp}mmHg\n")
            file.write(f"Pulse: {pulse} bpm\n")
        print("\nVital signs recorded successfully!\n")

    def all_records(self):
        return card_nums


class Doctor(HospitalStaff):
    """Handles clinical reports, diagnosis, and prescriptions."""

    def enter_report(self, card_no):
        # Fixed typo from folser
        file_path = os.path.join(self.folder, f"{card_no}.txt")

        if not os.path.exists(file_path):
            print("\nPatient file not found")
            return

        print("\nEnter doctor's report:\n")
        diagnosis = input("Diagnosis: ")
        prescription = input("Prescription: ")
        notes = input("Additional Notes: ")

        with open(file_path, "a") as file:
            file.write(
                f"\n--- DOCTOR'S REPORT ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"Diagnosis: {diagnosis}\n")
            file.write(f"Prescription: {prescription}\n")
            file.write(f"Notes: {notes}\n")
        print("\nDoctor's report added successfully!\n")


class Nurse(HospitalStaff):
    """Handles nursing observations and care notes."""

    def enter_notes(self, card_no):
        file_path = os.path.join(self.folder, f"{card_no}.txt")
        if not os.path.exists(file_path):
            print("\nPatient file not found.")
            return

        print("\nEnter nurse's notes:\n")
        observations = input("Observations: ")
        care = input("Care given: ")

        with open(file_path, "a") as file:
            file.write(
                f"\n--- NURSE'S NOTES ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f"Observations: {observations}\n")
            file.write(f"Care: {care}\n")
        print("\nNurse's notes added successfully!\n")


def main():
    print("Welcome to MRT Patient Recording System. \n\nWhat section would you like to access? \n")
    try:
        choice = int(input(
            "1. Records Section\n2. Doctor's Section\n3. Nurse's Section \n\nSelect a number and press Enter \n\n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == 1:
        staff = Reception()
        while True:
            choice = input(
                "\nReception Menu:\n1. Create a new file\n2. Enter vitals\n3. View Patient File\n4. View all card numbers\n5. Exit\n\nSelect a number: ")
            if choice == "1":
                print(f"\nNew number: {staff.num_gen()}\n")
                staff.create_card()
            elif choice == "2":
                staff.vital_signs(input("\nEnter file number: "))
            elif choice == "3":
                staff.check_patient_file(input("\nEnter file number: "))
            elif choice == "4":
                print(staff.all_records())
            elif choice == "5":
                break

    elif choice == 2:
        staff = Doctor()
        while True:
            choice = input(
                "\nDoctor's Menu:\n1. Enter Report\n2. View Patient File\n3. Exit\n\nSelect a number: ")
            if choice == "1":
                staff.enter_report(input("\nEnter card number: "))
            elif choice == "2":
                staff.check_patient_file(input("\nEnter card number: "))
            elif choice == "3":
                break

    elif choice == 3:
        staff = Nurse()
        while True:
            choice = input(
                "\nNurse's Menu:\n1. Enter Notes\n2. View Patient File\n3. Exit\n\nSelect a number: ")
            if choice == "1":
                staff.enter_notes(input("\nEnter card number: "))
            elif choice == "2":
                staff.check_patient_file(input("\nEnter card number: "))
            elif choice == "3":
                break


if __name__ == "__main__":
    main()
