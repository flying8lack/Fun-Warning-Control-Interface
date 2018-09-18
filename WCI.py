from tkinter import Tk, Button, Entry, messagebox, Label, Menu, NORMAL
from tkinter.ttk import Progressbar

class App:
    def __init__(self, master):
        self.master = master
        master.title("Warning Control Interface")
        master.geometry("300x170")

        self.count_bar = Progressbar(master, mode='determinate', maximum=10)
        self.count_bar.grid(row=8, column=50, pady=10)

        self.ex_btn = Button(master, text="Fire!", command=self.warn, fg="red")

        #menu setup
        self.menu_obj = Menu(master)
        self.menu_obj.add_command(label="Hello", command=self.hello)
        self.menu_obj.add_command(label="Reset", command=self.reset)
        self.menu_obj.add_command(label="Fill", command=self.fill)
        #master config
        master.config(menu=self.menu_obj)


        self.message_title = Entry(master)
        self.message_title.grid(row=1, column=50)

        self.message_title_text = Label(master, text="Title: ")
        self.message_title_text.grid(row=1, column=40)
        
        self.message_content = Entry(master)
        self.message_content.grid(row=3, column=50)

        self.message_content_text = Label(master, text="Message content: ")
        self.message_content_text.grid(row=3, column=40)

        self.wrn_btn = Button(master, text="Generate the warning!", command=self.warn)
        self.wrn_btn.grid(row=7, column=50, pady=10)

    def warn(self):
        self.count_bar['value'] += 1
        messagebox.showwarning(self.message_title.get(), self.message_content.get())

        if self.count_bar['value'] >= 10:
            self.ex_btn.config(state=NORMAL)
            self.ex_btn.grid(row=10, column=50)

    def hello(self):
        messagebox.showwarning("!", "\"Hello there\" - codsworth")

    def reset(self):
        self.count_bar['value'] = 0
        self.ex_btn.grid_forget()

    def fill(self):
        self.count_bar['value'] = 10
        self.warn()

root = Tk()
page = App(root)
root.mainloop()
