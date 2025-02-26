import cv2
import os
from tkinter import *
from tkinter import filedialog

password = ""  # Global variable to store the password used for encryption
message_length = 0  # Global variable to store the length of the encrypted message

def decrypt_message():
    filepath = filedialog.askopenfilename()
    img = cv2.imread(filepath)
    
    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    message = ""
    n = 0
    m = 0
    z = 0

    for attempt in range(3):
        pas = passcode_entry.get()
        if password == pas:
            for i in range(message_length):
                message = message + c[img[n, m, z]]
                n = n + 1
                m = m + 1
                z = (z + 1) % 3
            message_label.config(text="Decryption message: " + message)
            break
        else:
            attempts_left = 2 - attempt
            message_label.config(text="Incorrect passcode. You have {} attempts left.".format(attempts_left))
    else:
        message_label.config(text="Maximum attempts reached. Decryption failed.")

def run_decrypt_gui(encryption_password):
    global password, message_length
    password = encryption_password

    # Read the length of the encrypted message from the file
    with open("message_length.txt", "r") as f:
        message_length = int(f.read())

    # Create the GUI window
    root = Tk()
    root.title("Steganographic Decryption")

    # Passcode entry field
    Label(root, text="Enter passcode:").grid(row=0, column=0)
    global passcode_entry
    passcode_entry = Entry(root, show="*")
    passcode_entry.grid(row=0, column=1)

    # Decrypt button
    Button(root, text="Decrypt", command=decrypt_message).grid(row=1, column=0, columnspan=2)

    # Message label for decryption result
    global message_label
    message_label = Label(root, text="")
    message_label.grid(row=2, column=0, columnspan=2)

    root.mainloop()
