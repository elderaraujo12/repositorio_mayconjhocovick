from curses import window
import PySimpleGUI as sg 
sg.theme('Dark Blue 3')
Layout = [
    [sg.Text('Usuário')],
    [sg.Input(key= 'Usuário')],
    [sg.Text('Senha')],
    [sg.Input(key='Senha')],
    [sg.Button('Login')],
    [sg.Text('',key='mensagem')],
    [sg.Button('Criar novo login')],
]

window = sg.Window('Login', layout=Layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        Senha_correta = '123456'
        Usuario_correto = 'maycon'
        Usuario = values['Usuário']
        Senha = values['Senha']
        if Senha == Senha_correta and Usuario == Usuario_correto:
            window['mensagem'].update('LOGIN FEITO COM SUCESSO')
        else:
            window['mensagem'].update('SENHA OU USUÁRIO INCORRETO')
            
            
        
        