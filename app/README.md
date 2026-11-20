# BungeLens

BungeLens is a Kenyan civic-education application. Its FastAPI backend serves
source-linked parliamentary and Constitution records, uploaded PDFs, lessons,
and optional Gemini-assisted explanations. This guide documents the current
backend API, local setup, data provenance, and known limitations.

## Backend setup

Install dependencies from the repository root:

```powershell
python -m pip install -r backend-requirements.txt
```

Configure these environment variables in the repository-root `.env` file or
in the hosting provider's environment settings:

| Variable | Purpose | Default / behavior |
| --- | --- | --- |
| `DATABASE_URL` | PostgreSQL connection string, including Neon | If unset, SQLite is used |
| `BUNGELENS_DATABASE_PATH` | SQLite file location | `app/data/bungelens.sqlite3` |
| `GEMINI_API_KEY` | Enables AI answers and bill-impact explanations | AI endpoints return `503` if unset |
| `GEMINI_MODEL` | Gemini model name | `gemini-3.8-flash` |
| `BUNGELENS_ALLOWED_ORIGINS` | Comma-separated browser origins allowed by CORS | `http://localhost:5173,http://127.0.0.1:5173` |

Do not commit `.env` or paste secret values into documentation. The API and
record endpoints can run without a Gemini key.

Start the API from the repository root:

```powershell
python -m uvicorn app.main:app --reload
```

