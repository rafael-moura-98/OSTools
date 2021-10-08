import PySimpleGUI as sg

class telaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button('Enviar Dados')]
        ]

        #Janela
        window = sg.Window("Dados do Usuario").layout(layout)

        #Extrair dados da tela
        self.button, self.values = window.Read()

    def Start(self):
        print(self.values)

tela = telaPython()
tela.Start()