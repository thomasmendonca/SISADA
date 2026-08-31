# SISADA — Regras de Domínio

**Documento:** `02-domain-rules.md`  
**Versão:** 0.2  
**Status:** DRAFT — pronto para revisão antes da modelagem de dados  
**Dependências:** `01-product-requirements.md`, NAA (EB60-N-06.004, 5ª Ed/2020), NIAA/OFOR (2ª Ed/2021)

---

# 1. Objetivo

Este documento transforma os requisitos de produto do SISADA em regras de negócio explícitas.

As regras aqui descritas deverão orientar:

- modelagem do banco;
- serviços do backend;
- validações da API;
- permissões;
- testes automatizados;
- comportamento do frontend;
- geração de relatórios.

Regra geral do projeto:

> regras oficiais de composição da Nota de Conceito e demais regras específicas da avaliação atitudinal não serão inventadas antes da análise da NIDACA/OFOR.

---

# 2. Conceitos principais

## 2.1 Usuário

Pessoa autenticável no sistema.

Papéis iniciais:

```text
STUDENT
INSTRUCTOR
ADMIN
```

O papel define capacidades gerais.

O **escopo** define sobre quais dados o usuário pode atuar.

---

# 3. Corpo de Alunos, unidades e vínculos

## RD-ORG-001 — Corpo de Alunos é a unidade organizacional raiz

O sistema deverá representar o Corpo de Alunos como entidade organizacional superior.

## RD-ORG-002 — Pelotão e Curso são tipos da mesma entidade de agrupamento

Abaixo do Corpo de Alunos existirão unidades de formação.

```text
StudentBody
    ↓
TrainingUnit
```

`TrainingUnit.type` poderá assumir inicialmente:

```text
PLATOON
COURSE
```

Isso permite que, no decorrer do ano, o aluno deixe de pertencer a um pelotão e passe a pertencer a um curso sem que o sistema trate os dois conceitos como estruturas incompatíveis.

## RD-PLT-001 — Aluno pertence a uma unidade de formação ativa

Um aluno deverá possuir, no máximo, um vínculo ativo com uma `TrainingUnit` em determinado momento.

O histórico de vínculos anteriores deverá ser preservado.

## RD-PLT-002 — Instrutor pertence a uma unidade de formação ativa

Um instrutor deverá possuir, no máximo, um vínculo ativo com uma unidade de formação em determinado momento.

A unidade pode ser do tipo `PLATOON` ou `COURSE`, conforme a organização do Corpo de Alunos.

O instrutor poderá mudar de unidade ao longo do curso.

O histórico deverá ser preservado.

## RD-PLT-003 — Uma unidade pode possuir vários instrutores

A relação é:

```text
TrainingUnit 1 ---- N Instrutores
```

Embora um instrutor tenha apenas uma unidade ativa por vez, vários instrutores podem pertencer simultaneamente à mesma unidade.

## RD-PLT-004 — Mudança de pelotão não apaga histórico

Mudanças de pelotão não deverão modificar retroativamente avaliações realizadas em ciclos anteriores.

A avaliação deverá permanecer associada ao contexto existente no momento de sua realização.

---

# 4. Ciclo de avaliação

## RD-CYC-001 — Toda avaliação pertence a um ciclo

Não poderá existir avaliação SELF, PEER ou VERTICAL sem um `EvaluationCycle`.

## RD-CYC-002 — O ciclo controla a janela de edição

Enquanto o ciclo estiver `OPEN`, avaliações atribuídas poderão ser:

- iniciadas;
- salvas;
- submetidas;
- editadas novamente pelo próprio avaliador.

Depois do fechamento do ciclo, essas avaliações tornam-se bloqueadas no fluxo normal.

## RD-CYC-003 — Encerramento manual

O ciclo não será encerrado automaticamente ao atingir 100% de conclusão.

O sistema deverá calcular o progresso e poderá informar:

```text
100% concluído — pronto para encerramento
```

O encerramento efetivo será realizado por usuário autorizado.

Motivos:

- alunos afastados;
- alunos desligados;
- pendências justificadas;
- erro cadastral;
- avaliações canceladas;
- situações excepcionais.

## RD-CYC-004 — Estados iniciais