FastAPI's interactive documentation is available at
[`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs); the ReDoc view is
at [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc).

### Database

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

Bills, proceedings, articles, documents, and lessons share this table; `kind`
identifies each record type. SQLite is used for local development and tests
when `DATABASE_URL` is unset.

## API reference

The API base URL is `http://127.0.0.1:8000`. JSON collection endpoints return
`{"items": [...], "total": N}` unless otherwise noted. Collection `query`
parameters are optional and limited to 200 characters.

| Method and path | Purpose / response |
| --- | --- |
| `GET /` | API welcome message and status |
| `GET /health` or `GET /api/health` | Health and active database backend |
| `GET /api/home` | Up to four featured documents and document, bill, and proceeding counts |
| `GET /api/documents?query=` | Search/list library documents |
| `POST /api/documents/upload` | Upload and extract a PDF; returns `item` and `totalPages` |
| `POST /api/documents/ask` | Ask a question against an uploaded document or supplied text |
| `GET /api/bills?query=` | Search/list bill metadata |
| `GET /api/bills/{bill_id}` | Get one bill record |
| `GET /api/constitution/articles?query=` | Search/list Constitution sections |
| `GET /api/constitution/articles/{article_id}` | Get one Constitution section |
| `GET /api/constitution/daily` | Return `{"date": "YYYY-MM-DD", "item": ...}` for today's Kenya-time selection |
| `GET /api/proceedings?query=` | Search/list Hansard and proceeding records |
| `GET /api/lessons?query=` | Search/list learning lessons |
| `GET /api/lessons/{lesson_id}` | Get one learning lesson |
| `GET /api/impact/audiences` | Return the supported audience labels |
| `POST /api/impact/analyze` | Generate a source-grounded explanation of a bill for an audience |
| `POST /api/chat` | Ask a general civic question or ask about an uploaded document |
| `POST /api/proceedings/analyze` | Reserved endpoint; currently returns `501` because video analysis is not configured |

The legacy `POST /documents/upload` and `POST /documents/ask` paths are also
available; new clients should use the `/api/...` paths.

### Request examples

Upload a PDF (Windows `curl.exe` example):

```powershell
curl.exe -X POST http://127.0.0.1:8000/api/documents/upload `
  -F "file=@constitution.pdf"
```

Ask a question about an uploaded document:

```json
{
  "question": "What does this document say about access to information?",
  "document_id": "id-returned-by-the-upload-endpoint"
}
```

Ask a general question or request a bill-impact explanation:

```json
{
  "question": "What does Article 48 say about access to justice?"
}
```

```json
{
  "bill_id": "bill-record-id",
  "audience": "Workers"
}
```

Chat questions must contain 1-4,000 characters. Document-question requests may
include `document_text` (up to 1,000,000 characters) instead of `document_id`.
The impact `audience` must be one of `Workers`, `Students`, `Small businesses`,
`Farmers`, or `General citizens`.

### Limits and common errors

| Status | Meaning |
| --- | --- |
| `400` | Invalid request, unsupported upload type, or missing document question input |
| `404` | Requested bill, article, lesson, or uploaded document was not found |
| `409` | A bill record exists but its official bill text is not available for analysis |
| `413` | PDF exceeds 10 MB or extracted text exceeds 1,000,000 characters |
| `422` | Request validation failed or a PDF contains no readable text |
| `501` | Proceeding video transcription/analysis is not configured |
| `502` | Gemini request failed |
| `503` | Gemini is not configured or no verified daily Constitution section is available |

The official-record importer currently stores bill and proceeding metadata
and source links; it does not download and index full bill text. Therefore,
`POST /api/impact/analyze` returns `409` until official bill text is added to
that record.

## Frontend connection

The current client API base is set in `client/src/api.js` to
`http://127.0.0.1:8000/api`. When hosting the client and API separately,
update that base URL and set `BUNGELENS_ALLOWED_ORIGINS` to the client origin.
The Vite development server also defines an `/api` proxy in
`client/vite.config.js`; the current API client uses the absolute base URL.

## Official records and source attribution

Imported parliamentary records retain `sourceUrl`, `sourceName`, and
`sourceListingUrl` fields. Client pages and grounded AI responses use those
record references so readers can open the underlying source.

| Source | Used for |
| --- | --- |
| [National Assembly Bills](https://www.parliament.go.ke/the-national-assembly/house-business/bills) | National Assembly bill listings and bill-PDF links |
| [Senate Bills](https://www.parliament.go.ke/the-senate/house-business/bills) | Senate bill listings and bill-PDF links |
| [National Assembly Hansard](https://www.parliament.go.ke/the-national-assembly/house-business/hansard) | National Assembly Hansard/proceeding records |
| [Senate Hansard](https://www.parliament.go.ke/the-senate/house-business/hansard) | Senate Hansard/proceeding records |
| [National Assembly Committees](https://www.parliament.go.ke/the-national-assembly/committees) | Committee-learning lesson reference |
| [Constitution of Kenya, 2010 (Parliament PDF)](https://www.parliament.go.ke/sites/default/files/2017-05/The_Constitution_of_Kenya_2010.pdf) | Exact English excerpts for seeded Articles 22, 35, 43, 47, 48, and 49 |
| [Kenya Law Constitution page](https://new.kenyalaw.org/akn/ke/act/2010/constitution) | Source link in the Constitution-rights learning lesson |
| [Google Gemini API documentation](https://ai.google.dev/gemini-api/docs) | External AI service used by optional generated explanations |

Refresh official bill and Hansard metadata from Parliament:

```powershell
python -m app.sync_official_data
```

The importer accepts PDF links hosted under the official Parliament domain and
retains YouTube links when they appear with a proceeding. These video links are
references only; this backend does not transcribe or analyze them. The
importer does not invent bill stages, summaries, or constitutional text.

On startup, the backend seeds six Constitution excerpts (Articles 22, 35, 43,
47, 48, and 49) from the Parliament PDF, plus six learning lessons. Seeded
records are inserted only when their IDs are absent, so existing edited
records are not overwritten. The daily endpoint deterministically selects one
section using the current date at UTC+03:00.

The Constitution excerpts shown in the app are English source text. English
and Kiswahili plain-language notes are educational explanations, not official
translations or legal advice. Gemini does not independently browse the web in
this backend: it receives matching stored source text or the explicitly
selected uploaded document, and returned source links point to those records.
