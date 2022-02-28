import PySimpleGUI as sg

sg.theme = 'BluePurple'

janela1 = [
    [sg.InputText('Digite o código da mercadoria: ')],
    [sg.InputText('Digite o preço da mercadoria: ')],
    [sg.Button('Calcular')],
    [sg.Button('Cancelar Operação')]
]

janela1 = sg.Window('Mini PDV', janela1, size=(400,300), element_justification='center')

button, values = janela1.Read()

if button == 'Cancelar Operação':
      exit()

janela2 = [
    [sg.Text('Escolha sua forma de pagamento: ')],
    [sg.Checkbox('Dinheiro (à vista)')],
    [sg.Checkbox('Débito')],
    [sg.Checkbox('Crédito')],
    [sg.Button('')],
    [sg.Button('Pagar')],
    [sg.Button('Cancelar Operação')]
]

janela2 = sg.Window('Mini PDV - Forma de Pagamento', janela2, size=(400,300), element_justification='center')

button, values == janela2.Read()

if button == 'Cancelar Operação':
    exit()