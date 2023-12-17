import webbrowser
from tkinter import *

def submit():
    site = entry.get()
    open_tab(site)

def clear():
    entry.delete(0, END)

def open_tab(url):
    webbrowser.open("https://" + url)
#--------------------------------------------------------
    
window = Tk()
entry = Entry() #textbox that will accept a single line of user input


clear = Button(window, text='Clear', command=clear)
clear.pack(side=RIGHT)

submit = Button(window, text="GO", command=submit)
submit.pack(side=RIGHT)

entry.config(font=('Times New Roman', 30),
             bg='#111111', #sets the background color
             fg='#FFFFFF') #sets the foreground color
#entry.config(show='*') #this replaces all characters typed into it with the character that show is set equal to
entry.pack()

window.mainloop()



if __name__ == "__main__":
    
    open_tab()