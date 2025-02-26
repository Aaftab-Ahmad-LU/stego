import cv2
import os
from tkinter import *
from tkinter import filedialog

def encrypt_message():
    filepath = filedialog.askopenfilename()
    img = cv2.imread(filepath)
    
    msg = message_entry.get()
    password = passcode_entry.get()
    
    d = {}
    for i in range(255):
        d[chr(i)] = i

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")

    # Save the length of the message to a file
    with open("message_length.txt", "w") as f:
        f.write(str(len(msg)))

def run_encrypt_gui():
    # Create the GUI window
    root = Tk()
    root.title("Steganographic Encryption")

    # Message entry field
    Label(root, text="Enter secret message:").grid(row=0, column=0)
    global message_entry
    message_entry = Entry(root)
    message_entry.grid(row=0, column=1)

    # Passcode entry field
    Label(root, text="Enter passcode:").grid(row=1, column=0)
    global passcode_entry
    passcode_entry = Entry(root, show="*")
    passcode_entry.grid(row=1, column=1)

    # Encrypt button
    Button(root, text="Encrypt", command=encrypt_message).grid(row=2, column=0, columnspan=2)

    root.mainloop()
