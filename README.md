# Python Workflow Scope Demo

This public demo runs `app.py` in the browser with Pyodide. It turns workflow volume, handling time, labor cost, error rate, and implementation cost into a deterministic automation-priority estimate.

## Run locally

```bash
python3 -m http.server 8000
```

Open `http://127.0.0.1:8000/` and wait for the Python runtime indicator to turn green.

## Verification

```bash
python3 app.py
```

No form data leaves the browser.
