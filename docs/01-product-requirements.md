# SISADA — Especificação de Produto

**Documento:** `01-product-requirements.md`  
**Versão:** 0.1  
**Status:** DRAFT — em revisão  
**Objetivo:** consolidar os requisitos iniciais do sistema antes da modelagem de dados e implementação.

---

## 1. Visão do produto

O SISADA será um sistema web para apoiar a avaliação atitudinal de alunos dos Órgãos de Formação de Oficiais da Reserva (OFOR).

O sistema deverá digitalizar e padronizar a coleta de:

- autoavaliações;
- avaliações laterais realizadas entre alunos;
- avaliações verticais realizadas por instrutores;
- registros textuais de fatos positivos e negativos observados.

O objetivo do produto **não é eliminar a subjetividade**, porque a avaliação de atitudes possui componente inerentemente humano. O objetivo é:

1. reduzir arbitrariedade por meio de critérios padronizados;
2. agregar múltiplos pontos de vista;
3. aumentar rastreabilidade e transparência do processo;
4. permitir análise quantitativa dos resultados;
5. apoiar feedback e acompanhamento da evolução do aluno;
6. produzir relatórios institucionais a partir de dados estruturados.

---

## 2. Base normativa considerada nesta versão

Esta versão foi elaborada a partir de:

- NAA — EB60-N-06.004, 5ª Edição, 2020;
- NIAA/OFOR, 2ª Edição, 2021.

Regras relevantes identificadas:

- a NAA prevê avaliação vertical, autoavaliação e avaliação lateral;
- a avaliação formativa possui caráter de acompanhamento e não deve integrar diretamente a nota de aprovação;
- a avaliação deve considerar múltiplos pontos de vista, incluindo o próprio discente;
- a NIAA/OFOR prevê três avaliações atitudinais anuais: duas formativas e uma somativa;
- a avaliação atitudinal deve ser baseada em registros de observação;
- a NIAA/OFOR remete as regras específicas da avaliação atitudinal à NIDACA/OFOR;
- a composição oficial da Nota de Conceito e o papel exato da avaliação lateral permanecem bloqueados até análise da NIDACA/OFOR.

**Regra do projeto:** nenhuma fórmula oficial de Nota de Conceito será implementada antes da análise da NIDACA/OFOR.

---

## 3. Perfis de usuário

### 3.1 Aluno

O aluno deverá poder:

- autenticar-se no sistema;
- visualizar avaliações pendentes;
- realizar sua autoavaliação;
- avaliar os demais alunos do seu pelotão quando autorizado pelo ciclo;
- registrar notas por atributo;
- registrar fatos positivos e negativos;
- salvar avaliação em rascunho;
- revisar a avaliação antes do envio;
- submeter definitivamente a avaliação;
- visualizar os próprios resultados quando estes forem publicados;
- comparar sua autoavaliação com resultados consolidados permitidos.

### 3.2 Instrutor

O instrutor deverá poder:

- autenticar-se no sistema;
- visualizar alunos pertencentes aos pelotões aos quais estiver vinculado;
- realizar avaliação vertical dos alunos sob sua responsabilidade;
- consultar resultados consolidados dos alunos autorizados;
- consultar autoavaliações quando permitido;
- acompanhar o progresso de conclusão das avaliações;
- cadastrar, editar e desativar alunos dentro do escopo administrativo que lhe for concedido.

**Decisão provisória:** um instrutor não terá acesso global por padrão. O acesso será definido por vínculos entre instrutor e um ou mais pelotões.

### 3.3 Administrador

O administrador deverá poder:

- gerenciar instrutores;
- gerenciar alunos;
- gerenciar pelotões;
- gerenciar turmas e cursos;
- criar e configurar ciclos de avaliação;
- abrir e fechar ciclos;
- acompanhar o progresso das avaliações;
- vincular instrutores a pelotões;
- cancelar ou reabrir avaliações mediante justificativa;
- consultar logs de auditoria.

