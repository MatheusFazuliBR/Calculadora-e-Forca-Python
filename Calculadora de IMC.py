#Calculadora IMC utilizando TKinter em Python

import tkinter as tk

class CalculadoraIMC:
    def __init__(self, master):
        self.master = master
        master.title('Calculadora de IMC')

        self.label_peso = tk.Label(master, text='Peso (kg):')
        self.label_peso.pack()

        self.entrada_peso = tk.Entry(master)
        self.entrada_peso.pack()

        self.label_altura = tk.Label(master, text='Altura (m):')
        self.label_altura.pack()

        self.entrada_altura = tk.Entry(master)
        self.entrada_altura.pack()

        self.botao_calcular = tk.Button(master, text='Calcular IMC', command=self.calcular_imc)
        self.botao_calcular.pack()

        self.resultado = tk.Label(master, text='')
        self.resultado.pack()

    def calcular_imc(self):
        peso = float(self.entrada_peso.get())
        altura = float(self.entrada_altura.get())

        imc = peso / (altura ** 2)

        self.resultado.config(text=f'Seu IMC é: {imc:.2f}')

root = tk.Tk()
app = CalculadoraIMC(root)

root.mainloop()
