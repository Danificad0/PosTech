# 📊 VitiBrasil API — Tech Challenge FIAP

API desenvolvida para consulta de dados públicos sobre vitivinicultura no Brasil, disponibilizados pela Embrapa. O projeto realiza extração dos dados diretamente das tabelas disponíveis no site da Embrapa, sem dependência de banco de dados.

---

## 🚀 Funcionalidade

- API com scraping em tempo real dos dados das abas:
  - Produção
  - Processamento
  - Comercialização
  - Importação
  - Exportação
- Retorna os dados em JSON estruturado.
- Documentação automática via Swagger.

---

## 🏗️ Estrutura do Projeto

Postech/
│
├── app/
│ ├── api/ # Endpoints da API
│ ├── core/ # Configurações gerais
│ ├── db/ # (Futuro) Conexão com banco de dados
│ ├── models/ # (Futuro) Modelos de dados
│ ├── schemas/ # Schemas de validação (Pydantic)
│ ├── services/ # Scraper dos dados
│ └── main.py # Inicialização da API
│
├── requirements.txt # Dependências
├── README.md # Documentação
└── .env # Variáveis de ambiente

yaml
Copiar
Editar

---

## 🗺️ Arquitetura do Projeto

![Arquitetura do Projeto](./A_flowchart-style_digital_diagram_illustrates_the_.png)

### 🔗 **Fluxo de funcionamento:**
- 🕸️ **Scraper:** Extrai os dados diretamente das tabelas do site da Embrapa.
- 🔗 **API (FastAPI):** Expõe os dados através de endpoints REST.
- ☁️ **Client:** Usuários consomem os dados via API documentada (Swagger, Postman, Front-end ou outros sistemas).
- 💾 **Banco de Dados (Futuro):** Possibilidade de persistir os dados para histórico e performance.
- 🔒 **Autenticação (Futuro):** Pode ser implementada com JWT ou API Key.

---

## 🚀 Deploy

Projeto preparado para deploy em plataformas como Render, Railway ou AWS, além de permitir evolução futura para Docker e ambientes escaláveis.

---

## 🚀 Futuras melhorias

- Persistência dos dados em banco SQL/NoSQL.
- Autenticação (JWT ou API Key).
- Deploy com Docker.
- Monitoramento e logs estruturados.
- Agendamento de atualizações automáticas dos dados.

---

## 🧠 Autor

Daniel Souza  
Projeto desenvolvido para o **Tech Challenge — Pós Tech Machine Learning Engineering — FIAP**.

---