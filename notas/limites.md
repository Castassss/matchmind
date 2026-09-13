# Limites reais dos serviços — Fase 0

> Confirmado por pesquisa em 13/09/2026. Estes números mudam com frequência —
> revalida antes de dimensionar a fila da fase 4, especialmente o Gemini.

## API-Football — plano Pro ($19/mês)

- **7.500 chamadas/dia**
- **300 chamadas/minuto** (ou 5/segundo)
- Fonte: [api-football.com/pricing](https://www.api-football.com/pricing),
  [How ratelimit works](https://www.api-football.com/news/post/how-ratelimit-works)

Confronta com o orçamento do planner (fase 2): MVP ~160 chamadas/dia,
escala completa ~2.800/dia. Folga confortável nas duas contas — 7.500/dia
e 300/min não é limitador a este volume.

## Gemini — free tier

- **Confirmado em 13/09/2026** no dashboard pessoal em Google AI Studio →
  Rate Limits (a Google já não publica números fixos na documentação
  pública — variam por conta/tier).
  Fonte: [ai.google.dev/gemini-api/docs/rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- **Modelo:** `gemini-3-flash`
- **RPM (pedidos por minuto):** 5
- **TPM (tokens por minuto):** 250.000
- **RPD (pedidos por dia):** 20

Estes números são o que dimensiona o limitador de ritmo da fase 4 — com
RPD=20, o batch noturno de um MVP com ~20 jogos já esbarra no limite diário
se cada jogo gastar mais de 1 chamada Gemini. A gerir na fase 4 (fila,
retries, ou considerar plano pago se a análise por jogo precisar de mais
do que 1 chamada).

## Supabase — plano Free

- **500 MB** de armazenamento de base de dados por projeto
- Máximo de **2 projetos ativos** gratuitos por conta
- Projetos gratuitos **pausam automaticamente ao fim de 1 semana de
  inatividade** (relevante — o batch noturno diário evita isto na prática)
- Fonte: [supabase.com/pricing](https://supabase.com/pricing)

Confirma a política de retenção de 90 dias (fase 1) mantém isto confortável
mesmo depois de meses de uso — dados brutos (`fixture_data`, `odds`) são o
que cresce; análises/picks/resultados ficam pequenos.

## Decisões a fechar (fase 0)

- [ ] **2 ligas do MVP** — proposta do planner: Liga Portuguesa + La Liga
- [x] **Modelo Gemini predefinido** — `gemini-3-flash`
- [ ] **League IDs e season atual** — obter via `GET /leagues` depois de
      teres a chave API-Football ativa (passo 6 da fase 0)

## Contas e chaves — por fazer manualmente

Nada disto pode ser feito a partir daqui (exige pagamento e/ou login pessoal):

- [x] Criar repositório privado `matchmind` no GitHub e fazer o primeiro push
      desta estrutura
- [x] Conta Supabase — novo projeto
- [ ] Conta Render
- [ ] Conta Vercel
- [ ] Conta UptimeRobot
- [x] Google AI Studio — gerar chave Gemini + anotar rate limits reais (acima)
- [ ] API-Football — subscrever plano Pro **depois** de validar a chave Free
      com uma chamada de teste (armadilha já identificada no planner)
- [ ] Preencher `.env` local a partir de `.env.example` com as chaves reais
      (Supabase e Gemini já feitos — falta API-Football e o segredo do job)
- [ ] Replicar as mesmas variáveis em: Render (env vars), Vercel, GitHub Secrets
- [ ] Fazer uma chamada de teste autenticada ao API-Football e outra ao
      Gemini, do portátil — critério de "pronto" da fase 0
