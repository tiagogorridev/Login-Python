import tkinter as tk
from tkinter import messagebox

def criar_conta(email, senha):
    # Simplesmente adiciona o novo login ao arquivo
    with open("dados_login.txt", "a") as file:
        file.write(f"{email}:{senha}\n")

def verificar_login(email, senha):
    # Lê os logins do arquivo
    with open("dados_login.txt", "r") as file:
        linhas = file.readlines()

    for linha in linhas:
        login, senha_armazenada = linha.strip().split(":")
        if email == login and senha == senha_armazenada:
            return True

    return False

def criar_conta_click():
    email = entry_email.get()
    senha = entry_senha.get()

    if email and senha:
        criar_conta(email, senha)
        messagebox.showinfo("Conta Criada", "Conta criada com sucesso!")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

def login_click():
    email = entry_email.get()
    senha = entry_senha.get()

    if email and senha:
        if verificar_login(email, senha):
            messagebox.showinfo("Login Bem-sucedido", "Login bem-sucedido!")
        else:
            messagebox.showwarning("Erro de Login", "Credenciais incorretas.")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Interface gráfica
root = tk.Tk()
root.title("Sistema de Login")

label_email = tk.Label(root, text="E-mail:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()

entry_senha = tk.Entry(root, show="*")  # A senha é oculta
entry_senha.pack()

button_criar_conta = tk.Button(root, text="Criar Conta", command=criar_conta_click)
button_criar_conta.pack()

button_login = tk.Button(root, text="Login", command=login_click)
button_login.pack()

root.mainloop()
