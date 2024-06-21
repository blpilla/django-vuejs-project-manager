Gerenciador de Projetos - Frontend
Este é o frontend do projeto Gerenciador de Projetos, desenvolvido em Vue.js, que consome a API RESTful fornecida pelo backend Django. A autenticação é baseada em JWT (JSON Web Tokens).

Requisitos
Node.js 14.x ou superior
npm 6.x ou superior
Configuração do Ambiente
Clone o repositório:

bash
git clone https://github.com/seu-usuario/gerenciador-de-projetos.git
cd gerenciador-de-projetos/frontend
Instale as dependências:

bash
npm install
Inicie o servidor de desenvolvimento:

bash
npm run serve
O aplicativo estará disponível em http://localhost:8080.

Componentes
Login.vue: Tela de login do usuário.
Clientes.vue: Tela de gerenciamento de clientes.
Projetos.vue: Tela de gerenciamento de projetos.
Atividades.vue: Tela de gerenciamento de atividades.
App.vue: Componente principal da aplicação.
api/index.js: Configuração do axios para chamadas à API.
router/index.js: Configuração das rotas da aplicação.


API Endpoints
O frontend consome os seguintes endpoints da API:

Clientes

GET /api/clientes/
POST /api/clientes/
PUT /api/clientes/{id}/
DELETE /api/clientes/{id}/
Projetos

GET /api/projetos/
POST /api/projetos/
PUT /api/projetos/{id}/
DELETE /api/projetos/{id}/
Atividades

GET /api/atividades/
POST /api/atividades/
PUT /api/atividades/{id}/
DELETE /api/atividades/{id}/
Autenticação

POST /api/token/
Autenticação
A autenticação é realizada através de JWT. O token é armazenado no localStorage e incluído nas requisições feitas pelo axios.

Para rodar os testes, use o comando:

bash
npm run test
