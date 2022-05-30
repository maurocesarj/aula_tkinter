from tkinter import *


# Back-end
def imprimir():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        numero1 = float(entry1.get())
        numero2 = float(entry2.get())
        label1['text'] = numero1 + numero2
        label1['bg'] = 'white'
        label1['foreground'] = 'black'
    else:
        label1['text'] = 'Não tem como'
        label1['bg'] = 'red'
        label1['foreground'] = 'yellow'
        janela['bg'] = 'red'

# Front-end
# ============================ #
# Janela
janela = Tk()
janela.title('Teste')
janela.geometry('500x800+100+500')
janela.config(bg='white')

# Widgets
label1 = Label(janela, text='Resultado', font='Arial 36', foreground='black', bg='white')
entry1 = Entry(janela, font='Arial 36')
entry2 = Entry(janela, font='Arial 36')
btn1 = Button(janela, text='Mostrar', font='Arial 36', command=imprimir)


label1.pack(side=TOP)
entry1.pack(side=TOP)
entry2.pack(side=TOP)
btn1.pack(side=TOP)

# Executar
janela.mainloop()