**Restrição:** administradores não poderão editar diretamente notas ou comentários de avaliações já submetidas. Qualquer correção deverá ocorrer por fluxo controlado e auditável.

---

## 4. Estrutura organizacional inicial

O sistema deverá representar ao menos:

```text
OFOR
└── Curso/Turma
    └── Pelotão
        ├── Alunos
        └── Instrutores vinculados
```

A estrutura definitiva será definida na modelagem de domínio.

---

## 5. Tipos de avaliação

O sistema deverá suportar os seguintes tipos:

```text
SELF       -> autoavaliação
PEER       -> avaliação lateral
VERTICAL   -> avaliação realizada por instrutor
```

Uma avaliação lateral deverá possuir:

- um avaliador;
- um avaliado;
- um ciclo;
- notas por atributo;
- registros de observação;
- status;
- data de submissão.

O avaliador e o avaliado não poderão ser o mesmo usuário em uma avaliação `PEER`.

---

## 6. Atributos iniciais

O sistema deverá suportar inicialmente:

1. Apresentação;
2. Cooperação;
3. Coragem;
4. Persistência;
5. Equilíbrio Emocional;
6. Zelo.

Os atributos não deverão ser colunas fixas da entidade de avaliação.

Eles deverão ser cadastráveis/configuráveis para permitir alterações futuras sem modificar a estrutura principal do banco de dados.

---

## 7. Ciclo de avaliação

Um ciclo representa uma janela controlada de coleta de avaliações.

Exemplo:

```text
Avaliação Formativa — Maio/2027
Abertura: 01 MAI
Fechamento: 10 MAI
Tipos habilitados:
- SELF
- PEER
- VERTICAL
```

Estados iniciais previstos:

```text
DRAFT
SCHEDULED
OPEN
CLOSED
PROCESSING
PUBLISHED
ARCHIVED
```

### 7.1 Regra importante

O ciclo **não será fechado automaticamente apenas porque todos concluíram suas avaliações**.

O sistema poderá indicar:

```text
100% concluído — pronto para encerramento
```

mas o fechamento será uma ação administrativa ou ocorrerá por regra explícita de prazo.

Isso evita problemas com:

- ausência de aluno;
- desligamento;
- erro de cadastro;
- avaliação anulada;
- necessidade de reabertura;
- exceções administrativas.

---

## 8. Pendências individuais

Cada obrigação de avaliação será representada separadamente.

Exemplo:

```text
Aluno A -> avaliar Aluno B -> PEER
Aluno A -> avaliar Aluno C -> PEER
Aluno A -> avaliar Aluno A -> SELF
Instrutor X -> avaliar Aluno A -> VERTICAL
```

Estados previstos:

```text
ASSIGNED
IN_PROGRESS
SUBMITTED
CANCELLED
```

Assim, o sistema poderá calcular com precisão:

- quantidade esperada;
- quantidade concluída;
- percentual de conclusão;
- usuários pendentes.

---

## 9. Fluxo do aluno

```text
Login
  ↓
Dashboard
  ↓
Avaliações Pendentes
  ↓
Autoavaliação / Avaliação dos Pares
  ↓
Selecionar avaliação pendente
  ↓
Preencher atributos
  ↓
Registrar fatos positivos/negativos
  ↓
Revisar
  ↓
Submeter
  ↓
Confirmação de conclusão
```

Uma avaliação submetida não poderá ser editada livremente.

---

## 10. Fluxo do instrutor

```text
Login
  ↓
Dashboard do Instrutor
  ↓
Pelotões autorizados
  ↓
Aluno
  ↓
Avaliação Vertical
  ↓
Notas por atributo
  ↓
Registros positivos/negativos
  ↓
Revisar
  ↓
Submeter
```

---

## 11. Resultados apresentados ao aluno

Após publicação autorizada do ciclo, o aluno poderá visualizar, conforme regras normativas ainda a confirmar:

- média consolidada de cada atributo;
- indicador geral de desempenho;
- comparação entre sua autoavaliação e a avaliação consolidada;
- comparação com estatísticas da turma;
- evolução ao longo de ciclos anteriores.

