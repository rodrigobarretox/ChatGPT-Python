# ChatGPT-Python

Este projeto é uma interface gráfica simples que permite interagir com o ChatGPT usando a biblioteca Tkinter para Python. O programa permite que o usuário envie mensagens e receba respostas do modelo GPT-3.5-turbo da OpenAI.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Configuração da API](#configuração-da-api)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Autores](#autores)

## Instalação

1. Clone este repositório para sua máquina local:

    ```bash
    git clone https://github.com/rodrigobarretox/ChatGPT-Python.git
    cd ChatGPT-Python
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Antes de iniciar a aplicação, você precisa configurar sua chave de API da OpenAI. Veja a seção [Configuração da API](#configuração-da-api) para mais detalhes.

2. Execute o script principal:

    ```bash
    python chat.py
    ```

3. A interface gráfica será aberta, permitindo que você envie mensagens e receba respostas do ChatGPT.

## Configuração da API

1. Obtenha uma chave de API da OpenAI [aqui](https://beta.openai.com/signup/).

2. Substitua a string `'<SUA-CHAVE-AQUI>'` no código pela sua chave de API:

    ```python
    api_key = '<SUA-CHAVE-AQUI>'
    ```

## Contribuição

Contribuições são bem-vindas! Por favor, siga os passos abaixo para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch (`git checkout -b feature/AmazingFeature`).
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`).
4. Envie para a branch (`git push origin feature/AmazingFeature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autores

- **Rodrigo Barreto** - *Desenvolvedor* - [Perfil no GitHub](https://github.com/rodrigobarretox)

## Agradecimentos

- À OpenAI pela API incrível.
- À comunidade Python pelo suporte contínuo.
