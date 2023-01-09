import PySimpleGUI as sg

class telaPython:
    def __init__(self):
        sg.theme('LightBlue2')

        layout = [
            [sg.Text('EXPRESSION:')],
            [sg.Input()],
            [sg.Button('Calculate')]
        ]

        self.window = sg.Window(
            'Calculate Expression',
            layout=layout,
            grab_anywhere=True,
            finalize=True
        )

        self.screen_width, self.screen_height = self.window.get_screen_size()
        self.window_width, self.window_height = self.window.size
        self.window.bind('<Escape>', '-ESCAPE-')
        self.window.bind('<Key-Return>', '-ENTER-')

    def run(self):
        # Extrair dados da tela
        self.event, self.values = self.window.Read()

        if self.event in (sg.WINDOW_CLOSED, '-ESCAPE-'):
            exit()
        
        if self.event in ('-ENTER-', 'Calculate'):
            print('Calculate was pressed!')
            print(self.values)

    def windows_botton_right(self):
        x = (self.screen_width - self.window_width - 50)
        y = (self.screen_height - self.window_height - 100)
        self.window.move(x, y)


tela = telaPython()
tela.windows_botton_right()
while True:
    tela.run()

