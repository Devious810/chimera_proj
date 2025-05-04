# Chimera\_Proj

Progetto Python per assistente chimico offline basato su GPT4All e indicizzazione TF‑IDF per ricerca in documenti PDF.

## 📋 Descrizione

Questo progetto offre un'interfaccia a linea di comando per:

* Eseguire risposte predefinite su titolazioni, distillatori, analisi proteine e primo soccorso.
* Ricerca RAG (Retrieval-Augmented Generation) su documenti PDF indicizzati.
* Funzionare interamente offline con il modello **Phi-3-mini-4k-instruct**.

## ⚙️ Requisiti

* Python 3.10+
* \[venv] ambiente virtuale
* Windows PowerShell (o qualsiasi shell Unix-like)

## 🚀 Installazione

1. Clona il repository:

   ```bash
   git clone https://github.com/Devious810/chimera_proj.git
   cd chimera_proj
   ```
2. Crea ed entra nell'ambiente virtuale:

   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1      # Windows PowerShell
   # oppure
   source venv/bin/activate            # Linux/macOS
   ```
3. Installa le dipendenze:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 🎯 Utilizzo

### Avviare l’assistente CLI

* Windows PowerShell:

  ```powershell
  .\run.ps1
  ```
* Linux/macOS o cmd:

  ```bash
  python cli.py
  ```

Segui le istruzioni a schermo per selezionare lingua, opzioni e ricerche.

### Comandi principali

1. **Titolazione base**: spiega passo-passo come fare una titolazione.
2. **Montare un distillatore**: guida al montaggio di un distillatore.
3. **Analisi proteine**: informazioni su analisi proteiche.
4. **Primo soccorso (ferita)**: istruzioni di primo soccorso.
5. **Cerca nei PDF**: ricerca full-text su documenti in `docs/*.pdf`.
6. **Esci**

## 📄 Struttura del progetto

```
├── ask.py                # script di esempio standalone
├── cli.py                # interfaccia a linea di comando
├── index_docs.py         # script per creare indice TF‑IDF da PDF
├── faiss_index.pkl       # indice serializzato
├── docs/                 # documenti PDF per la ricerca
│   └── test.pdf          # PDF di prova
├── prompts/              # directory prompt suddivisi per lingua
│   ├── en/               # prompt in inglese
│   └── it/               # prompt in italiano
├── requirements.txt      # dipendenze del progetto
├── run.ps1               # script PowerShell per avviare CLI
└── run.bat               # script batch Windows per avviare CLI
```

## 🧪 Test

Per verificare rapidamente il funzionamento, esegui:

```bash
python index_docs.py   # indicizza i PDF
python cli.py          # avvia l’assistente
```

## 📝 Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi `LICENSE` per i dettagli.
