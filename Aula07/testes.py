from tkinter import *

import funcoes
from funcoes import *

# criação da janela e configuração do bg
root = Tk()
root.geometry("1280x768")
bg = PhotoImage(file="back.png")
root.configure(bg="#5CE1E6")
# label para definir bg
label1 = Label(root, image=bg)
label1.place(x=0, y=0)
# comando Enter
root.bind('<Return>', lambda event:(funcoes.Cadastro.dados_login(entryUsername, entryPassword)))

# label
username = Label(root, text="Username",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
username.place(x=465, y=320)
# Linha 01
linhaName = Label(root, text="________________________________",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
linhaName.place(x=465, y=375)

password = Label(root, text="Password",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
password.place(x=465, y=420)
# linha 02
linhaPassword = Label(root, text="________________________________",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
linhaPassword.place(x=465, y=475)
# Botão
login = Button(root, text="Login", font='Arial 15', bg="#5CE1E6", foreground='white', bd=0, padx=97, pady=17, cursor="hand2", command=lambda: funcoes.Cadastro.dados_login(entryUsername, entryPassword))
login.place(x=512, y=525)

# Entry Username
entryUsername = Entry(root, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=27)
entryUsername.place(x=467, y=365)
# Entry Password
entryPassword = Entry(root, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=27, show="*")
entryPassword.place(x=467, y=465)




# iniciaçização e configuração da janela
root.resizable(False, False)
root.mainloop()