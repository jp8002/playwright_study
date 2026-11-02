# Suíte de Testes Usando Playwright

## Introdução
Este repositório contém o código com a suíte de testes usando Playwright, tendo como aplicação testada o OWASP Juice Shop.

## Passo a Passo

Para executar a suíte de testes corretamente, siga os passos a seguir.

### 1. Instalar o Docker
Como o OWASP Juice Shop é executado via contêiner, é necessária a presença do Docker na máquina.
Para realizar a instalação, consulte a documentação oficial:

[Get Docker](https://docs.docker.com/get-started/get-docker)

### 2. Baixar a imagem do Juice Shop
Com o Docker instalado, baixe a imagem do OWASP Juice Shop:

```bash
docker pull bkimminich/juice-shop
```

### 3. Rodar a imagem do Juice Shop

Com a imagem baixada, rode um novo contêiner espelhando a porta 3000 da máquina local com a porta 3000 do contêiner:

```bash
docker run -d -p 3000:3000 bkimminich/juice-shop
```

### 4. Criar o ambiente virtual

Acesse a raiz do projeto e crie um ambiente virtual usando o módulo venv do Python:
```bash
python -m venv playVenv
```

### 5. Ativar o ambiente virtual

Com o ambiente virtual criado, ative-o executando o comando correspondente ao seu sistema operacional.

#### No Linux / macOS
``` bash
source playVenv/bin/activate
```

#### No Windows
```
playVenv\Scripts\activate
```

### 6. Instalar as bibliotecas necessárias

Usando o gerenciador de pacotes do Python (pip), instale as dependências e os navegadores do Playwright:
```bash
pip install -r requirements.txt
playwright install
```

### 7. Rodar a suíte de testes

Com o ambiente configurado e o Juice Shop em execução, rode os testes:
```bash
pytest
```

### 8. Rodar a suíte de testes gerando relatório em html (Opcional)
Usando a biblioteca pytest-html, é possível gerar um relatório em html ao final dos testes:
```bash
pytest --html=report.html --self-contained-html
```

### 9. Rodar a suíte de testes em dois navegadores, gerando relatório em html (Opcional)
```bash
 pytest --browser chromium --browser firefox
```