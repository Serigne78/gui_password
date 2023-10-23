from tkinter import *










#Backend------------------------------------------
def add():
      valeur_web = input_website.get()
      valeur_password = input_password.get()
      valeur_user = input_email.get()
      
      # Ouvre un fichier en mode ajout ('a')
      with open('data.txt', 'a') as fichier:
      # Écrit du texte à la fin du fichier
            fichier.write(f"{valeur_web}|{valeur_user}|{valeur_password}\n")
            input_website.delete(0, END)
            input_password.delete(0, END)

def generate():
      #Password Generator Project
      import random
      letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
      numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
      symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

      
      nr_letters= 5
      nr_symbols = 5
      nr_numbers = 5


      #Hard Level - Order of characters randomised:
      #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
      mdp = []
      mdp1 = []
      for i in range(nr_letters):
             mdp.append(letters[i])

      for i in range(nr_symbols):
            mdp.append(numbers[i])

      for i in range(nr_numbers):
            mdp.append(symbols[i])

      mot = random.shuffle(mdp)
      mot  ="".join(mdp)
      input_password.insert(0, mot)



# Le fichier est automatiquement fermé lorsque le bloc `with` se termine





window = Tk()
window.title("Your Password")
window.config(padx=20, pady=20)
#--------------Sauvegegarde----------


canvas = Canvas(width=350, height=350)
image = PhotoImage(file="bacround_password.png")  # Chargez l'image dans une variable
canvas.create_image(125, 125, image=image)  # Utilisez la variable contenant l'image
canvas.grid(column=1, row=0)

my_website = Label(text="Website:", font=14)
my_website.grid(column=0, row=1)
input_website = Entry(width=35)
input_website.focus()
input_website.grid(column=1, row=1)

my_email = Label(text="Email/Username:",font=14 )
my_email.grid(column=0, row=2)
input_email = Entry(width=35)
input_email.insert(0, "abo78neauphle@gmail.com")
input_email.grid(column=1, row=2)

my_password = Label(text="Password:",font=14 )
my_password.grid(column=0, row=3)
input_password = Entry(width=21)
input_password.grid(column=1, row=3)

button_password = Button(text="Generate Password", font=14, command=generate)
button_password.grid(column=2, row=3)
button_add = Button(text="Add", font=14, width=36, command=add)
button_add.grid(column=1, row=4)

#Backend------------------------------------------




window.mainloop()






