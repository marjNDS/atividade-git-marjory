import tkinter as tk
from tkinter import filedialog, messagebox

def novo_arquivo():
    text_area.delete(1.0, tk.END)

def abrir_arquivo():
    caminho = filedialog.askopenfilename(defaultextension=".txt",
                                         filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])
    if caminho:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, conteudo)

def salvar_arquivo():
    caminho = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])
    if caminho:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            conteudo = text_area.get(1.0, tk.END)
            arquivo.write(conteudo)
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")

# Janela principal
janela = tk.Tk()
janela.title("Bloco de Notas Simples")
janela.geometry("600x400")

# Área de texto
text_area = tk.Text(janela, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

# Menu
menu_bar = tk.Menu(janela)
arquivo_menu = tk.Menu(menu_bar, tearoff=0)
arquivo_menu.add_command(label="Novo", command=novo_arquivo)
arquivo_menu.add_command(label="Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=janela.quit)

menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
janela.config(menu=menu_bar)

# Inicia a aplicação
janela.mainloop()
