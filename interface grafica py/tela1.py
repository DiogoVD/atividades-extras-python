import PySimpleGUI as sg

class TelaPy:
    def __init__(self):
        sg.change_look_and_feel('DarkBlue14')
        #layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartoes',key='aceita_cartao'),sg.Radio('Não','cartoes',key='naoAceita_cartao')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,15),key='sliderVelocity')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,10),key='output')]
        ]
        #janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)


    def Iniciar(self):
        keys = ['nome','idade','gmail','outlook','yahoo']
        while True:

            #Extrair dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceita_cartao']
            Nao_aceita_cartao = self.values['naoAceita_cartao']
            sliderVelocity = self.values['sliderVelocity']

            self.janela['output'].update('')
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita_gmail: {aceita_gmail}')
            print(f'aceita_outlook: {aceita_outlook}')
            print(f'aceita_yahoo: {aceita_yahoo}')
            print(f'aceita_cartao: {aceita_cartao}')
            print(f'naoAceita_cartao: {Nao_aceita_cartao}')
            print(f'sliderVelocity: {sliderVelocity}')

            for key in keys:
                self.janela[key].update('')
            self.janela['aceita_cartao'].update(False)
            self.janela['naoAceita_cartao'].update(False)
            self.janela['sliderVelocity'].update(0)

tela = TelaPy()
tela.Iniciar()