Exemplo conceitual:

| Atributo | Autoavaliação | Pares | Referência da turma |
|---|---:|---:|---:|
| Cooperação | 8,5 | 7,8 | 7,5 |
| Coragem | 7,5 | 8,1 | 7,9 |

### Questão em aberto

A expressão “abaixo / na média / acima da turma” exige uma regra matemática objetiva.

A tolerância que define “na média” ainda não foi definida e não deverá ser inventada durante a implementação.

## 11.1. Indicador de alinhamento entre autoavaliação e pares

O sistema deverá calcular a diferença entre a percepção do próprio aluno e a percepção consolidada de seus pares.

Para cada ciclo em que existam autoavaliação e avaliações laterais suficientes, serão construídos dois vetores com os mesmos atributos:

```text
A = vetor da autoavaliação
P = vetor das médias das avaliações dos pares
```

A distância euclidiana entre esses vetores será calculada por:

```text
d(A,P) = √Σ(Ai - Pi)²
```

Quanto menor o valor, maior a proximidade matemática entre a autoavaliação do aluno e a percepção agregada de seus pares.

### Exemplo

```text
Autoavaliação:
[8, 7, 9, 8, 6, 9]

Média dos pares:
[7, 8, 8, 7, 7, 8]

Distância Euclidiana ≈ 2,45
```

O indicador deverá ser tratado como ferramenta de análise e feedback, e não como componente automático da nota oficial.

Além da distância global, o sistema deverá apresentar o **gap por atributo**:

```text
gap_atributo = autoavaliação - média_dos_pares
```

Isso permitirá identificar quais atributos mais contribuem para a divergência entre autoimagem e percepção externa.

Exemplo:

| Atributo | Auto | Pares | Gap |
|---|---:|---:|---:|
| Apresentação | 8,0 | 7,8 | +0,2 |
| Cooperação | 8,0 | 8,1 | -0,1 |
| Equilíbrio Emocional | 10,0 | 5,5 | +4,5 |

O sistema também deverá permitir analisar a evolução da distância ao longo dos ciclos.

Exemplo:

```text
Ciclo 1 -> 3,10
Ciclo 2 -> 2,40
Ciclo 3 -> 1,60
Ciclo 4 -> 1,20
```

### Questão em aberto

Categorias interpretativas como:

```text
ALINHADO
LEVE DIVERGÊNCIA
DIVERGÊNCIA
FORTE DIVERGÊNCIA
```

não deverão ser implementadas sem uma justificativa metodológica ou normativa para os respectivos limites.

---

## 12. Privacidade das avaliações laterais

O aluno avaliado não deverá receber a identidade individual de quem atribuiu determinada nota ou comentário, salvo se norma aplicável determinar o contrário.

Resultados laterais deverão ser apresentados de forma agregada.

O sistema deverá prever um número mínimo de avaliações antes de apresentar estatísticas laterais, evitando inferência da identidade de avaliadores em grupos muito pequenos.

O valor mínimo será definido posteriormente.

---

## 13. Registros de observação

Cada avaliação poderá conter registros de fatos observados.

Tipos iniciais:

```text
POSITIVE
NEGATIVE
```

Cada registro deverá possuir:

- texto;
- autor;
- avaliado;
- ciclo;
- data;
- tipo;
- vínculo com a avaliação correspondente.

O sistema deverá incentivar descrições factuais e contextualizadas, evitando comentários genéricos.

---

## 14. Inteligência Artificial

A IA atuará exclusivamente como ferramenta de apoio à elaboração textual.

Fluxo previsto:

```text
Avaliações concluídas
       ↓
Backend consolida dados permitidos
       ↓
Observações positivas/negativas
       ↓
Serviço de IA
       ↓
Minuta de relatório
       ↓
Revisão humana
       ↓
Aprovação
```

### Restrições da IA

A IA:

