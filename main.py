from tkinter import *
from tkinter.ttk import Combobox
import subprocess


class MyApp:

    def __init__(self):
        # input values
        self.input_values = []

        self.window = Tk()
        self.window.title("Linkedin Scraper")
        self.window.geometry("1110x550")
        self.window.minsize(480, 360)
        self.window.iconbitmap("robot.ico")
        self.window.config(background='#094F6E')

        # initialization des composants
        self.frame1 = Frame(self.window, bg='#094F6E')
        self.frame2 = Frame(self.window, bg='#094F6E')
        self.width = 300
        self.height = 300
        self.image = PhotoImage(file="linkedin.png").zoom(15).subsample(32)
        self.canvas = Canvas(self.frame1, width=self.width, height=self.height, bg="#094F6E", bd=0,
                             highlightthickness=0)

        # creation des composants
        self.create_widgets()
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.image)

        # empaquetage
        self.canvas.pack(side=TOP, pady=10)
        self.frame1.pack(side=LEFT, padx=10)

        self.frame2.pack(side=LEFT, padx=10, pady=10)

        # Create input fields and button
        self.create_input_fields()
        self.create_message_input()
        self.create_button()

    def create_widgets(self):
        self.create_title()

        # Create a search input field
        label_search = Label(self.frame1, text="Search", font=("Trebuchet MS", 20), bg='#094F6E', fg='white')
        label_search.pack(side=TOP, padx=10, pady=10)
        entry_search = Entry(self.frame1, width=30)
        entry_search.pack(side=TOP, padx=10, pady=10)
        self.input_values.append(entry_search)

    def create_title(self):
        label_title = Label(self.frame1, text="Search Filter", font=("Trebuchet MS", 30), bg='#094F6E', fg='white')
        label_title.pack(side=TOP, padx=10, pady=10)

    def create_input_fields(self):
        # Create 12 input fields with 2 input cases in every line
        input_labels = ["Connections", "Connections of", "Followers of", "Location", "Talks about", "Current company",
                        "Past company", "School", "Industry", "Profile language", "Open to", "Service categories"]
        for i in range(6):
            for j in range(2):
                label = Label(self.frame2, text=input_labels[i * 2 + j], font=("Trebuchet MS", 12), bg='#094F6E',
                              fg='white')
                label.grid(row=i, column=j * 2, padx=10, pady=10)

                if i * 2 + j in [0, 9, 10]:  # create combobox for Label 1, Label 10, and Label 11
                    values = []
                    if i * 2 + j == 0:  # populate combobox for Label 1
                        values = ["", "1st", "2nd", "3rd+", "1st & 2nd", "1st & 3rd+", "2nd & 3rd+", "All"]
                    elif i * 2 + j == 9:  # populate combobox for Label 10
                        values = ["", "English", "French", "Portuguese", "Spanish", "Others"]
                    elif i * 2 + j == 10:  # populate combobox for Label 11
                        values = ["", "Pro bono consulting and volunteering", "Joining a nonprofit board", "Both"]
                    combobox = Combobox(self.frame2, width=27, values=values, state="readonly")
                    combobox.grid(row=i, column=j * 2 + 1, padx=10, pady=10)
                    self.input_values.append(combobox)
                else:  # create entry for other labels
                    entry = Entry(self.frame2, width=30)
                    entry.grid(row=i, column=j * 2 + 1, padx=10, pady=10)
                    self.input_values.append(entry)

    def create_message_input(self):
        # Create a message input field on the left side of the frame
        label = Label(self.frame2, text="Message", font=("Trebuchet MS", 12), bg='#094F6E', fg='white')
        label.grid(row=6, column=0, padx=10, pady=10)

        entry = Text(self.frame2, width=30, height=5)
        entry.grid(row=6, column=1, columnspan=3, padx=10, pady=10)
        self.input_values.append(entry)

    def create_button(self):
        # Create a send button on the right side of the frame
        button_send = Button(self.frame2, text="Send", font=("Trebuchet MS", 12), bg='#094F6E', fg='white',
                             command=self.on_send)
        button_send.grid(row=6, column=4, padx=10, pady=20, sticky="E")

    def on_send(self):
        self.input_values = []
        for widget in self.frame1.winfo_children():
            if isinstance(widget, Entry):
                self.input_values.append(widget.get())
        for widget in self.frame2.winfo_children():
            if isinstance(widget, Entry) or isinstance(widget, Combobox):
                self.input_values.append(widget.get())
            elif isinstance(widget, Text):
                self.input_values.append(widget.get("1.0", "end-1c"))

        # Join all the inputs into a single string
        # input_string = " ".join(self.input_values)
        wait_label = Label(self.frame2, text="Wait", font=("Trebuchet MS", 12), bg="blue", fg="white")
        wait_label.grid(row=7, column=1, columnspan=3, padx=10, pady=10)
        # Run the command to scrape LinkedIn using the input string
        subprocess.run(["python", "linkedin.py", self.input_values[0], self.input_values[1], self.input_values[2],
                        self.input_values[3], self.input_values[4], self.input_values[5], self.input_values[6]
                        , self.input_values[7], self.input_values[8], self.input_values[9],
                        self.input_values[10], self.input_values[11], self.input_values[12], self.input_values[13]])
        self.window.after(10, wait_label.destroy)
        # Show success message
        success_label = Label(self.frame2, text="Done", font=("Trebuchet MS", 12), bg="green", fg="white")
        success_label.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

        # Hide success message after 2 seconds
        self.window.after(2000, success_label.destroy)


# afficher
app = MyApp()
app.window.mainloop()
