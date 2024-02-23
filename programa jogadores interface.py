import tkinter as tk
from tkinter import messagebox

def calcular_media_gols(gols, partidas):
    total = sum(gols)
    media = total / partidas
    return media

def cadastrar_jogador():
    nome_jogador = nome_entry.get()
    num_jogos = int(partidas_entry.get())
    
    gols_jogador = []
    for j in range(num_jogos):
        gols = int(gols_entries[j].get())
        gols_jogador.append(gols)
    
    media_gols = calcular_media_gols(gols_jogador, num_jogos)
    jogadores[nome_jogador] = {
        'partidas': num_jogos,
        'gols': gols_jogador,
        'média-gols/partida': media_gols
    }
    
    messagebox.showinfo("Cadastro Concluído", f"Jogador {nome_jogador} cadastrado com sucesso!")

def exibir_relatorio():
    relatorio_text.delete(1.0, tk.END)
    for jogador, info in jogadores.items():
        relatorio_text.insert(tk.END, f'Jogador: {jogador}\n')
        relatorio_text.insert(tk.END, f'Partidas: {info["partidas"]}\n')
        relatorio_text.insert(tk.END, f'Gols: {info["gols"]}\n')
        relatorio_text.insert(tk.END, f'Média de gols por Partida: {info["média-gols/partida"]:.2f}\n')
        relatorio_text.insert(tk.END, '-' * 20 + '\n')

jogadores = {}

root = tk.Tk()
root.title("Cadastro de Jogadores e Média de Gols")

nome_label = tk.Label(root, text="Nome do Jogador:")
nome_label.pack()

nome_entry = tk.Entry(root)
nome_entry.pack()

partidas_label = tk.Label(root, text="Número de Partidas:")
partidas_label.pack()

partidas_entry = tk.Entry(root)
partidas_entry.pack()

gols_entries = []
for i in range(10):
    gols_label = tk.Label(root, text=f"Gols na Partida {i+1}:")
    gols_label.pack()
    gols_entry = tk.Entry(root)
    gols_entry.pack()
    gols_entries.append(gols_entry)

cadastrar_button = tk.Button(root, text="Cadastrar Jogador", command=cadastrar_jogador)
cadastrar_button.pack()

relatorio_button = tk.Button(root, text="Exibir Relatório", command=exibir_relatorio)
relatorio_button.pack()

relatorio_text = tk.Text(root)
relatorio_text.pack()

root.mainloop()
