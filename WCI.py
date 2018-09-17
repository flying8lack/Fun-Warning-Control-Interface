from tkinter import Tk, Button, Entry, messagebox, Label

class App:
    def __init__(self, master):
        self.master = master
        master.title("Warning Control Interface")
        master.geometry("300x110")

        self.message_title = Entry(master)
        self.message_title.grid(row=1, column=50)

        self.message_title_text = Label(master, text="Title: ")
        self.message_title_text.grid(row=1, column=40)
        
        self.message_content = Entry(master)
        self.message_content.grid(row=3, column=50)

        self.message_content_text = Label(master, text="Message content: ")
        self.message_content_text.grid(row=3, column=40)

        self.wrn_btn = Button(master, text="Generate the warning!", command=self.warn, fg="red")
        self.wrn_btn.grid(row=7, column=50)

    def warn(self):
        messagebox.showwarning(self.message_title.get(), self.message_content.get())

root = Tk()
page = App(root)
root.mainloop()
