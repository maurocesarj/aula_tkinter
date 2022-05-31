# import da biblioteca
from tkinter import *

# criação da janela
janela = Tk()
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)



janela.title('Aula')
janela.config(bg="#0B0B0B")

# criação dos botoes
btn1 = Button(janela, text='Bt 01', font='Arial 25', foreground='white', bg="#0B0B0B")
btn2 = Button(janela, text='Bt 02', font='Arial 25', foreground='white', bg="#0B0B0B")
btn3 = Button(janela, text='Bt 03', font='Arial 25', foreground='white', bg="#0B0B0B")
btn4 = Button(janela, text='Bt 04', font='Arial 25', foreground='white', bg="#0B0B0B")
btn5 = Button(janela, text='Bt 05', font='Arial 25', foreground='white', bg="#0B0B0B")
btn6 = Button(janela, text='Bt 06', font='Arial 25', foreground='white', bg="#0B0B0B")

#
btn1.grid(row=0, column=0, sticky=NSEW)
btn2.grid(row=0, column=1, sticky=NSEW)
btn3.grid(row=0, column=2, sticky=NSEW)
btn4.grid(row=1, column=0, sticky=NSEW)
btn5.grid(row=1, column=1, sticky=NSEW)
btn6.grid(row=1, column=2, sticky=NSEW)

# executar
janela.mainloop()