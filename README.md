# Doxa

AI analytics layer for **How Southa Are You**.

Doxa reads gameplay data from the existing Neon PostgreSQL database and provides analytics through a FastAPI backend and Svelte frontend.

## Stack

* **Backend:** Python, FastAPI, SQLAlchemy
* **Frontend:** Svelte 5, TypeScript, Tailwind CSS
* **Database:** PostgreSQL (Neon)
* **AI:** Planned

## Architecture

```text
How Southa Are You
        ↓
Spring Boot API
        ↓
Neon PostgreSQL
        ↓
      Doxa
     ↙    ↘
Analytics  AI
     ↓
 Dashboard
```

Doxa is **read-only** and does not modify the How Southa Are You database schema.

## Current Features

### Analytics

* Overview statistics
* Most-played questions
* Hardest questions
* Easiest questions
* Most-missed questions
* Fastest responses
* Slowest responses

### Planned

* Category analytics
* Difficulty analytics
* Activity trends
* AI-powered natural-language insights

## Running Locally

### Backend

```bash
cd backend
source .venv/bin/activate
uv run uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend runs on the Vite development server.

## Screenshot

![Doxa Overview](frontend/assets/homescreen.png)

## Project Status

Doxa is currently in the **core analytics dashboard** stage. Batch 1 is implemented and connected to the real Neon database.
