from cProfile import label
from importlib.metadata import entry_points
import tkinter as tk
from tkinter import NSEW, Entry, Grid, ttk
import datetime as dt
from typing import Text
from pandas import describe_option #pegar o horio da criacao
lista_tipos = ['maycon','Inacio', 'Diego']
lista2 = ['99988120574']
lista3 = ['5','6','7','10...']
lista_idade = ['18, ......']
lista_cep = ['CEP']
lista_codigo = ['0010','0015','0021']

janela = tk.Tk()
#criacao da funcao

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = Combobox_selecionar_tipo.get()
    raca = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d / %m / %y / %H:%m ")
    codigo = len(lista_codigo)+1
    codigo_str = 'COD-{}'.format(codigo)
    lista_codigo.append((codigo_str, lista_tipos ,entry_quant, data_criacao,lista_codigo))

#titulo da janela 

janela.title('SEU CADASTRO')

label_descricao = tk.Label(text='Uma descricao sobre voce')
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4 )

label_tipo_unidade = tk.Label(text='Nome')
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2  )

Combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
Combobox_selecionar_tipo.grid(row=3, column=2,padx=10, pady=10, sticky='nswe', columnspan=2)


lebel_lista_codigo = tk.Label(text='código de login')
lebel_lista_codigo.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

Combobox_selecionar_tipo = ttk.Combobox(values=lista_codigo)
Combobox_selecionar_tipo.grid(row=4, column=2,padx=10, pady=10, sticky='nswe', columnspan=2)


entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

Combobox_selecionar_tipo = ttk.Combobox(values=lista2)
Combobox_selecionar_tipo.grid(row=5, column=2,padx=10, pady=10, sticky='nswe', columnspan=2)

label_tipo_unidade = tk.Label(text='Numero tell')
label_tipo_unidade.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2  )

Combobox_selecionar_tipo = ttk.Combobox(values=lista_idade)
Combobox_selecionar_tipo.grid(row=6, column=2,padx=10, pady=10, sticky='nswe', columnspan=2)

label_tipo_unidade = tk.Label(text='Qual a sua idade?')
label_tipo_unidade.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=2  )

Combobox_selecionar_tipo = ttk.Combobox(values=lista_cep)
Combobox_selecionar_tipo.grid(row=7, column=2,padx=10, pady=10, sticky='nswe', columnspan=2)

label_tipo_unidade = tk.Label(text='CEP')
label_tipo_unidade.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=2  )


botao_criar_codigo = tk.Button(text='salvar', command=inserir_codigo())
botao_criar_codigo.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()

print(lista_codigo)
print('SEJA BEM-VINDO AO LOVE PET')
