import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests 

# Chave de API do OpenAI (substitua pela sua chave sem <>)
api_key = '<SUA-CHAVE-AQUI>'

# Função para enviar a mensagem e obter a resposta do ChatGPT
def send_message():
    message = input_text.get("1.0", tk.END).strip()  # Obtém o texto do input
    input_text.delete("1.0", tk.END)  # Limpa o campo de input

    if message:
        add_message_to_chat("Você", message)  # Adiciona a mensagem enviada ao chat

        # Chamada à API do ChatGPT
        response = call_openai_chatgpt(message)
        if response is not None:
            add_message_to_chat("ChatGPT", response)  # Adiciona a resposta ao chat
        else:
            messagebox.showerror("Erro", "Não foi possível obter resposta do ChatGPT.")

# Função para fazer a chamada à API do ChatGPT
def call_openai_chatgpt(message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching response from ChatGPT: {e}")
        return None

# Função para adicionar mensagens ao chat
def add_message_to_chat(sender, message):
    chat_text.config(state=tk.NORMAL)  # Habilita a edição do campo de texto
    chat_text.insert(tk.END, f"{sender}: {message}\n\n")  # Adiciona a mensagem
    chat_text.config(state=tk.DISABLED)  # Desabilita a edição do campo de texto
    chat_text.see(tk.END)  # Move a barra de rolagem para o final

# Função principal para criar a interface gráfica
def main():
    root = tk.Tk()
    root.title("ChatGPT")

    # Área de exibição do chat
    global chat_text
    chat_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
    chat_text.pack(padx=10, pady=10)

    # Campo de entrada de texto
    global input_text
    input_text = tk.Text(root, wrap=tk.WORD, width=50, height=3)
    input_text.pack(padx=10, pady=10)

    # Botão de enviar
    send_button = tk.Button(root, text="Enviar", command=send_message)
    send_button.pack(padx=10, pady=10)

    # Iniciar o loop principal da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()


