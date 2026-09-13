MatchMind
=========

PWA pessoal que analisa automaticamente, todas as madrugadas, os jogos de
futebol das próximas 48h e produz uma análise longa + top 10-15 de apostas
por jogo, com resolução automática (green/red) e calibração de confiança
ao longo do tempo.

Documentação de referência (planner de construção e arquitetura) vive no
projeto "MatchMind" no Claude — este repositório é onde o código e as
notas por stream ficam.

Estrutura
---------

```
matchmind/
  backend/          # FastAPI + coletor + motor de análise
  frontend/         # React + Vite (PWA)
  notas/            # notas de trabalho por stream (um ficheiro por tema)
    concluidas/      # notas fechadas, movidas para aqui
  .github/workflows/ # gatilho do batch noturno (Actions só faz o POST)
```

Estado
------

Fase 0 (fundações e decisões) em curso — ver `notas/limites.md`.
