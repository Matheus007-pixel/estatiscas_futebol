#  Estatísticas de Futebol — Flask App

Aplicação web desenvolvida em **Python + Flask** para gerenciamento e visualização de estatísticas de times de futebol.

O projeto consome uma **API externa de futebol**, implementa **cache de dados**, **Dark Mode persistente** e possui uma interface moderna utilizando **Bootstrap** e **Font Awesome**.

---

##  Funcionalidades

-  Cadastro, edição e exclusão de times
-  Busca automática de escudos via API externa
-  Cache de escudos no banco de dados (SQLite)
-  Dark Mode persistente (localStorage)
-  Visualização de estatísticas por time
-  Interface moderna e responsiva
- Uso de variáveis de ambiente para segurança da API

---

## Tecnologias Utilizadas

- Python
- Flask
- SQLite
- HTML5 / CSS3
- Bootstrap 5
- Font Awesome
- JavaScript
- API-Football
- Gunicorn

---

## Estrutura do Projeto

```text
estatisticas-futebol-flask/
├── app.py
├── services/
│   ├── football_api.py
│   └── escudo_service.py
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── time.html
│   ├── cadastrar.html
│   └── editar.html
├── requirements.txt
├── README.md
└── database.db
