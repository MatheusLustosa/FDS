# Contribuindo para o Projeto AlphaTech University <img src="https://github.com/user-attachments/assets/927439f6-8b7f-4532-aee0-90f9a1c79256" alt="alphafundo" width="50" style="float:left; margin-right:10px;">

Este guia foi criado para novos colaboradores do projeto SmartSchool, detalhando o processo de configuração do ambiente, ferramentas necessárias e o fluxo de trabalho recomendado para garantir uma colaboração eficiente e organizada.

## Índice
1. [Pré-requisitos](#pré-requisitos)
2. [Criando sua conta no GitHub](#criando-sua-conta-no-github)
3. [Clonando o Repositório](#clonando-o-repositório)
4. [Configuração Inicial do Ambiente](#configuração-inicial-do-ambiente)
5. [Fluxo de Trabalho no Git](#fluxo-de-trabalho-no-git)
6. [Solicitando Permissão para Commitar](#solicitando-permissão-para-commitar)
7. [Ferramentas Externas Necessárias](#ferramentas-externas-necessárias)
8. [Solicitação de Merge da Branch Prod para a Main](#solicitação-de-merge-da-branch-prod-para-a-main)
9. [Acessando a Aplicação na Azure](#acessando-a-aplicação-na-azure)

## Pré-requisitos
Antes de começar, certifique-se de ter o seguinte instalado na sua máquina:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [VScode](https://code.visualstudio.com/download)

---
## Criando sua conta no GitHub
O primeiro passo é criar uma conta no GitHub seguindo as instruções abaixo:

- [Guia de Criação de Conta no GitHub](https://docs.github.com/pt/get-started/start-your-journey/creating-an-account-on-github)

---

## Clonando o Repositório
Abra o terminal do Git Bash e siga os passos abaixo:

1. Navegue até o diretório onde você deseja clonar o repositório:
    ```bash
    cd /c/Users/SeuUsuario/SeuDiretorio
    ```
2. Clone o repositório:
    ```bash
    git clone https://github.com/MatheusLustosa/FDS.git
    ```

---

## Configuração Inicial do Ambiente
Após acessar o código, configure seu ambiente seguindo as etapas abaixo:

1. **Habilitando execução de scripts no PowerShell do Windows:**
    ```bash
    Set-ExecutionPolicy -Scope CurrentUser Unrestricted
    ```
2. **Criando um ambiente virtual:**
    ```bash
    py -m venv venv
    ```
3. **Ativando o ambiente virtual:**
    ```bash
    venv\Scripts\activate.bat
    ```
4. **Instalando os pacotes do `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Criando arquivos de migração para o banco de dados:**
    ```bash
    python manage.py makemigrations usuarios
    ```
6. **Aplicando as migrações ao banco de dados:**
    ```bash
    python manage.py migrate
    ```
7. **Executando o site localmente:**
   - Acesse a URL [http://127.0.0.1:8000/](http://127.0.0.1:8000/) e inicie o servidor com:
    ```bash
    python manage.py runserver
    ```

---

## Fluxo de Trabalho no Git
Para manter seu repositório atualizado e enviar mudanças, utilize os comandos abaixo:

1. **Verificar o status do repositório:**
    ```bash
    git status
    ```
2. **Adicionar arquivos modificados:**
    ```bash
    git add .
    ```
3. **Fazer o commit das mudanças:**
    ```bash
    git commit -m "seu comentário"
    ```
4. **Enviar as mudanças para o repositório remoto:**
    ```bash
    git push
    ```
5. **Receber atualizações do repositório remoto:**
    ```bash
    git pull
    ```

---

## Solicitando Permissão para Commitar
Caso você não tenha sido adicionado como colaborador, siga estes passos:

1. **Solicitar acesso:**
   Abra uma issue no repositório solicitando permissão para ser colaborador. Descreva seu interesse e as áreas específicas em que deseja ajudar.
2. **Aguardar aprovação:**
   Um mantenedor revisará sua solicitação e, se aprovado, adicionará você como colaborador.
3. **Confirmar colaboração:**
   Após ser adicionado, você receberá uma notificação por e-mail. Confirme e siga os passos para envio de atualizações descritos acima.

---

## Ferramentas Externas Necessárias
Certifique-se de criar contas e acessar as seguintes ferramentas:

- **Projeto no Jira:** [AlphaTech University no Jira](https://cesar-team-c925b8yd.atlassian.net/jira/software/projects/AE/boards/5?atlOrigin=eyJpIjoiOGQyNjQxNmVlNzYxNDUzNmEwMDA5Y2Y4YTZiMmVkMmEiLCJwIjoiaiJ9)
- **Protótipo de Lo-Fi no Figma:** [Protótipo AlphaTech University no Figma](https://www.figma.com/design/7uEuFDZ5T9I2HeTYMGfnR9/FDS-Entrega-1?node-id=0-1&t=nimLCI6xdHeemn50-1)

---

## Solicitação de Merge da Branch Prod para a Main
Para solicitar um merge da branch `prod` (hospedada na Azure) para a branch `main`, siga estes passos:

1. **Certifique-se de que está na branch `prod`:**
    ```bash
    git checkout prod
    ```
2. **Atualize a branch `prod`:**
    ```bash
    git pull origin prod
    ```
3. **Crie um pull request:**
   - Abra um pull request no GitHub solicitando o merge de `prod` para `main`, com uma descrição detalhada das mudanças.
4. **Aguarde a revisão e aprovação:**
   Notifique os mantenedores para que revisem o pull request.
5. **Merge aprovado:**
   Um mantenedor fará o merge das mudanças na branch `main`.

---

## Acessando a Aplicação na Azure
Para acessar a aplicação web do AlphaTech University, use o link abaixo. Antes de contribuir, verifique as issues abertas e comente em qualquer issue na qual você tenha interesse em trabalhar:

- [Acessar Projeto AlphaTech University na Azure](https://alphatech-btdjdsgcg6dff6f4.brazilsouth-01.azurewebsites.net/)

*Observação: Ao acessar a aplicação, consulte as diretrizes de contribuição para garantir a consistência e qualidade do projeto.*

---

Seguindo esses passos, você garantirá uma colaboração organizada e eficiente com o projeto AlphaTech University!
