# Fórum

Como Django é uma aplicação do python, você precisa dele instalado na sua máquina.
https://www.python.org/downloads/

# Instalando Django
Digitar o seguinte comando para a instalação do framework, assim ele ja pega a última versão do framework:
    pip install django

Após isso, iniciamos o projeto no qual iremos trabalhar, com o comando:

    django-admin startproject Fórum .


Em seguida, iniciamos o nosso app com o comando:

    django-admin startapp Core


Para começar a rodar e fazer os teste online, damos o seguinte comando:

  python manage.py runserver


Utilizo também o comando frezze, pra congelar a aplicação com os dados que já foram instalados e utilizados, e coloco ele em um arquivo txt que vai ser gerado, que no meu caso vai se chamar requirements.txt:

    pip frezze > requirements.txt


E o seguinte comando para ler esse arquivo e instalar as dependências dele:

    pip install -r requirements.txt


# Bando de dados
Sqlite3
