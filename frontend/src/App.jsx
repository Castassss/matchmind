import { useState, useEffect } from 'react'

function App() {
  const [backendStatus, setBackendStatus] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    checkBackend()
  }, [])

  const checkBackend = async () => {
    try {
      setLoading(true)
      const backendUrl = 'https://matchmind-backend-9f24.onrender.com'
      const response = await fetch(`${backendUrl}/health`)

      if (response.ok) {
        const data = await response.json()
        setBackendStatus(data)
      } else {
        setError(`Backend respondeu com status ${response.status}`)
      }
    } catch (err) {
      setError(`Erro ao conectar com backend: ${err.message}`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header>
        <h1>🎯 MatchMind</h1>
        <p>Análise de Apostas Desportivas com IA</p>
      </header>

      <main>
        <section className="status-box">
          <h2>Status do Sistema</h2>

          {loading && <p className="loading">⏳ Verificando conexão...</p>}

          {error && <p className="error">❌ {error}</p>}

          {backendStatus && (
            <div className="status-ok">
              <p className="check">✅ Backend conectado</p>
              <pre>{JSON.stringify(backendStatus, null, 2)}</pre>
            </div>
          )}

          <button onClick={checkBackend} className="btn-refresh">
            🔄 Verificar de novo
          </button>
        </section>

        <section className="info-box">
          <h2>Fase 0 — Fundações</h2>
          <ul>
            <li>✅ Backend (Render) — Deployado</li>
            <li>✅ Frontend (Vercel) — Deployado</li>
            <li>✅ Database (Supabase) — Configurada</li>
            <li>⏳ Próximos passos — Fase 1 (APIs)</li>
          </ul>
        </section>
      </main>

      <footer>
        <p>MatchMind v0.1.0 — Desenvolvido com React + Vite</p>
      </footer>
    </div>
  )
}

export default App
