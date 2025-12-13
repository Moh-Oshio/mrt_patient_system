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
