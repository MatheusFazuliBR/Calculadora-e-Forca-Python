#Lista de Tarefas utilizando TKinter em Python

import tkinter as tk

class ListaDeTarefas:
    def __init__(self, master):
        self.master = master
        master.title('Lista de Tarefas')

        self.tarefas = []

        self.frame_tarefas = tk.Frame(master)
        self.frame_tarefas.pack()

        self.texto_tarefa = tk.Entry(self.frame_tarefas)
        self.texto_tarefa.pack(side=tk.LEFT)

        self.botao_adicionar = tk.Button(self.frame_tarefas, text='Adicionar Tarefa', command=self.adicionar_tarefa)
        self.botao_adicionar.pack(side=tk.RIGHT)

        self.lista_tarefas = tk.Listbox(master)
        self.lista_tarefas.pack()

        self.botao_remover = tk.Button(master, text='Remover Tarefa Selecionada', command=self.remover_tarefa)
        self.botao_remover.pack()

    def adicionar_tarefa(self):
        tarefa = self.texto_tarefa.get()
        if tarefa:
            self.tarefas.append(tarefa)
            self.lista_tarefas.insert(tk.END, tarefa)
            self.texto_tarefa.delete(0, tk.END)

    def remover_tarefa(self):
        indice_selecionado = self.lista_tarefas.curselection()
        if indice_selecionado:
            indice = indice_selecionado[0]
            tarefa_removida = self.tarefas.pop(indice)
            self.lista_tarefas.delete(indice)

root = tk.Tk()
app = ListaDeTarefas(root)

root.mainloop()
