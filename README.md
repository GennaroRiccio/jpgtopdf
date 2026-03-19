# jpgtopdf

Unisce tutti i file JPG/JPEG contenuti in una cartella in un unico file PDF, rispettando l'ordine alfabetico dei nomi file.

## Requisiti

- Python 3.x
- [Pillow](https://python-pillow.org/)

## Installazione

### Con PowerShell (Windows)

Esegui lo script di setup dalla cartella `src/`:

```powershell
cd src
.\setup_env.ps1
```

Lo script:
- Crea automaticamente un virtual environment `.venv` (se non esiste)
- Attiva il virtual environment
- Installa le dipendenze da `requirements.txt`

### Manuale

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r src\requirements.txt
```

## Utilizzo

```bash
python src/jpg_to_pdf.py <cartella_input> <file_output.pdf>
```

### Esempio

```bash
python src/jpg_to_pdf.py ./immagini output.pdf
```

## Funzionamento

1. Legge tutti i file `.jpg` e `.jpeg` nella cartella indicata
2. Li ordina alfabeticamente per nome
3. Converte ogni immagine in modalità RGB
4. Salva tutte le immagini in un unico file PDF multi-pagina

## Struttura del progetto

```
jpgtopdf/
├── src/
│   ├── jpg_to_pdf.py      # Script principale
│   ├── requirements.txt   # Dipendenze Python (Pillow)
│   └── setup_env.ps1      # Script di setup ambiente (Windows/PowerShell)
└── README.md
```

## Errori comuni

| Situazione | Messaggio | Causa |
|---|---|---|
| Cartella non trovata | `Errore: la cartella '...' non esiste.` | Il percorso indicato non è valido |
| Nessun JPG trovato | `Nessun file JPG trovato in '...'` | La cartella non contiene file `.jpg`/`.jpeg` |
