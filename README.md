# ✂ snip — URL Shortener

> A full-stack URL shortener built with FastAPI and SQLAlchemy. Supports custom aliases, expiry dates, and click tracking. Features cryptographically secure short code generation, proper REST API design, and a clean minimal frontend.
>
> Built from scratch as a learning project to transition from tutorial-following to independent backend development.

---

## Features

- Shorten any valid URL instantly
- Custom aliases: use your own short code like `my-brand` instead of a random one
- Expiry dates: set a date after which the link stops working
- Click tracking: see how many times a link has been visited
- Collision-safe short code generation using Python's `secrets` module
- Proper HTTP status codes throughout (`201`, `302`, `404`, `409`, `410`)
- Inline error handling: no crashes, no silent failures
- Clean minimal frontend with a custom date picker and copy-to-clipboard

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend framework | FastAPI |
| Database ORM | SQLAlchemy |
| Database | SQLite |
| Data validation | Pydantic |
| Frontend | HTML, CSS, Vanilla JS |

---

## How It Works

```
User submits a long URL
    → Backend validates it
    → Generates a cryptographically secure 8-character short code
    → Checks for collisions in the database
    → Saves the record and returns the short URL

User visits the short URL
    → Backend looks up the short code
    → Checks if the link has expired
    → Redirects to the original URL (HTTP 302)
    → Increments the click counter
```

---

## Project Structure

```
url_shortener/
├── app/
│   ├── api/v1/endpoints/
│   │   └── url_routers.py    ← API routes and redirect logic
│   ├── core/
│   │   └── utils.py          ← Short code generator
│   ├── db/
│   │   └── database.py       ← Database setup and session management
│   ├── models/
│   │   └── models.py         ← SQLAlchemy database models
│   ├── schemas/
│   │   └── schemas.py        ← Pydantic request/response schemas
│   └── main.py               ← App entry point
├── index.html                ← Frontend
└── requirements.txt
```

---

## Getting Started

> This guide assumes you have **Python 3.10 or higher** installed. Not sure? Run `python --version` in your terminal. If you don't have Python, download it from [python.org](https://python.org).

### Step 1 — Clone the repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/url-shortener-app.git
cd url-shortener-app
```

### Step 2 — Create a virtual environment

A virtual environment keeps your project's dependencies separate from the rest of your system. Think of it as a clean isolated workspace.

```bash
python -m venv venv
```

Now activate it:

**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

You'll know it's active when you see `(venv)` at the start of your terminal line.

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

This installs everything the project needs — FastAPI, SQLAlchemy, uvicorn, and more. It might take a minute.

### Step 4 — Run the backend server

```bash
uvicorn app.main:app --reload
```

You should see something like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

Your backend is now running. Don't close this terminal.

### Step 5 — Open the frontend

Simply open `index.html` in your browser. You can double-click it from your file explorer, or drag it into a browser window.

That's it. The frontend talks directly to your locally running backend.

### Step 6 — Explore the API docs

FastAPI gives you interactive API documentation for free. Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

Here you can test every endpoint directly without needing the frontend.

---

## API Endpoints

| Method | Endpoint | Description | Status Code |
|---|---|---|---|
| `POST` | `/api/v1/urls` | Create a short URL | 201 |
| `GET` | `/{short_code}` | Redirect to original URL | 302 |
| `GET` | `/api/v1/urls/{short_code}` | Get link info and stats | 200 |
| `GET` | `/health` | Health check | 200 |

### Example — Create a short URL

**Request:**
```json
POST /api/v1/urls
{
  "original_url": "https://www.youtube.com",
  "custom_alias": "my-yt",
  "expires_at": "2026-12-31T00:00:00"
}
```

**Response:**
```json
{
  "original_url": "https://www.youtube.com",
  "short_code": "my-yt",
  "created_at": "2026-05-24T07:44:31.873256",
  "expires_at": "2026-12-31T00:00:00",
  "click_count": 0
}
```

---

## What I Learnt

### Backend Architecture
How to separate concerns properly,  models, schemas, services, and routers each have one job. Business logic lives in the service layer, not inside endpoint functions.

### HTTP at a deeper level
The difference between `301` and `302` redirects and why it matters. When to use `404` vs `409` vs `410` and what each one actually communicates to the client.

### SQLAlchemy ORM
How database sessions work, the difference between a model instance and a schema, and why you never expose your raw database IDs in an API response.

### Pydantic Validation
How to use `AnyHttpUrl` for URL validation, `field_validator` for custom rules, and `ConfigDict(from_attributes=True)` to bridge SQLAlchemy models and Pydantic schemas cleanly.

### Security thinking
Why sequential IDs are a security risk, why `secrets` is safer than `random`, and how to think about what information you expose in an API response.

### API Design
What makes a RESTful path clean, how to version an API (`/api/v1/`), and why your redirect endpoint lives at root level while info endpoints live under `/api/v1/`.

### CORS
Why browsers block cross-origin requests and how to configure FastAPI middleware to allow them.

---

## Disclaimer

**Backend** — Written entirely by me in Python using FastAPI and SQLAlchemy. Every design decision, debugging session, and architectural choice was worked through manually.

**Frontend** — The `index.html` file was generated using AI (Claude) based on a detailed specification I wrote describing all the required features, API contract, and design requirements. The integration, testing, and bug fixing was done by me.

---

## Author

Built by Palin Jena.
Feel free to open issues, suggest features, or just say hi.
