import gspread
from google.oauth2.service_account import Credentials
import random
import pandas as pd
import numpy as np



def input_type():
    """
    User input for whether to add a start a new bill, add a new item, or edit an item
    """
    while True:
        print('Would you like to start a new bill, add a new item, or edit an item?')
        data_str = input(
            'Please enter "start" for new bill or "new" for adding a new item, "update" to updat an item currently in the list or "delete" to remove an existing item: \n')

        if validate_data(data_str):
            break

    return data_str



# Giving the user more variety for initial input
start = ["start", "START", "Start"]
new = ["new", "NEW", "New"]
updater = ["update", "UPDATE", "Update"]
delete = ["delete", "DELETE", "Delete"]
# Combining the options
user_options = start + new + updater + delete


def validate_data(data):
    """
    Test user input matches options provided
    """
    try:
        if data not in user_options:
            raise ValueError(f'You entered {data}, you need to enter "new",'
                             ' "update" or "delete" to continue')
    except ValueError as e:
        print(f'Invalid data: {e}, please try again. \n')
        return False

    return True

def split(data):
    """
    Creates the bill depending on user inputs
    """
    if data in start:
        """
        Takes the user input and starts a new bill
        """
        print('new bill')
    elif data in new:
        """
        Adds a new item to the bill
        """
        print('new item')
    elif data in updater:
        """
        Updates an existing item in the bill
        """
        print('update bill')
    elif data in delete:
        """
        Deletes the item requested
        """
        print('delete bill')
    else:
        print('Invalide entry. Please try again.')

def main():
    """
    run all functions
    """
    input = input_type()
    split(input)

# Run intro first as if the user wants to reuse the tool,
# we don't want the intro to run again
#run_intro()
print("Let's split this bill! \n")
main()

