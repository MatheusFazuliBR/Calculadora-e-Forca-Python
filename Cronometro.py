#Cronometro utilizando TKinter em Python

import tkinter as tk
from datetime import datetime

class CronometroDigital:
    def __init__(self, master):
        self.master = master
        master.title('Cronômetro Digital')

        self.iniciado = False
        self.tempo_inicial = datetime.now()
        self.tempo_atual = self.tempo_inicial

        self.display = tk.Label(master, text="00:00:00", font=("Helvetica", 48), bg="black", fg="white")
        self.display.pack()

        self.botao_iniciar = tk.Button(master, text='Iniciar', command=self.iniciar)
        self.botao_iniciar.pack(side=tk.LEFT)

        self.botao_parar = tk.Button(master, text='Parar', command=self.parar, state=tk.DISABLED)
        self.botao_parar.pack(side=tk.LEFT)

        self.botao_resetar = tk.Button(master, text='Resetar', command=self.resetar, state=tk.DISABLED)
        self.botao_resetar.pack(side=tk.LEFT)

        self.atualizar_tempo()

    def iniciar(self):
        if not self.iniciado:
            self.iniciado = True
            self.tempo_inicial = datetime.now() - (self.tempo_atual - self.tempo_inicial)
            self.botao_iniciar.config(text='Pausar')
            self.botao_parar.config(state=tk.NORMAL)
            self.botao_resetar.config(state=tk.NORMAL)
            self.atualizar_tempo()

    def parar(self):
        if self.iniciado:
            self.iniciado = False
            self.tempo_atual = datetime.now()
            self.botao_iniciar.config(text='Continuar')
            self.botao_parar.config(state=tk.DISABLED)

    def resetar(self):
        self.iniciado = False
        self.tempo_inicial = datetime.now()
        self.tempo_atual = self.tempo_inicial
        self.display.config(text="00:00:00")
        self.botao_iniciar.config(text='Iniciar')
        self.botao_parar.config(state=tk.DISABLED)
        self.botao_resetar.config(state=tk.DISABLED)

    def atualizar_tempo(self):
        if self.iniciado:
            self.tempo_atual = datetime.now()
            tempo_decorrido = self.tempo_atual - self.tempo_inicial
            horas, resto = divmod(tempo_decorrido.seconds, 3600)
            minutos, segundos = divmod(resto, 60)
            self.display.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
            self.master.after(1000, self.atualizar_tempo)

root = tk.Tk()
cronometro = CronometroDigital(root)

root.mainloop()
