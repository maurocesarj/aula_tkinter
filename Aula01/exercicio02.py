from tkinter import *


# Back-end
def imprimir():
    label1['text'] = entry1.get()

# Front-end
# ============================ #
# Janela
janela = Tk()
janela.title('Teste')
janela.geometry('400x200+100+500')
janela.minsize(width=400, height=200)
janela.maxsize(width=800, height=400)
janela.config(bg='blue')

# Widgets
label1 = Label(janela, text='Olá mundo', font='Arial 36 bold')
entry1 = Entry(janela, font='Arial 36')
btn1 = Button(janela, text='Sair', font='Arial 36', command=quit)
btn2 = Button(janela, text='imprimir', font='Arial 36', command=imprimir)

label1.pack(side=TOP)
entry1.pack(side=TOP)
btn1.pack(side=TOP)
btn2.pack(side=TOP)

# Executar
janela.mainloop()