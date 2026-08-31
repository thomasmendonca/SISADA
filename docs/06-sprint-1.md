# SISADA — Sprint 1

**Objetivo da Sprint:** criar a fundação técnica do projeto sem implementar regras de avaliação.

## SPRINT-1

### PROJ-001 — Criar repositório e estrutura inicial

Critérios de aceitação:
- [ ] repositório Git criado
- [ ] pastas backend, frontend e docs
- [ ] .gitignore
- [ ] README.md inicial
- [ ] .env.example
- [ ] documentação adicionada
- [ ] commit seguindo Conventional Commits

Commit sugerido:
`chore: initialize project structure`

---

### BACK-001 — Inicializar FastAPI

Critérios:
- [ ] FastAPI instalado
- [ ] app/main.py
- [ ] aplicação inicia com Uvicorn
- [ ] GET /health retorna HTTP 200
- [ ] teste básico criado

Commit sugerido:
`feat(backend): initialize fastapi application`

---

### FRONT-001 — Inicializar React + TypeScript + Vite

Critérios:
- [ ] projeto Vite criado
- [ ] TypeScript habilitado
- [ ] aplicação inicia localmente
- [ ] build funciona

Commit sugerido:
`feat(frontend): initialize react application`

---

### INFRA-001 — PostgreSQL + Redis com Docker Compose

Critérios:
- [ ] docker-compose.yml
- [ ] PostgreSQL sobe
- [ ] Redis sobe
- [ ] volumes persistentes
- [ ] credenciais vindas do .env
- [ ] nenhum segredo commitado

Commit sugerido:
`build(infra): add postgres and redis services`

---

### DB-001 — SQLAlchemy

Critérios:
- [ ] SQLAlchemy 2.x
- [ ] asyncpg
- [ ] configuração DATABASE_URL
- [ ] AsyncSession
- [ ] dependency get_session
- [ ] aplicação conecta ao banco

Commit sugerido:
`feat(db): configure sqlalchemy database session`

---

### DB-002 — Alembic

Critérios:
- [ ] Alembic instalado
- [ ] configuração ligada aos models
- [ ] migration inicial executável
- [ ] alembic upgrade head funciona

Commit sugerido:
`build(db): configure alembic migrations`

---

### QA-001 — Pytest

Critérios:
- [ ] pytest configurado
- [ ] teste do /health
- [ ] testes executam sem erro

Commit sugerido:
`test(backend): add health endpoint test`

---

## Definition of Done da Sprint

A Sprint 1 termina quando:

- [ ] frontend sobe
- [ ] backend sobe
- [ ] PostgreSQL sobe
- [ ] Redis sobe
- [ ] /health responde
- [ ] backend conecta no PostgreSQL
- [ ] migration funciona
- [ ] pytest passa
- [ ] documentação está no repositório
- [ ] nenhum segredo foi commitado

## Não fazer nesta Sprint

- User
- login
- JWT
- avaliação
- Redis cache
- Celery
- IA

A meta é fundação, não quantidade de features.