- não calculará a nota oficial;
- não alterará avaliações;
- não criará fatos que não estejam presentes nos dados fornecidos;
- não decidirá aprovação ou reprovação;
- não publicará relatório sem revisão humana;
- não receberá identidade dos avaliadores laterais quando isso não for necessário.

A geração deverá registrar, futuramente:

- modelo utilizado;
- versão do prompt;
- data da geração;
- responsável pela aprovação;
- versão do relatório.

---

## 15. Requisitos funcionais iniciais

### Autenticação

- **RF-001** — O sistema deverá permitir login de usuários ativos.
- **RF-002** — O sistema deverá controlar permissões conforme papel e escopo.
- **RF-003** — O sistema deverá impedir acesso a recursos não autorizados.

### Gestão acadêmica

- **RF-010** — O administrador deverá cadastrar alunos.
- **RF-011** — O administrador deverá cadastrar instrutores.
- **RF-012** — O administrador deverá cadastrar pelotões.
- **RF-013** — O administrador deverá vincular alunos a pelotões.
- **RF-014** — O administrador deverá vincular instrutores a pelotões.

### Ciclos

- **RF-020** — O administrador deverá criar ciclos de avaliação.
- **RF-021** — O administrador deverá definir data de abertura e encerramento.
- **RF-022** — O administrador deverá definir os tipos de avaliação habilitados.
- **RF-023** — O sistema deverá impedir submissões fora do período aberto.
- **RF-024** — O sistema deverá calcular o percentual de conclusão do ciclo.

### Autoavaliação

- **RF-030** — O aluno deverá realizar uma autoavaliação por ciclo quando habilitada.
- **RF-031** — O sistema deverá impedir mais de uma autoavaliação válida do mesmo aluno no mesmo ciclo.

### Avaliação lateral

- **RF-040** — O aluno deverá avaliar os demais alunos autorizados de seu pelotão.
- **RF-041** — O sistema deverá impedir que um aluno realize avaliação lateral de si mesmo.
- **RF-042** — O sistema deverá impedir avaliações laterais duplicadas no mesmo ciclo.
- **RF-043** — O sistema deverá ocultar a identidade individual do avaliador nos resultados apresentados ao aluno avaliado.

### Avaliação vertical

- **RF-050** — O instrutor deverá avaliar alunos pertencentes ao seu escopo autorizado.
- **RF-051** — O sistema deverá impedir avaliação vertical de aluno fora do escopo do instrutor.

### Avaliação

- **RF-060** — Cada avaliação deverá registrar notas para todos os atributos obrigatórios.
- **RF-061** — A avaliação poderá possuir fatos positivos e negativos.
- **RF-062** — O usuário poderá salvar uma avaliação como rascunho.
- **RF-063** — O usuário deverá confirmar a submissão.
- **RF-064** — Uma avaliação submetida deverá tornar-se imutável no fluxo normal.

### Resultados

- **RF-070** — O sistema deverá calcular estatísticas consolidadas por atributo.
- **RF-071** — O aluno deverá visualizar apenas seus próprios resultados autorizados.
- **RF-072** — O instrutor deverá visualizar resultados dos alunos de seu escopo.
- **RF-073** — O sistema deverá permitir comparação entre autoavaliação e avaliação consolidada.
- **RF-074** — O sistema deverá calcular a distância euclidiana entre o vetor de autoavaliação do aluno e o vetor das médias das avaliações laterais correspondentes aos mesmos atributos.
- **RF-075** — O sistema deverá calcular e apresentar o gap entre autoavaliação e média dos pares para cada atributo.
- **RF-076** — O sistema deverá preservar e permitir consultar a evolução histórica da distância euclidiana por ciclo de avaliação.

### IA

- **RF-080** — O sistema deverá consolidar registros de observação para geração de relatório.
- **RF-081** — O sistema deverá solicitar à IA uma minuta textual.
- **RF-082** — A minuta deverá exigir revisão humana antes da publicação.
- **RF-083** — O sistema deverá manter histórico das versões geradas e aprovadas.

---

## 16. Requisitos não funcionais iniciais

