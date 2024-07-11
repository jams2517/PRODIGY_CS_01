import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount
            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) - shift_amount
            if char.islower():
                if char_code < ord('a'):
                    char_code += 26
                decrypted_text += chr(char_code)
            elif char.isupper():
                if char_code < ord('A'):
                    char_code += 26
                decrypted_text += chr(char_code)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer for shift value.")
        return

    encrypted = caesar_cipher_encrypt(text, shift)
    result_text.set(encrypted)

def decrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer for shift value.")
        return

    decrypted = caesar_cipher_decrypt(text, shift)
    result_text.set(decrypted)

app = tk.Tk()
app.title("Caesar Cipher")

# Text input
tk.Label(app, text="Enter the text:").pack()
text_entry = tk.Text(app, height=5, width=50)
text_entry.pack()

# Shift value input
tk.Label(app, text="Enter the shift value:").pack()
shift_entry = tk.Entry(app)
shift_entry.pack()

# Buttons for encryption and decryption
encrypt_button = tk.Button(app, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Result display
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, wraplength=400, justify="left")
result_label.pack()

app.mainloop()
