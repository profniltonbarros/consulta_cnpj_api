import customtkinter as ctk
import requests

# Configuração da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Consulta CNPJ")
app.geometry("500x400")

# Função de consulta
def consultar_cnpj():
    cnpj = entrada.get().strip()

    if not cnpj:
        resultado.configure(text="Digite um CNPJ válido")
        return

    try:
        url = f"https://api.opencnpj.org/{cnpj}"
        res = requests.get(url)
        dados = res.json()

        texto = (
            f"CNPJ: {dados.get('cnpj','')}\n"
            f"Razão Social: {dados.get('razao_social','')}\n"
            f"Nome Fantasia: {dados.get('nome_fantasia','')}\n"
            f"Situação: {dados.get('situacao_cadastral','')}"
        )

        resultado.configure(text=texto)

    except:
        resultado.configure(text="Erro ao consultar CNPJ")

# Título
titulo = ctk.CTkLabel(app, text="Consulta de CNPJ", font=("Arial", 20))
titulo.pack(pady=10)

# Entrada
entrada = ctk.CTkEntry(app, placeholder_text="Digite o CNPJ")
entrada.pack(pady=10)

# Botão
botao = ctk.CTkButton(app, text="Consultar", command=consultar_cnpj)
botao.pack(pady=10)

# Resultado
resultado = ctk.CTkLabel(app, text="", justify="left")
resultado.pack(pady=20)

# Executar
app.mainloop()