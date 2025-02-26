import tkinter as tk
import encrypt_gui
import decrypt_gui

def open_encrypt_gui():
    encrypt_gui.run_encrypt_gui()

def open_decrypt_gui():
    # Prompt the user for the encryption password before opening the decryption GUI
    encryption_password = input("Enter the password used during encryption: ")
    decrypt_gui.run_decrypt_gui(encryption_password)

# Create the main window
root = tk.Tk()
root.title("Main Menu")

# Create buttons to open encryption and decryption GUIs
btn_encrypt = tk.Button(root, text="Open Encryption GUI", command=open_encrypt_gui)
btn_encrypt.grid(row=0, column=0, padx=20, pady=20)

btn_decrypt = tk.Button(root, text="Open Decryption GUI", command=open_decrypt_gui)
btn_decrypt.grid(row=0, column=1, padx=20, pady=20)

root.mainloop()
