'''
Title : Base64 format to Image for Emooffee
Date Created : April 1, 2023 | Last Updated : April 2, 2023
Language : Python 3.11.2 
'''


# Importing base64 module
import base64

# Function for convertion
def img_convertion(file_loc):

    # Open file with base64 string data
    with open(file_loc, 'r') as file:
        encoded_data = file.read()
        encoded_data = encoded_data.split(",")
        img_data = encoded_data[-1]

    # decode base64 string data
    decoded_data=base64.b64decode(bytes(img_data,'utf-8'))

    # Write the base64 data back to image format
    img_file = open('C:/Users/navee/Downloads/image.jpeg', 'wb')
    img_file.write(decoded_data)
    img_file.close()

    curr_img_path = "C:/Users/navee/Downloads/image.jpeg"

    return curr_img_path


# Function call