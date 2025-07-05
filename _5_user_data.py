'''
Title : User Data file for emooffee
Data Created : April 3, 2023 | Last Updated : April 3, 2023
Language : Python 3.11.2
'''


# ----- Imports
from datetime import datetime
import ast


# ----- Variable initialization 
user_data_dic = {}


# ----- File reading and updating 
with open("user_data_file.txt", 'r') as read_data_file:

    now = datetime.now()
    date_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

    udd_content = read_data_file.read()
    udd_content = ast.literal_eval(udd_content)

    # Append to the exisiting
    with open("user_data.txt", 'w') as write_data_file:

        curr_user_data = ['blob', 'emotion type','coffee type', 'coffee levels', 'feedback']

        #user_data_dic[] = curr_user_data

        udd_content[date_time_string] = curr_user_data

        print(str(udd_content))

        write_data_file.write(str(udd_content))
