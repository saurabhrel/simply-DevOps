import tkinter as tk

class UserForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry fields for user input
        self.name_label = tk.Label(self, text="Name:")
        self.name_entry = tk.Entry(self)

        self.email_label = tk.Label(self, text="Email:")
        self.email_entry = tk.Entry(self)

        self.age_label = tk.Label(self, text="Age:")
        self.age_entry = tk.Entry(self)

        # Create a button to submit the form
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)

        # Pack the labels, entry fields, and button into the frame
        self.name_label.pack()
        self.name_entry.pack()

        self.email_label.pack()
        self.email_entry.pack()

        self.age_label.pack()
        self.age_entry.pack()

        self.submit_button.pack()

    def submit(self):
        # Get the user input from the entry fields
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()

        # Do something with the user input
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Age: {age}")

# Create a window and add the UserForm to it
root = tk.Tk()
user_form = UserForm(root)
user_form.pack()

# Start the main loop
root.mainloop()

