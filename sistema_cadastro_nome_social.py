import PySimpleGUI as sg

sg.theme = 'DarkPurple3'

layout1 = [
    [sg.Text('Sistema de Cadastro para Pessoas Trans', key='Sistema de cadsatro para Pessoas Trans')],
    [sg.Text('_____________________________________________________________________________________')],
    [sg.Text('Digite seu nome completo: ', key='Digite seu nome completo: ')],
    [sg.InputText('')],
    [sg.Text('')],
    [sg.Text('Digite sua data de nascimento: ', key='Digite sua data de nascimento: ')],
    [sg.InputText('')],
    [sg.Text('Digite seu apelido/nome social: ', key='Digite seu apelido/nome social: ')],
    [sg.InputText('')],
    [sg.Text('Digite o nome da sua mãe: ', key='Digite o nome da sua mãe: ')],
    [sg.InputText('')],
    [sg.Text('Digite o nome do seu pai: ', key='Digite o nome do seu pai: ')],
    [sg.InputText('')],
    [sg.Text('')],
    [sg.Button('Cadastrar')],
    [sg.Text('')],
    [sg.Button('Cancelar')]
]

layout1 = sg.Window('Sistema de Cadastro - Nome Social para Pessoas LGBTQIA+', layout1, size=(600,500), element_justification = 'center')

button, values = layout1.Read()

if button == 'Cadastrar':
      layout1.close()

if button == 'Cancelar':
    exit()

layout2 = [
    [sg.Text('Cadastro efeutuado com sucesso!!!')],
    [sg.Button('Fechar')]
]

layout2 = sg.Window('Confirmação de Cadastro', layout2, size=(250,100), element_justification='center')

button, values == layout2.Read()

if button == 'Fechar':
   exit()
