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

- A Google **deixou de publicar números fixos de RPM/RPD/TPM** na
  documentação pública; a página de rate limits remete para o dashboard
  pessoal em **Google AI Studio → Rate Limits**, porque os valores variam
  por conta/tier.
  Fonte: [ai.google.dev/gemini-api/docs/rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- **Ação pendente (não posso fazer por ti):** entrar em Google AI Studio com
  a tua conta, abrir a secção de Rate Limits, e anotar aqui os valores reais
  de RPM / RPD / TPM para o modelo escolhido. É esse número que dimensiona
  o limitador de ritmo da fase 4.
- **Modelo predefinido:** por decidir (ver "Decisões a fechar" abaixo) —
  proposta do planner é o *flash* mais recente disponível no free tier.

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
- [ ] **Modelo Gemini predefinido** — proposta: o *flash* mais recente
      disponível no free tier
- [ ] **League IDs e season atual** — obter via `GET /leagues` depois de
      teres a chave API-Football ativa (passo 6 da fase 0)

## Contas e chaves — por fazer manualmente

Nada disto pode ser feito a partir daqui (exige pagamento e/ou login pessoal):

- [ ] Criar repositório privado `matchmind` no GitHub e fazer o primeiro push
      desta estrutura
- [ ] Conta Supabase — novo projeto
- [ ] Conta Render
- [ ] Conta Vercel
- [ ] Conta UptimeRobot
- [ ] Google AI Studio — gerar chave Gemini + anotar rate limits reais (acima)
- [ ] API-Football — subscrever plano Pro **depois** de validar a chave Free
      com uma chamada de teste (armadilha já identificada no planner)
- [ ] Preencher `.env` local a partir de `.env.example` com as chaves reais
- [ ] Replicar as mesmas variáveis em: Render (env vars), Vercel, GitHub Secrets
- [ ] Fazer uma chamada de teste autenticada ao API-Football e outra ao
      Gemini, do portátil — critério de "pronto" da fase 0
