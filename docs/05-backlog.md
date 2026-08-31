# SISADA — Backlog do MVP

**Documento:** `05-backlog.md`
**Versão:** 0.1
**Status:** EXECUTÁVEL

---

# EPIC 01 — Fundação

## PROJ-001 — Criar repositório e estrutura inicial
Critérios:
- backend/
- frontend/
- docs/
- .gitignore
- README.md
- .env.example
- primeiro commit padronizado

## PROJ-002 — Adicionar documentação existente ao repositório
Critérios:
- product requirements
- domain rules
- data model
- architecture
- ADRs

## INFRA-001 — Criar Docker Compose
Critérios:
- serviço backend
- serviço frontend
- PostgreSQL
- Redis
- volumes
- variáveis por .env

## BACK-001 — Inicializar FastAPI
Critérios:
- aplicação sobe
- /health retorna 200
- estrutura app/core/modules criada

## FRONT-001 — Inicializar React + TypeScript + Vite
Critérios:
- aplicação sobe
- página inicial simples
- build funciona

## DB-001 — Configurar SQLAlchemy
Critérios:
- conexão PostgreSQL
- AsyncSession
- dependency de sessão
- teste de conexão

## DB-002 — Configurar Alembic
Critérios:
- Alembic inicializado
- migration executável
- banco atualizável com alembic upgrade head

## QA-001 — Configurar Pytest
Critérios:
- teste /health
- comando pytest funcional

## CI-001 — Pipeline inicial GitHub Actions
Critérios:
- backend tests
- frontend build
- execução em Pull Request

---

# EPIC 02 — Usuários e autenticação

## AUTH-001 — Criar User e Role
## AUTH-002 — Criar migration de usuários e papéis
## AUTH-003 — Implementar hash de senha
## AUTH-004 — Implementar cadastro administrativo
## AUTH-005 — Implementar login
## AUTH-006 — Implementar access token
## AUTH-007 — Implementar refresh token
## AUTH-008 — Endpoint /me
## AUTH-009 — Controle de papéis
## AUTH-010 — Testes de autenticação e autorização

---

# EPIC 03 — Estrutura organizacional

## ORG-001 — Criar StudentBody
## ORG-002 — Criar TrainingUnit
## ORG-003 — Criar StudentProfile
## ORG-004 — Criar InstructorProfile
## ORG-005 — Criar StudentUnitMembership
## ORG-006 — Criar InstructorUnitMembership
## ORG-007 — Impedir dois memberships ativos
## ORG-008 — CRUD administrativo de unidades
## ORG-009 — CRUD administrativo de alunos
## ORG-010 — CRUD administrativo de instrutores
## ORG-011 — Alterar vínculo preservando histórico

---

# EPIC 04 — Atributos

## ATT-001 — Criar Attribute
## ATT-002 — Criar AttributeVersion
## ATT-003 — Seed dos seis atributos
## ATT-004 — CRUD administrativo
## ATT-005 — Preservar versões históricas

---

# EPIC 05 — Ciclos de avaliação

## CYC-001 — Criar EvaluationCycle
## CYC-002 — Habilitar SELF/PEER/VERTICAL
## CYC-003 — Criar CycleStudent
## CYC-004 — Criar CycleInstructor
## CYC-005 — Criar CycleAttribute
## CYC-006 — Gerar snapshot do ciclo
## CYC-007 — Abrir ciclo
## CYC-008 — Fechar ciclo manualmente
## CYC-009 — Publicar ciclo
## CYC-010 — Auditar mudanças de estado

---

# EPIC 06 — Assignments

## ASN-001 — Criar EvaluationAssignment
## ASN-002 — Gerar SELF
## ASN-003 — Gerar PEER
## ASN-004 — Gerar VERTICAL
## ASN-005 — Impedir duplicidade
## ASN-006 — Cancelar assignment com justificativa
## ASN-007 — Calcular percentual de conclusão

---

# EPIC 07 — Avaliações

## EVA-001 — Criar Evaluation
## EVA-002 — Criar EvaluationScore
## EVA-003 — Criar formulário de avaliação
## EVA-004 — Salvar rascunho
## EVA-005 — Submeter avaliação
## EVA-006 — Editar enquanto ciclo estiver OPEN
## EVA-007 — Bloquear edição após fechamento
## EVA-008 — Campos positivo/negativo opcionais
## EVA-009 — Validar score 0.000–10.000
## EVA-010 — Testes das invariantes SELF/PEER/VERTICAL

---

# EPIC 08 — Analytics

## ANA-001 — Média PEER por atributo
## ANA-002 — Média VERTICAL por atributo
## ANA-003 — Gap SELF x PEER
## ANA-004 — Distância euclidiana
## ANA-005 — Comparação com turma
## ANA-006 — Evolução temporal
## ANA-007 — Endpoint analytics do aluno
## ANA-008 — Testes dos cálculos

---

# EPIC 09 — Dashboards

## DASH-001 — Dashboard aluno
## DASH-002 — Avaliações pendentes
## DASH-003 — Dashboard instrutor
## DASH-004 — Progresso do ciclo
## DASH-005 — Radar chart
## DASH-006 — Histórico de desempenho

---

# EPIC 10 — Relatórios e IA

## REP-001 — Criar AIReport
## REP-002 — Criar interface AIProvider
## REP-003 — MockAIProvider
## REP-004 — Consolidar observações
## REP-005 — Criar job Celery
## REP-006 — Gerar minuta
## REP-007 — Revisar relatório
## REP-008 — Aprovar relatório
## REP-009 — Exibir relatório ao aluno
## REP-010 — Registrar modelo e prompt

---

# EPIC 11 — Auditoria e segurança

## AUD-001 — Criar AuditLog
## AUD-002 — Auditar fechamento de ciclo
## AUD-003 — Auditar cancelamentos
## AUD-004 — Auditar consulta de comentário identificado
## SEC-001 — Rate limiting
## SEC-002 — Política de senha
## SEC-003 — Tratamento uniforme de erros
## SEC-004 — Revisão de permissões
## SEC-005 — Proteção de secrets

---

# EPIC 12 — Entrega

## DEP-001 — Ambiente de produção
## DEP-002 — Nginx/HTTPS
## DEP-003 — Backup PostgreSQL
## DEP-004 — Logs
## DEP-005 — Deploy
## DEP-006 — README final
## DEP-007 — Diagramas e screenshots para portfólio
