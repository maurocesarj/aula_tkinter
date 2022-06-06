from tkinter import *


# Back-end
def calcular():
    if entrar_c.get().replace('.', '', 1).isdigit():
        c = float(entrar_c.get())
        f = c * 1.8 + 32
        resultado['text'] = f

    else:
        pass

# Front-end
# ============================ #
# Janela
janela = Tk()
janela.title('CONVERTER C EM F')

fr1 = Frame(janela)
fr2 = Frame(janela)

# Widgets
indicar_c = Label(fr1, text='C°:', font='Arial 18', foreground='white',bg="#272626")
entrar_c = Entry(fr1, font='Arial 18', bg="#272626", foreground='white')
botao = Button(fr2, font='Arial 18', text='Converter °F:', command=calcular)
resultado = Label(fr2, font='Arial 20', text=' ', bg="#272626", foreground='white')

fr1.pack()
fr2.pack()

indicar_c.grid(row=0, column=0, sticky=NSEW)
entrar_c.grid(row=0, column=1, sticky=NSEW)
botao.grid(row=2, column=0, sticky=NSEW)
resultado.grid(row=2, column=1, sticky=NSEW)


# Executar
janela.mainloop()