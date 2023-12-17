import webbrowser

def open_tab():
    print("This script will open a tab in your default browser.\n")
    url = input("Enter the website you would like to visit: ")

    webbrowser.open("https://" + url)
    print("\nTab should've opend by now.\n")

if __name__ == "__main__":
    
    open_tab()