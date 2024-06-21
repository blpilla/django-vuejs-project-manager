Gerenciador de Projetos - Backend
Este é o backend do projeto Gerenciador de Projetos, desenvolvido em Django, que fornece uma API RESTful para gerenciamento de clientes, projetos e atividades. A autenticação é baseada em JWT (JSON Web Tokens).

Requisitos
Python 3.8+
Django 3.2+
PostgreSQL
Configuração do Ambiente

Clone o repositório.

Crie e ative um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
Instale as dependências:

bash
pip install -r requirements.txt
Configure o banco de dados:

Atualize as configurações do banco de dados no arquivo settings.py com suas credenciais do PostgreSQL:

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'seu_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '',
    }
}

Execute as migrações:

bash
python manage.py makemigrations
python manage.py migrate
Crie um superusuário:

bash
python manage.py createsuperuser
Inicie o servidor de desenvolvimento:

bash
python manage.py runserver
API Endpoints
Os principais endpoints da API são:

Clientes

GET /api/clientes/: Lista todos os clientes.
POST /api/clientes/: Cria um novo cliente.
PUT /api/clientes/{id}/: Atualiza um cliente existente.
DELETE /api/clientes/{id}/: Deleta um cliente.
Projetos

GET /api/projetos/: Lista todos os projetos.
POST /api/projetos/: Cria um novo projeto.
PUT /api/projetos/{id}/: Atualiza um projeto existente.
DELETE /api/projetos/{id}/: Deleta um projeto.
Atividades

GET /api/atividades/: Lista todas as atividades.
POST /api/atividades/: Cria uma nova atividade.
PUT /api/atividades/{id}/: Atualiza uma atividade existente.
DELETE /api/atividades/{id}/: Deleta uma atividade.
Autenticação

POST /api/token/: Obtém um token de acesso JWT.
Testes
Para rodar os testes unitários, utilize o comando:

bash
python manage.py test
A cobertura de testes deve ser de, no mínimo, 80%. Para verificar a cobertura de testes, você pode utilizar a ferramenta coverage:

bash
pip install coverage
coverage run manage.py test
coverage report

