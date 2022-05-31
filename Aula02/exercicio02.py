# import da biblioteca
from tkinter import *

def aumentar():
    if int(label1['text']) < 10:
        label1['text'] = int(label1['text']) + 1

    else:
        pass

def diminuir():
    if int(label1['text']) > -10:
        label1['text'] = int(label1['text']) - 1

    else:
        pass

# criação da janela
janela = Tk()
janela.grid_rowconfigure(0, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.bind('-', lambda event: diminuir())
janela.bind('+', lambda event: aumentar())



janela.title('Aula')
janela.config(bg="#0B0B0B")

# criação dos botoes
btn1 = Button(janela, text='-', font='Arial 25', foreground='white', bg="#0B0B0B", command=diminuir)
label1 = Label(janela, text='0', font='Arial 25', foreground='white', bg='#0B0B0B')
btn3 = Button(janela, text='+', font='Arial 25', foreground='white', bg="#0B0B0B", command=aumentar)

#
btn1.grid(row=0, column=0, sticky=NSEW)
label1.grid(row=0, column=1, sticky=NSEW)
btn3.grid(row=0, column=2, sticky=NSEW)

# executar
janela.mainloop()