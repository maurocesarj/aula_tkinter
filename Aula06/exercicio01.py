from tkinter import *

# configuração e criação da janela
janela = Tk()
janela.title('Cadastro Pessoal')
janela.geometry('1100x375')
janela.configure(bg='#202124')


# criação dos frames
fr1 = Frame(pady=15)
fr2 = Frame(pady=15)
fr3 = Frame(pady=15)
fr1.configure(bg='#202124')
fr2.configure(bg='#202124')
fr3.configure(bg='#202124')

# criação Label
# frame 01
titulo = Label(fr1, text='Informações pessoais:', font='Arial 16', foreground='WHITE', width=18, height=1, anchor=SW, bg='#202124', pady=15)
nome = Label(fr1, text='Nome:', font='Arial 16',foreground='WHITE', bg='#202124')
entrar_Nome = Entry(fr1, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)
data_Nascimento = Label(fr1, text='Data Nascimento:', font='Arial 16',foreground='WHITE', bg='#202124')
entrar_Data = Entry(fr1, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)
cpf = Label(fr1, text='CPF:', font='Arial 16',foreground='WHITE', bg='#202124')
entra_cpf = Entry(fr1, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)
telefone = Label(fr1, text='Telefone:', font='Arial 16',foreground='WHITE', bg='#202124')
entra_telefone = Entry(fr1, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)

# Frame 02

endereco = Label(fr2, text='Endereço', font='Arial 17',foreground='WHITE', bg='#202124')
rua = Label(fr2, text='Rua: ', font='Arial 16',foreground='WHITE', bg='#202124')
entra_Rua = Entry(fr2, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)
bairro = Label(fr2, text='Bairro: ', font='Arial 16',foreground='WHITE', bg='#202124')
entra_Bairro = Entry(fr2, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)
cidade = Label(fr2, text='Cidade: ', font='Arial 16',foreground='WHITE', bg='#202124')
entra_Cidade = Entry(fr2, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)
numero = Label(fr2, text='N°: ', font='Arial 16',foreground='WHITE', bg='#202124')
entra_Numero = Entry(fr2, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)
uf = Label(fr2, text='UF: ', font='Arial 16',foreground='WHITE', bg='#202124')
entra_Uf = Entry(fr2, font='Arial 16', foreground='WHITE', bg='#202124', highlightbackground="#CB6CE6", highlightthickness=1, bd=0)

# frame 03
bt1 =  Button(fr3, text='Gravar Dados', font='Arial 16', foreground='white', bg='#202124')
bt2 =  Button(fr3, text='Limpar Dados', font='Arial 16', foreground='white', bg='#202124')



fr1.grid(row=0, sticky=EW)
fr2.grid(row=1)
fr3.grid(row=2)

titulo.grid(row=0, columnspan=2)
nome.grid(row=1, column=0)
entrar_Nome.grid(row=1, column=1)
data_Nascimento.grid(row=2, column=0)
entrar_Data.grid(row=2, column=1)
cpf.grid(row=1, column=4)
entra_cpf.grid(row=1, column=5)
telefone.grid(row=2, column=4)
entra_telefone.grid(row=2, column=5)

# frame 02
endereco.grid(row=0)
rua.grid(row=1, column=0)
entra_Rua.grid(row=1, column=1, columnspan=3, sticky=EW)
bairro.grid(row=2, column=0)
entra_Bairro.grid(row=2, column=1)
numero.grid(row=1, column=4)
entra_Numero.grid(row=1, column=5)
cidade.grid(row=2, column=2)
entra_Cidade.grid(row=2, column=3)
uf.grid(row=2, column=4)
entra_Uf.grid(row=2, column=5)

# frame 03
bt1.grid(row=0, column=0)
bt2.grid(row=0, column=1)

janela.mainloop()