```text
DRAFT
SCHEDULED
OPEN
CLOSED
PROCESSING
PUBLISHED
ARCHIVED
```

Transições deverão ser controladas pela aplicação.

Exemplo principal:

```text
DRAFT -> SCHEDULED -> OPEN -> CLOSED -> PROCESSING -> PUBLISHED -> ARCHIVED
```

## RD-CYC-005 — Ciclos formativos adicionais

O sistema poderá ser tecnicamente capaz de criar ciclos adicionais de acompanhamento.

Entretanto, a classificação desses ciclos como avaliações atitudinais oficiais dependerá da regulamentação aplicável.

---

# 5. Participantes do ciclo

## RD-PAR-001 — Participantes deverão ser identificados no contexto do ciclo

O sistema não deverá depender exclusivamente do pelotão atual do usuário para reconstruir avaliações antigas.

O ciclo deverá preservar os participantes e seus vínculos relevantes.

## RD-PAR-002 — Desativação de aluno não apaga avaliações

Se um aluno tornar-se inativo durante um ciclo:

- avaliações já realizadas sobre ele continuam válidas;
- avaliações já realizadas por ele continuam válidas;
- o usuário permanece no histórico;
- o cadastro passa a indicar que está inativo.

## RD-PAR-003 — Pendências de usuário inativo exigem decisão administrativa

Avaliações ainda pendentes envolvendo um aluno que se tornou inativo não deverão impedir indefinidamente o fechamento do ciclo.

O administrador poderá cancelar as pendências aplicáveis, preservando justificativa e auditoria.

---

# 6. Avaliação lateral — PEER

## RD-PEER-001 — Aluno avalia todos os demais alunos do seu pelotão

Ao gerar as atribuições de um ciclo lateral, cada aluno participante deverá avaliar todos os outros alunos participantes do mesmo pelotão.

Para um pelotão com `N` alunos, cada aluno receberá:

```text
N - 1
```

avaliações laterais.

Quantidade total de relações PEER:

```text
N x (N - 1)
```

## RD-PEER-002 — Autoavaliação não é avaliação lateral

É proibida uma avaliação `PEER` em que:

```text
evaluator_id == evaluatee_id
```

## RD-PEER-003 — Não pode existir duplicidade

Para um mesmo ciclo, deverá existir no máximo uma avaliação PEER válida para a combinação:

```text
cycle_id
evaluator_id
evaluatee_id
type = PEER
```

Essa regra deverá possuir proteção no banco de dados, além da validação na aplicação.

## RD-PEER-004 — Identidade do avaliador não é exibida ao aluno avaliado

O aluno deverá receber apenas dados laterais consolidados.

Não deverá visualizar:

- nota individual atribuída por determinado colega;
- comentário bruto escrito por determinado colega;
- identidade associada a um comentário.

## RD-PEER-005 — Instrutor pode acessar autoria

Instrutores autorizados do pelotão poderão visualizar:

- avaliações individuais;
- comentários originais;
- identidade do aluno avaliador.

Esse acesso deverá ser auditável.

## RD-PEER-006 — Resultados apresentados ao aluno devem ser agregados

Exemplo:

```text
Média dos pares em Cooperação: 7,842
```

e não:

```text
Aluno A: 8,000
Aluno B: 6,500
Aluno C: 9,025
```

## RD-PEER-007 — Proteção contra inferência

O sistema deverá prever um número mínimo de avaliações laterais válidas antes de divulgar determinados indicadores agregados ao aluno.

O número mínimo ainda será definido.

---

# 7. Autoavaliação — SELF

## RD-SELF-001 — Uma autoavaliação por aluno por ciclo

Para cada ciclo em que SELF estiver habilitado, cada aluno participante poderá possuir somente uma autoavaliação válida.

## RD-SELF-002 — Avaliador e avaliado são a mesma pessoa

Uma avaliação SELF exige:

```text
evaluator_id == evaluatee_id
```

## RD-SELF-003 — Autoavaliação deve utilizar os mesmos atributos comparáveis

Para permitir análises SELF x PEER, a autoavaliação deverá utilizar a mesma versão do conjunto de atributos utilizada na avaliação lateral daquele ciclo.

---

# 8. Avaliação vertical — VERTICAL

## RD-VERT-001 — Pode haver mais de um instrutor por pelotão

