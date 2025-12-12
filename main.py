from random import randint
from datetime import datetime, date
import os

# Storage for running card numbers
card_nums = []

# Implementation of the Reception Class.
# This class helps the Reception store the information of a new patient and record time of visit for the new patient.


class Reception:
    # Initializes the system by reading existing file numbers and creating the patient directory

    def __init__(self):
        # This attempts to load previously generated file numbers from the .txt file storing the file numbers.
        try:
            with open('file_numbers.txt', 'r') as file:
                for line in file:
                    number = line.strip()
                    if number and number not in card_nums:
                        card_nums.append(number)
        # If the file does not exist, an empty list is initialized.
        except FileNotFoundError:
            pass

        self.folder = 'patients'

        # This ensures the 'patients' folder exists. If it does, individual patient records are stored in it.

        os.makedirs(self.folder, exist_ok=True)


# In addition to the code in the constructor, methods for:
# - generating a random card number
# - creating a new patient card using the last generated number as the new patient card number
# - checking a patient file using the card number
# - recording vital signs of the patient upon entry into the hospital
