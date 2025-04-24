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

def copiar_texto():
    text_area.event_generate("<<Copy>>")

def colar_texto():
    text_area.event_generate("<<Paste>>")

def cortar_texto():
    text_area.event_generate("<<Cut>>")

def exibir_menu_contexto(evento):
    menu_contexto.tk_popup(evento.x_root, evento.y_root)

# Janela principal
janela = tk.Tk()
janela.title("Bloco de Notas Simples")
janela.geometry("600x400")

# Área de texto
text_area = tk.Text(janela, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

# Menu superior
menu_bar = tk.Menu(janela)

# Menu Arquivo
arquivo_menu = tk.Menu(menu_bar, tearoff=0)
arquivo_menu.add_command(label="Novo", command=novo_arquivo)
arquivo_menu.add_command(label="Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=janela.quit)
menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)

# Menu Editar
editar_menu = tk.Menu(menu_bar, tearoff=0)
editar_menu.add_command(label="Copiar", command=copiar_texto)
editar_menu.add_command(label="Colar", command=colar_texto)
editar_menu.add_command(label="Cortar", command=cortar_texto)
menu_bar.add_cascade(label="Editar", menu=editar_menu)

# Aplica o menu à janela
janela.config(menu=menu_bar)

# Menu de contexto (botão direito)
menu_contexto = tk.Menu(janela, tearoff=0)
menu_contexto.add_command(label="Copiar", command=copiar_texto)
menu_contexto.add_command(label="Colar", command=colar_texto)
menu_contexto.add_command(label="Cortar", command=cortar_texto)

# Vincula o clique direito na área de texto
text_area.bind("<Button-3>", exibir_menu_contexto)

# Inicia a aplicação
janela.mainloop()
