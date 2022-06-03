from tkinter import *

import funcoes
from funcoes import *
# funçao


# criação do tkinter

app = Tk()
app.title('Calculadora')
app.configure(bg='#383735')
app.geometry('320x500')

# rowconfigure
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)
app.grid_rowconfigure(5, weight=1)

# columnconfigure
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)


# visor
visor = Label(app, text='', font='Arial 25', pady=15, anchor=NE, foreground='white', bg='#2E2E2E')

# numeros
btn1 = Button(app, text='1', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '1'))
btn2 = Button(app, text='2', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '2'))
btn3 = Button(app, text='3', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '3'))
btn4 = Button(app, text='4', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '4'))
btn5 = Button(app, text='5', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '5'))
btn6 = Button(app, text='6', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '6'))
btn7 = Button(app, text='7', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '7'))
btn8 = Button(app, text='8', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '8'))
btn9 = Button(app, text='9', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '9'))
btn0 = Button(app, text='0', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '0'))

# operadores e funcoes
btnmult = Button(app, text='*', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '*'))
btndivi = Button(app, text='/', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '/'))
btnsoma = Button(app, text='+', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '+'))
btnmenos = Button(app, text='-', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '-'))

btnponto = Button(app, text='.', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '.'))
btndel = Button(app, text='DEL', font='Arial 15', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.apagartudo(visor))
btnC = Button(app, text='C', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.apagarUltimo(visor))
btnesquerda = Button(app, text='(', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, '('))
btndireita = Button(app, text=')', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda: funcoes.calculadora.entrada(visor, ')'))
btnigual = Button(app, text='=', font='Arial 20', foreground='white', bg='#2E2E2E', padx=12, pady=12, command=lambda : funcoes.calculadora.saida(visor))


# grid
# primeira fileira
visor.grid(row=0, column=0, columnspan=4, sticky=NSEW)
btn7.grid(row=1, column=0, sticky=NSEW)
btn8.grid(row=1, column=1, sticky=NSEW)
btn9.grid(row=1, column=2, sticky=NSEW)
btnmult.grid(row=1, column=3, sticky=NSEW)
# segunda fileira
btn4.grid(row=2, column=0, sticky=NSEW)
btn5.grid(row=2, column=1, sticky=NSEW)
btn6.grid(row=2, column=2, sticky=NSEW)
btndivi.grid(row=2, column=3, sticky=NSEW)
# terceira fileira
btn1.grid(row=3, column=0, sticky=NSEW)
btn2.grid(row=3, column=1, sticky=NSEW)
btn3.grid(row=3, column=2, sticky=NSEW)
btnsoma.grid(row=3, column=3, sticky=NSEW)
# quarta fileira
btn0.grid(row=4, column=0, sticky=NSEW)
btnigual.grid(row=4, column=1, sticky=NSEW)
btnponto.grid(row=4, column=2, sticky=NSEW)
btnmenos.grid(row=4, column=3, sticky=NSEW)
# quinta fileira
btndel.grid(row=5, column=0, sticky=NSEW)
btnC.grid(row=5, column=1, sticky=NSEW)
btnesquerda.grid(row=5, column=2, sticky=NSEW)
btndireita.grid(row=5, column=3, sticky=NSEW)



app.mainloop()



