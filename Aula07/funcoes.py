
class Cadastro():

    def dados_login(entry1, entry2):
        global armazenar_nome
        armazenar_nome = entry1.get()
        global armazenar_senha
        armazenar_senha = entry2.get()
        print(armazenar_senha, armazenar_nome)