- **RNF-001 — Segurança:** senhas nunca poderão ser armazenadas em texto puro.
- **RNF-002 — Autorização:** toda operação protegida deverá validar papel e escopo.
- **RNF-003 — Auditoria:** ações administrativas críticas deverão ser registradas.
- **RNF-004 — Integridade:** avaliações submetidas não poderão ser alteradas silenciosamente.
- **RNF-005 — Rastreabilidade:** alterações de configuração deverão registrar autor e data.
- **RNF-006 — Testabilidade:** regras de negócio críticas deverão possuir testes automatizados.
- **RNF-007 — Portabilidade:** a aplicação deverá poder ser executada por Docker.
- **RNF-008 — Documentação:** endpoints deverão possuir documentação OpenAPI.
- **RNF-009 — Privacidade:** avaliações laterais deverão ser agregadas para apresentação ao avaliado.
- **RNF-010 — IA:** conteúdo produzido por IA deverá ser identificado como minuta até aprovação humana.

---

## 17. Decisões ainda não fechadas

### BLOQUEADORAS

1. Fórmula oficial de cálculo da avaliação atitudinal.
2. Peso da avaliação vertical.
3. Papel da avaliação lateral no resultado oficial.
4. Papel da autoavaliação no resultado oficial.
5. Escala exata das notas.
6. Critérios dos seis atributos.
7. Regras de anonimato previstas pela NIDACA/OFOR.
8. Quem pode visualizar comentários individuais.
9. Forma oficial de publicação dos resultados.

Esses itens dependem principalmente da análise da **NIDACA/OFOR**.

### NÃO BLOQUEADORAS

1. Fórmula para “abaixo / na média / acima da turma”.
2. Número mínimo de avaliações para liberar média lateral.
3. Limiares para interpretar a distância euclidiana como alinhamento, leve divergência, divergência ou forte divergência.
4. Política de reabertura de avaliação.
5. Estratégia de gamificação.
6. Formato do relatório PDF.
7. Provedor de IA.

---

## 18. Questão específica sobre avaliações formativas adicionais

A NIAA/OFOR analisada prevê três avaliações atitudinais anuais: duas formativas e uma somativa.

O sistema poderá tecnicamente suportar ciclos adicionais, mas eles não deverão ser classificados automaticamente como avaliações atitudinais oficiais.

Uma possibilidade futura é distinguir:

```text
OFFICIAL_ATTITUDINAL
DEVELOPMENT_CHECKIN
```

Essa decisão somente será fechada após análise da NIDACA/OFOR.

---

## 19. Fora do escopo do primeiro MVP

O primeiro MVP não incluirá:

- cálculo oficial da Nota de Conceito;
- ranking público;
- IA generativa;
- PDF institucional;
- notificações em tempo real;
- aplicativo mobile;
- microserviços;
- integração com sistemas externos do Exército.

O objetivo do MVP inicial é validar:

```text
usuário
+ pelotão
+ ciclo
+ avaliação
+ atributos
+ observações
+ consolidação básica
```

---

## 20. Critério para encerrar a fase de requisitos

A fase de requisitos será considerada suficientemente madura para iniciar a modelagem de dados quando:

- [ ] os papéis e permissões estiverem fechados;
- [ ] o comportamento do ciclo estiver definido;
- [ ] as regras de autoavaliação estiverem definidas;
- [ ] as regras de avaliação lateral estiverem definidas;
- [ ] as regras de avaliação vertical estiverem definidas;
- [ ] os dados mínimos do aluno estiverem definidos;
- [ ] a NIDACA/OFOR tiver sido analisada ou suas dependências explicitamente isoladas;
- [ ] as principais regras de privacidade estiverem definidas.

---

## 21. Próxima etapa

Após aprovação deste documento:

1. fechar questões de escopo pendentes;
2. elaborar `02-domain-rules.md`;
3. desenhar entidades e relacionamentos;
4. criar `03-architecture.md`;
5. criar ADRs;
6. decompor o MVP em épicos, histórias e tasks;
7. somente então inicializar o código.
