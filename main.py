from random import randint
from datetime import datetime, date
import os

# Storage for running card numbers
card_nums = []

# Implementation of the Reception Class.
# This class helps the Reception store the information of a new patient and record time of visit for the new patient.


class Reception:
    """Initializes the system by reading existing file numbers and creating the patient directory"""

    def __init__(self):
        try:
            with open('file_numbers.txt', 'r') as file:
                for line in file:
                    number = line.strip()
                    if number and number not in card_nums:
                        card_nums.append(number)
        except FileNotFoundError:
            pass

        self.folder = 'patients'

        os.makedirs(self.folder, exist_ok=True)

    def num_gen(self):
        rand_num = str(randint(100, 5000))
        def_len = 6
        new_num = (((def_len - len(rand_num)) * '0') + rand_num)

        card_nums.append(new_num)

        with open('file_numbers.txt', 'a') as file:
            file.write(f'{new_num}\n')

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

        with open(file_path, 'a') as file:
            file.write(
                f"--- PATIENT CARD CREATED ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---\n")
            file.write(f'File Number: {file_no}\n')
            file.write(f'Name of Patient: {name}\n')
            file.write(f'Sex: {sex}\n')
            file.write(f'Age: {age} years\n')
            file.write(f'Address: {address}\n')
            file.write(f'Phone: {phone_number}\n')
