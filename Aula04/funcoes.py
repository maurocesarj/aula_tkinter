class calculadora():

    def entrada(label, valor):
        textooperacao = label['text']
        if textooperacao == 'Operação Inválida  ':
            label['text'] = ''
            label['font'] = 'Arial 20'
            label['text'] += valor
        else:
            label['text'] += valor

    def saida(label):
        operacao = label['text']
        if operacao[-1] == '+':
            label['text'] = 'Operação Inválida  '
            label['font'] = '25'

        elif operacao[-1] == '-':
            label['text'] = 'Operação Inválida  '
            label['font'] = '25'

        elif operacao[-1] == '*':
            label['text'] = 'Operação Inválida  '
            label['font'] = '25'

        elif operacao[-1] == '/':
            label['text'] = 'Operação Inválida  '
            label['font'] = '25'

        else:
            resultado = eval(label['text'])
            label['text'] = str(resultado)

    def apagartudo(label):
        label['text'] = ''
        label['font'] = 'Arial 20'

    def apagarUltimo(label):
        textolabel = label['text']
        label['text'] = textolabel[:-1]
