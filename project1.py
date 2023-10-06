def password():
    import random
    import string

    password_length = 12

    characters = string.ascii_letters + string.digits + string.punctuation

    pass_random = ''.join(random.choice(characters) for _ in range (password_length))

    print("Your password: ", pass_random)

def gui_password():
    import tkinter as tk
    import random
    import string

    def generate_password():
        length = int(length_entry.get())
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        password_result.config(text="Password: " + password)

    window = tk.Tk()
    window.title("Random Password Generator")

    length_label = tk.Label(window, text="Panjang Password: ")
    length_label.pack(pady=25)

    length_entry = tk.Entry(window)
    length_entry.pack()

    generate_button = tk.Button(window, text="Generate Password", command=generate_password)
    generate_button.pack(padx=25)

    password_result = tk.Label(window, text="")
    password_result.pack()

    window.mainloop()

while True:
    UserInput = int(input("Create Your new Password: \n\n1. System Password \n2. GUI Password \n3. OUT \n\nPut Your Choice: "))
    if UserInput == 1:
        password()
    elif UserInput == 2:
        gui_password()
    else:
        break