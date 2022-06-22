from ast import Break
from PySimpleGUI import PySimpleGUI as sg 
sg.theme('Dark Blue 3')
layout = [
[sg.Text('Usuário'), sg.Input(key='usuário', size=(20,4))],
[sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,4))],
[sg.Checkbox('salvar o login?')],
[sg.Button('Criar uma conta')],
[sg.Button('ENTRAR')]
]

#JANELA
janela = sg.Window('tela de login', layout)
#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'ENTRAR':
        if valores['usuario'] == 'maycon' and valores['senha'] == '123456':
            break
            print('BEM VINDO AO LOVE PET') 
while True:
    eventos, valores == janela.read()
    if eventos == sg.WINDOW_CLOSED:
        Break
    if eventos == 'Criar uma conta':
        if valores['Usuário'] == 'lindo' and valores['senha'] == 'lindinho12':
            break
            print('Seja bem-vindo')
            
                   



