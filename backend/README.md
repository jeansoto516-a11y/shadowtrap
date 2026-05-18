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