""" Importing module requests """
import requests
""" Import Tkinter objects """
from tkinter import Tk, Button, Label

class AppUI():
    def __init__(self, master, button_command):
        """ Init method """
        self.master = master
        self.label = Label(master, text="Press for a random fact")
        self.button = Button(master, text="Fact", command=button_command)

        # Grid system
        self.label.grid(row=0, column=0, padx=5, pady=5)
        self.button.grid(row=1, column=0, padx=5, pady=5)

        self.master.mainloop()

def gen_new_fact(master):
    """ Generates random fact """
    # API url
    url = "https://cat-fact.herokuapp.com/facts/random"

    # Data retrieval
    data = requests.get(url).json()

    # Display the data
    display_label = Label(master, text=data['text']).grid(row=2, column=0, padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()
    ui = AppUI(root, lambda: gen_new_fact(root))
