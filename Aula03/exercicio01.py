from tkinter import *


# Back-end
def calcular():
    if (entrar_peso.get().replace('.', '', 1).isdigit()) and (entrar_altura.get().replace('.', '', 1).isdigit()):
        peso = float(entrar_peso.get())
        altura = float(entrar_altura.get())
        imc = peso / (altura*altura)
        resultado['text'] = round(imc, 2)
    else:
        resultado['text'] = 'Entrada Invalida'

# Front-end
# ============================ #
# Janela
janela = Tk()
janela.title('IMC')
janela.geometry('400x155')
janela.configure(bg="#272626")
janela.bind('<Return>', lambda event:calcular())

# Widgets
indicar_peso = Label(janela, text='Peso:', font='Arial 18', foreground='white',bg="#272626")
indicar_altura = Label(janela, text='Altura:', font='Arial 18', foreground='white',bg="#272626")
entrar_peso = Entry(janela, font='Arial 18', bg="#272626", foreground='white')
entrar_altura = Entry(janela, font='Arial 18', bg="#272626",foreground='white')
botao = Button(janela, font='Arial 18', text='Calcular IMC',command=calcular)
resultado = Label(janela, font='Arial 20', text=' ', bg="#272626",foreground='white')


indicar_peso.grid(row=0, column=0, sticky=NSEW)
entrar_peso.grid(row=0, column=1, sticky=NSEW)
indicar_altura.grid(row=1, column=0, sticky=NSEW)
entrar_altura.grid(row=1, column=1, sticky=NSEW)
botao.grid(row=3, column=1, sticky=NSEW)
resultado.grid(row=4, column=1, sticky=NSEW)


# Executar
janela.mainloop()