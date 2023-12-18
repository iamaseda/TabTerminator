import tkinter
import customtkinter #must install customtkinter
import webbrowser

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def submit():
    site = entry.get()
    open_tab(site)

def clear():
    entry.delete(0, tkinter.END)

def open_tab(url):
    webbrowser.open("https://" + url)

#--------------------------------------------------------
    
window = customtkinter.CTkFrame(master=root)
window.pack(fill="both", expand=True)

label = customtkinter.CTkLabel(master=window, text="Tab Opener")
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=window, placeholder_text="Enter a website...") #textbox that will accept a line of user input
entry.pack()

submit = customtkinter.CTkButton(master=window, text="GO", command=submit)
submit.pack(pady=12, padx=10 )

clear = customtkinter.CTkButton(master=window, text='Clear', command=clear)
clear.pack(pady=12, padx=10)


entry.configure(font=('Times New Roman', 30)) 
#entry.configure(show='*') #this replaces all characters typed into it with the character that show is set equal to
entry.pack()

window.mainloop()