from bs4 import BeautifulSoup
import requests
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk() 
app.geometry("400x240")


url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name"
bulba = requests.get(url)
soup = BeautifulSoup(bulba.text, 'html.parser')

def invalid():
    error_message = customtkinter.CTkToplevel(app)
    error_message.title("Error")
    error_message.geometry("200x150")
    error_message.resizable(False)
    
    label = customtkinter.CTkLabel(error_message, text="Not a Pokemon", fg_color="transparent")
    label.place(relx = 0.25, rely=0.25)

def button_function():
    Pokemon = entry.get()


    if soup.find(title=Pokemon):
        info = soup.find(title=Pokemon).parent.parent.get_text()
        info = info.splitlines()
        info.pop(0)
        info.pop(1)

        s = info[0] + "\n" + info[1] + "\n"
        for i in range(len(info)-2):
            s = s + info[i+2] + " "
        results.configure(text=s)
    else:
        invalid()



button = customtkinter.CTkButton(master=app, text="Search", command=button_function)
button.place(relx = 0.1,y=150)

entry = customtkinter.CTkEntry(app, placeholder_text="Enter a Pokemon")
entry.place(relx= 0.1, y=100)
label = customtkinter.CTkLabel(app, text="Pokemon Search", fg_color="transparent")
label.place(relx = 0.1, y=50)

results = customtkinter.CTkLabel(app, text="", fg_color="transparent")
results.place(relx = .6, y=100)

app.mainloop()

