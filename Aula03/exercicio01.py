from tkinter import *


# Back-end
def calcular():
    if (entrar_peso.get().replace('.', '', 1).isdigit()) and (entrar_altura.get().replace('.', '', 1).isdigit()):
        peso = float(entrar_peso.get())
        altura = float(entrar_altura.get())
        imc = peso / (altura*altura)
        resultado['text'] = round(imc, 2)
    else:
        pass

# Front-end
# ============================ #
# Janela
janela = Tk()
janela.title('IMC')
janela.geometry('400x155')
janela.configure(bg="#0B0B0B")

# Widgets
indicar_peso = Label(janela, text='Peso:', font='Arial 18', foreground='white',bg="#0B0B0B")
indicar_altura = Label(janela, text='Altura:', font='Arial 18', foreground='white',bg="#0B0B0B")
entrar_peso = Entry(janela, font='Arial 18', bg="#0B0B0B", foreground='white')
entrar_altura = Entry(janela, font='Arial 18', bg="#0B0B0B",foreground='white')
botao = Button(janela, font='Arial 18', text='Calcular IMC',command=calcular)
resultado = Label(janela, font='Arial 20', text=' ', bg="#0B0B0B",foreground='white')


indicar_peso.grid(row=0, column=0, sticky=NSEW)
entrar_peso.grid(row=0, column=1, sticky=NSEW)
indicar_altura.grid(row=1, column=0, sticky=NSEW)
entrar_altura.grid(row=1, column=1, sticky=NSEW)
botao.grid(row=3, column=1, sticky=NSEW)
resultado.grid(row=4, column=1, sticky=NSEW)


# Executar
janela.mainloop()