Vários instrutores podem realizar avaliações verticais dos alunos do mesmo pelotão.

## RD-VERT-002 — Um aluno pode receber várias avaliações verticais no mesmo ciclo

A unicidade da avaliação vertical deverá considerar, no mínimo:

```text
cycle_id
instructor_id
student_id
type = VERTICAL
```

Dois instrutores diferentes poderão avaliar o mesmo aluno no mesmo ciclo.

## RD-VERT-003 — Instrutor só avalia dentro do seu escopo

Um instrutor só poderá realizar avaliação vertical de alunos pertencentes ao seu pelotão no contexto aplicável ao ciclo.

## RD-VERT-004 — Participação de instrutores deve ser explícita

O sistema deverá gerar ou registrar `EvaluationAssignments`.

Assim, o fato de um instrutor pertencer ao pelotão não obrigará implicitamente que toda regra futura dependa dessa associação.

O ciclo poderá definir quais instrutores participarão da avaliação vertical.

---

# 9. Atribuição de avaliações

## RD-ASG-001 — Avaliação nasce de uma atribuição

Sempre que possível, a aplicação deverá distinguir:

```text
EvaluationAssignment
```

de:

```text
Evaluation
```

A atribuição representa a obrigação de avaliar.

A avaliação representa o conteúdo preenchido.

## RD-ASG-002 — Estados da atribuição/avaliação

Estados mínimos:

```text
ASSIGNED
IN_PROGRESS
SUBMITTED
CANCELLED
LOCKED
```

## RD-ASG-003 — SUBMITTED não significa imutável enquanto o ciclo estiver aberto

No SISADA, a submissão representa que o avaliador considera o preenchimento concluído.

Entretanto, enquanto o ciclo permanecer `OPEN`, o próprio avaliador poderá voltar e editar sua avaliação.

Ao fechar o ciclo, a avaliação passa a `LOCKED`.

## RD-ASG-004 — Edição antes do fechamento sobrescreve o estado corrente

Se uma avaliação já submetida for editada pelo próprio avaliador enquanto o ciclo estiver `OPEN`, o estado corrente poderá ser sobrescrito.

Não será mantido histórico completo de valores anteriores nesta primeira versão.

O registro deverá manter ao menos:

- `created_at`;
- `updated_at`;
- `submitted_at`.

Depois de `CLOSED`, a edição normal será proibida.

---

# 10. Rascunhos

## RD-DRF-001 — Avaliação pode ser salva parcialmente

Enquanto `OPEN`, o avaliador poderá salvar avaliação como rascunho.

## RD-DRF-002 — Rascunho não conta como avaliação concluída

Somente avaliações com status `SUBMITTED` deverão integrar o percentual de conclusão.

## RD-DRF-003 — Rascunho não entra em analytics

Notas e observações de avaliações ainda não submetidas não deverão entrar em médias, relatórios ou indicadores.

---

# 11. Atributos e notas

## RD-SCR-001 — Escala

A escala inicial será:

```text
0,000 a 10,000
```

## RD-SCR-002 — Precisão

Notas poderão possuir até três casas decimais.

Exemplos válidos:

```text
7
7,5
7,842
10,000
0,000
```

Exemplos inválidos:

```text
-1
10,001
7,8421
```

## RD-SCR-003 — Não utilizar ponto flutuante para persistência de nota

No banco, valores deverão ser armazenados como tipo decimal/numeric apropriado e protegidos por constraint:

```text
0 <= score <= 10
```

A definição exata será feita na modelagem de dados.

## RD-SCR-004 — Atributos são configuráveis

Os seis atributos iniciais são:

- Apresentação;
- Cooperação;
- Coragem;
- Persistência;
- Equilíbrio Emocional;
- Zelo.

Eles não deverão ser colunas fixas da tabela `Evaluation`.

## RD-SCR-005 — Versão dos critérios

O sistema deverá preservar qual conjunto/versão de atributos foi utilizado em cada ciclo.

Alterações futuras em descrição ou critérios de um atributo não podem modificar retroativamente o significado de avaliações antigas.

---

# 12. Observações positivas e negativas

## RD-OBS-001 — Tipos

Observações iniciais:

```text
POSITIVE
NEGATIVE
```

## RD-OBS-002 — Observações são opcionais

