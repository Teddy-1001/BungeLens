# BungeLens backend

Install the backend dependencies from the repository root:

```powershell
python -m pip install -r backend-requirements.txt
```

Copy `.env.example` to `.env` in the repository root. Set `DATABASE_URL` to
your Neon connection string to use PostgreSQL, and set `GEMINI_API_KEY` to
enable AI answers and bill-impact analysis. The API and record endpoints can
start without the Gemini key; AI requests return a clear service-unavailable
error until it is configured.

The backend creates the PostgreSQL table and index on startup. To create them
manually in the Neon SQL Editor, run:

```sql
CREATE TABLE IF NOT EXISTS civic_records (
    kind TEXT NOT NULL,
    id TEXT NOT NULL,
    payload JSONB NOT NULL,
    text_content TEXT NOT NULL DEFAULT '',
    source_url TEXT NOT NULL DEFAULT '',
    source_name TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL,
    PRIMARY KEY (kind, id)
);

CREATE INDEX IF NOT EXISTS civic_records_kind_updated
    ON civic_records (kind, updated_at DESC);
```

The app stores bills, proceedings, articles, documents, and lessons in this
shared table; `kind` distinguishes the record type. When `DATABASE_URL` is
unset, the backend uses the local SQLite database at
`app/data/bungelens.sqlite3` for development and tests.

Start the API from the repository root:

```powershell
python -m uvicorn app.main:app --reload
```

The SQLite fallback path can be changed with `BUNGELENS_DATABASE_PATH`. The
frontend development server proxies `/api` to `http://127.0.0.1:8000`; set
`VITE_API_BASE_URL` when deploying the frontend separately.

Import or refresh official bill and Hansard records from Parliament of Kenya:

```powershell
python -m app.sync_official_data
```

The importer reads the National Assembly and Senate listing pages, stores
source-linked bill and proceeding metadata, and adds official bill PDFs to the
library. Hansard video links are retained when they appear alongside a record.
Only metadata and source links are imported; no bill stages, summaries, or
constitutional articles are inferred. Full-text analysis requires text to be
available in the backend record.
