#📊 VitiBrasil API — Pós-Tech FIAP
API desenvolvida para consulta de dados públicos sobre vitivinicultura no Brasil, disponibilizados pela Embrapa.

Este projeto foi desenvolvido como parte do Tech Challenge — Pós-Tech Machine Learning Engineering — FIAP, atendendo todos os requisitos propostos, desde o desenvolvimento da API, autenticação, scraping dos dados, documentação e deploy do MVP.

#🏗️ Como o projeto está organizado
PosTech/
- .env → Variáveis de ambiente (não versionado)
- .gitignore → Arquivos ignorados no controle de versão
- README.md → Documentação do projeto
- requirements.txt → Dependências do projeto

- app/
  - api/ → Rotas da API e autenticação
    - auth.py → Gerenciamento de autenticação JWT
    - endpoints.py → Endpoints principais (produção, processamento, etc.)
  
  - core/ → Configurações de segurança e geração de tokens
    - security.py
  
  - db/ → (Reservado para banco de dados futuro)
    - database.py
  
  - models/ → (Reservado para modelos futuros)
    - data_models.py
  
  - schemas/ → Validação de dados (Pydantic)
    - auth.py
  
  - services/ → Scraper dos dados do site da Embrapa
    - scraper.py
  
  - main.py → Inicialização da API FastAPI

- .git/ → Dados internos do Git

#🚀 Funcionalidades principais
##🔍 Scraping em tempo real dos dados públicos da Embrapa.

##📊 Endpoints REST para:

Produção

Processamento

Comercialização

Importação

Exportação

##🔐 Autenticação via JWT.

##📑 Documentação automática via Swagger.

##☁️ Deploy online com link público.

###☁️ Link do MVP
API publicada em:
https://postech-m8h5.onrender.com

Documentação Swagger:
https://postech-m8h5.onrender.com/docs

##✅ Verificação dos requisitos
| Requisito                                                                                       | Status                                                                    |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Criar uma REST API em Python que faça a consulta no site da Embrapa.**                        | ✅ Feito — API funcional, faz scraping em tempo real.                      |
| **Sua API deve estar documentada.**                                                             | ✅ Feito — Documentação automática via Swagger em `/docs`.                 |
| **É recomendável (não obrigatório) a escolha de um método de autenticação (JWT, por exemplo).** | ✅ Feito — Autenticação com JWT implementada.                              |
| **Criar um plano para fazer o deploy da API, desenhando a arquitetura do projeto.**             | ✅ Feito — Diagrama de arquitetura criado e README explicando a estrutura. |
| **Fazer um MVP realizando o deploy com um link compartilhável e um repositório no GitHub.**     | ✅ Feito — API publicada no Render e repositório disponível no GitHub.     |

##🧠 Cenário de aplicação da API
A API pode ser utilizada para:

###📈 Dashboards dinâmicos com dados atualizados da vitivinicultura.

###🔍 Análises estatísticas de produção, comercialização, importação e exportação.

###🤖 Alimentação de modelos futuros de Machine Learning, como previsão de produção ou tendências de mercado.