A avaliação possuirá dois campos independentes:

```text
positive_observation
negative_observation
```

Nenhum deles será obrigatório para submissão.

Essa decisão evita induzir o avaliador a registrar um fato inexistente apenas para satisfazer uma validação do formulário.

## RD-OBS-003 — Campos vazios são semanticamente válidos

A ausência de texto positivo ou negativo significa apenas que o avaliador não registrou fato daquele tipo naquela avaliação.

O sistema não deverá interpretar campo vazio como avaliação positiva, negativa ou neutra.

## RD-OBS-004 — Observação deve descrever fato

A interface e as orientações deverão incentivar registros factuais/contextualizados e desencorajar rótulos pessoais.

Preferível:

```text
"Durante a atividade X, assumiu a organização do grupo após a ausência do chefe."
```

Evitar:

```text
"É excelente."
```

---

# 13. Exibição dos resultados

## RD-RES-001 — Separar fontes de avaliação

Enquanto a norma específica não definir a composição oficial, o sistema deverá manter separados:

```text
SELF
PEER
VERTICAL
```

Não será criada uma média oficial única misturando os três tipos sem regra normativa definida.

## RD-RES-002 — Aluno visualiza os próprios resultados autorizados

O aluno poderá visualizar, após publicação:

- média dos pares por atributo;
- autoavaliação;
- indicadores comparativos permitidos;
- evolução histórica permitida;
- relatório textual aprovado.

## RD-RES-003 — Comentários brutos não são exibidos ao aluno

O aluno não terá acesso direto aos textos originais dos pares.

## RD-RES-004 — Instrutor possui visão detalhada

Instrutores autorizados poderão consultar as avaliações e observações individuais dos alunos de seu escopo.

---

# 14. Analytics SELF x PEER

## RD-ANA-001 — Média dos pares por atributo

Para cada aluno, atributo e ciclo:

```text
peer_mean(attribute)
```

será calculada utilizando apenas avaliações PEER:

- válidas;
- submetidas;
- não canceladas.

## RD-ANA-002 — Gap por atributo

```text
gap_i = self_score_i - peer_mean_i
```

Interpretação matemática:

- positivo: autoavaliação maior que média dos pares;
- negativo: autoavaliação menor que média dos pares;
- zero: igualdade.

O gap não será automaticamente interpretado como bom ou ruim.

## RD-ANA-003 — Distância Euclidiana

Se:

```text
A = vetor SELF
P = vetor das médias PEER
```

então:

```text
distance(A,P) = sqrt(sum((Ai - Pi)^2))
```

## RD-ANA-004 — Mesmos atributos

A distância somente poderá ser calculada quando os dois vetores corresponderem ao mesmo conjunto de atributos do ciclo.

## RD-ANA-005 — Distância não altera nota oficial

O indicador é analítico e de feedback.

Não poderá alterar automaticamente nota, aprovação, reprovação ou classificação.

## RD-ANA-006 — Histórico

O sistema deverá permitir acompanhar a distância ao longo de ciclos.

## RD-ANA-007 — Faixas interpretativas ainda não definidas

Categorias como:

```text
ALINHADO
LEVE DIVERGÊNCIA
DIVERGÊNCIA
FORTE DIVERGÊNCIA
```

não serão implementadas até existir justificativa metodológica/normativa para seus limites.

---

# 15. Inteligência Artificial e relatórios

## RD-AI-001 — IA recebe apenas dados autorizados

O serviço de IA deverá receber somente informações necessárias para gerar a minuta.

## RD-AI-002 — Comentários laterais serão consolidados

Os comentários brutos poderão ser utilizados como fonte para elaboração da minuta, mas não serão mostrados diretamente ao aluno.

## RD-AI-003 — Função da IA

A IA deverá:

- consolidar fatos;
- padronizar linguagem;
- melhorar redação;
- organizar conteúdo;
- gerar minuta institucional.

## RD-AI-004 — A IA não pode criar evidências

A saída não poderá adicionar fatos não presentes nas observações fornecidas.

## RD-AI-005 — Relatório é uma minuta

Todo conteúdo gerado por IA deverá permanecer com status de minuta até revisão humana.

## RD-AI-006 — Revisão humana obrigatória

