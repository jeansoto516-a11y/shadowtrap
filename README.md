# ShadowTrap

## SSH Honeypot & Threat Monitoring System

ShadowTrap é um sistema avançado de Honeypot SSH desenvolvido para estudos de cibersegurança, monitoramento de ameaças e análise de comportamento malicioso em redes.

O projeto simula um servidor SSH vulnerável capaz de capturar tentativas de conexão, credenciais, comandos executados e atividades suspeitas em tempo real através de um sistema de monitoramento desenvolvido em Python.

---

# Objetivo do Projeto

O principal objetivo do ShadowTrap é criar um ambiente controlado para:

- Monitoramento de ataques SSH
- Captura de tentativas de autenticação
- Registro de atividades suspeitas
- Estudos de segurança ofensiva e defensiva
- Análise de comportamento de invasores
- Simulação de ambientes honeypot
- Aprendizado de redes e protocolos TCP/SSH

---

# Tecnologias Utilizadas

## Backend
- Python
- FastAPI
- Paramiko
- SQLAlchemy
- WebSockets

## Banco de Dados
- SQLite
- PostgreSQL (futuramente)

## Frontend (em desenvolvimento)
- React
- Vite
- TailwindCSS

## Infraestrutura
- Docker
- Docker Compose

---

# Funcionalidades

## Implementadas
- Estrutura profissional do projeto
- API FastAPI
- Servidor TCP Honeypot
- Detecção de conexões
- Sistema de threads
- Integração inicial do backend

## Em Desenvolvimento
- Servidor SSH fake real
- Captura de usuário e senha
- Logs avançados
- Dashboard de monitoramento
- Estatísticas de ataques
- WebSocket em tempo real
- Sistema de autenticação
- GeoIP
- Dockerização

---

# Estrutura do Projeto

```bash
shadowtrap/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── honeypot/
│   │   ├── logs/
│   │   ├── services/
│   │   └── utils/
│
├── frontend/
│
└── README.md

🖥️ Como Executar o Projeto
📥 1. Clonar o repositório
git clone https://github.com/SEU-USUARIO/shadowtrap.git
📂 2. Acessar o projeto
cd shadowtrap/backend
🐍 3. Criar ambiente virtual
python -m venv venv
⚡ 4. Ativar ambiente virtual
Windows (PowerShell)
.\venv\Scripts\Activate

Quando ativado, aparecerá:

(venv)

📦 5. Instalar dependências
pip install -r requirements.txt

🚀 6. Rodar a aplicação
uvicorn app.main:app --reload

🌐 Acessos do Sistema

API Principal
http://127.0.0.1:8000

Documentação Swagger
http://127.0.0.1:8000/docs

⚠️ Aviso Legal

Este projeto possui finalidade exclusivamente educacional e de pesquisa em cibersegurança.

O ShadowTrap NÃO deve ser utilizado para atividades ilegais, invasões ou qualquer ação não autorizada em ambientes reais.

🧭 Roadmap
 Estrutura inicial do projeto
 API FastAPI
 Servidor TCP Honeypot
 Honeypot SSH real
 Captura de credenciais
 Sistema de logs
 Banco de dados completo
 Dashboard web
 Monitoramento em tempo real
 GeoIP tracking
 Dockerização
 Deploy em VPS Linux

👨‍💻 Autor

Jean Carlos Soto Barbosa

👨‍💻 Desenvolvedor
Desenvolvido por Jean Carlos Soto Barbosa.

Focado em:

Engenharia de Software
Backend Development
APIs REST
Inteligência Artificial
Sistemas Financeiros
Análise Quantitativa

🔥 ShadowTrap Status
ACTIVE • MONITORING • READY FOR ATTACK DATA COLLECTION
