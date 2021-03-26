# Livro de Receitas

Aplicação web desenvolvida em Flask para cadastro e visualização de receitas

[Link para vídeo explicativo do sistema](https://youtu.be/721S-R5WNMc)

## Instalação

Primeiramente faça a clonagem do repositório e em seguida entre no diretório:

```bash
git clone https://github.com/isabellefo/livro-receitas.git
cd livro-receitas
```

Dentro da pasta do projeto, crie e inicialize um ambiente virtual:

```bash
virtualenv venv
```

Inicialização em ambiente ***Windows***:
```bash
venv/Script/activate
```

Inicialização em ambiente ***Linux***:
```bash
source venv/bin/activate
```

Por fim, instale as dependências do projeto:

```
pip install -r requirements.txt
```

## Execução

```bash
cd livro-receitas
python run.py
```

Outra forma de realizar a execução

```
cd livro-receitas
waitress-serve --listen=127.0.0.1:5000
```

A aplicação roda no ip 127.0.0.1 e na porta 5000