Antes de ser disponibilizado ao aluno, o relatório deverá ser revisado e aprovado por usuário autorizado, inicialmente um instrutor.

## RD-AI-007 — Rastreabilidade

A geração deverá futuramente registrar:

- versão do modelo;
- versão do prompt;
- data/hora;
- dados/avaliações de origem;
- responsável pela revisão;
- versão aprovada.

---

# 16. Encerramento e publicação

## RD-CLS-001 — Fechamento bloqueia edição normal

Após `CLOSED`:

- alunos não podem editar SELF;
- alunos não podem editar PEER;
- instrutores não podem editar VERTICAL pelo fluxo normal.

## RD-CLS-002 — Fechamento não significa publicação

Resultados não serão automaticamente disponibilizados aos alunos no momento do fechamento.

Fluxo conceitual:

```text
OPEN
  ↓
CLOSED
  ↓
PROCESSING
  ↓
PUBLISHED
```

## RD-CLS-003 — Reabertura futura

Caso exista necessidade de alteração depois do fechamento, deverá haver fluxo administrativo específico com:

- autorização;
- justificativa;
- auditoria.

A política detalhada será definida posteriormente.

---

# 17. Auditoria

## RD-AUD-001 — Ações críticas devem gerar log

Exemplos:

- fechamento de ciclo;
- reabertura;
- cancelamento de atribuição;
- desativação de aluno;
- alteração de avaliação já submetida;
- consulta de comentário lateral identificado;
- geração de relatório por IA;
- aprovação de relatório.

## RD-AUD-002 — AuditLog não pode ser editado pelo usuário comum

Logs deverão ser tratados como registros de rastreabilidade.

---

# 18. Regras normativas pendentes

Os seguintes pontos permanecem bloqueados até análise da NIDACA/OFOR ou definição normativa equivalente:

1. composição oficial da Nota de Conceito;
2. peso da avaliação vertical;
3. eventual peso da avaliação lateral;
4. eventual papel da autoavaliação no resultado oficial;
5. critérios oficiais dos atributos;
6. periodicidade e classificação oficial dos ciclos;
7. regras formais de divulgação;
8. requisitos específicos de registros de observação;
9. regras específicas de anonimato, se existentes;
10. consequências oficiais de resultados atitudinais.

---

# 19. Pontos de decisão ainda abertos

Antes de finalizar a primeira versão do domínio, ainda será necessário decidir:

### P-001 — Papel múltiplo por usuário

Definir se um mesmo `User` poderá possuir simultaneamente mais de um papel, por exemplo:

```text
INSTRUCTOR + ADMIN
```

A recomendação de arquitetura permanece utilizar relação N:N `User <-> Role`, mas a decisão de produto ainda precisa ser confirmada.

### P-002 — Número mínimo para média lateral

Definir `MIN_PEER_RESPONSES`.

### P-003 — Participação vertical

Regra adotada:

```text
todos os instrutores participantes da unidade no contexto do ciclo
avaliam todos os alunos participantes daquela unidade
```

As `EvaluationAssignments` deverão ser geradas automaticamente a partir do snapshot do ciclo.

### P-004 — Quem aprova relatório de IA

Inicialmente proposto: instrutor do pelotão.

A política final poderá incluir função pedagógica/administrativa.

---

# 20. Invariantes críticas

Estas regras deverão receber proteção forte e testes automatizados:

```text
PEER: evaluator != evaluatee

SELF: evaluator == evaluatee

score >= 0
score <= 10

máximo 3 casas decimais

nenhuma avaliação sem ciclo

nenhuma avaliação duplicada para a mesma atribuição

rascunho não entra em analytics

avaliação CANCELLED não entra em analytics

após CLOSED, edição normal é proibida

mudança de pelotão não altera histórico anterior

aluno nunca recebe identidade do avaliador PEER
```

---

# 21. Próxima etapa

Após revisão deste documento:

```text
01-product-requirements.md  ✅
02-domain-rules.md          ✅ v0.1
03-data-model.md            <- próximo
```

A próxima fase deverá transformar estas regras em:

- entidades;
- primary keys;
- foreign keys;
- cardinalidades;
- constraints;
- índices;
- tabelas associativas;
- histórico de vínculos.

Depois disso será elaborado o diagrama entidade-relacionamento (DER).
