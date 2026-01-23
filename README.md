#  Estatísticas de Futebol — Projeto Flask

Aplicação web desenvolvida em **Flask + SQLite** para cadastro e visualização de times de futebol, criada com foco em **portfólio profissional**.

O projeto permite que o usuário cadastre clubes, adicione estatísticas básicas e faça upload do escudo do time diretamente pelo sistema, sem dependência de APIs externas.

---

##  Objetivo do Projeto

- Criar uma aplicação estável e previsível
- Evitar dependência de APIs externas instáveis
- Demonstrar boas práticas com Flask
- Simular um sistema real de cadastro de clientes/clubes

---

##  Funcionalidades

- Cadastro de times
- Edição e exclusão
- Upload de escudo (imagem PNG/JPG)
- Validação de tamanho da imagem (até 2MB)
- Página individual para cada time
- Interface responsiva com Bootstrap
- Dark Mode persistente

---

##  Decisões Técnicas

- APIs externas removidas (ex: API-Football)
- Upload local de imagens feito pelo usuário
- Escudo salvo no servidor e referenciado no banco
- Banco SQLite para simplicidade 
- Arquivos sensíveis ignorados via `.gitignore`

> *“Optei por não utilizar APIs externas para evitar instabilidade e garantir que o projeto funcione de forma previsível em produção.”*

---

##  Estrutura do Projeto

estatiscas_futebol/
│
├── app.py
├── requirements.txt
├── services/
│ └── escudos.py
│
├── static/
│ ├── escudos/
│ │ └── default.png
│ └── uploads/
│
├── templates/
│ ├── index.html
│ ├── cadastrar.html
│ ├── editar.html
│ └── time.html
│
└── database.db (ignorado no Git)


---

##  Banco de Dados

Tabela `times`:

- `id`
- `nome`
- `jogos`
- `gols`
- `escudo`


---

##  Upload de Escudos

- Formatos permitidos: PNG, JPG, JPEG
- Tamanho máximo: 2MB
- Imagens são salvas localmente
- Caso não seja enviado, usa imagem padrão

---

## Como Executar Localmente

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd estatiscas_futebol
pip install -r requirements.txt
python app.py
