# Python Workflow Scope Demo

This public demo runs `app.py` in the browser with Pyodide. It turns workflow volume, handling time, labor cost, error rate, and implementation cost into a deterministic automation-priority estimate.

[Run the live workflow scope analyzer](https://tinyopsstudio.github.io/python-workflow-scope-demo/).

If the result is promising but the first build step is still unclear, start with the [$19 Quick Workflow Triage](https://tinyopsstudio.com/quick-workflow-triage?utm_source=github&utm_medium=repository&utm_campaign=workflow_scope_demo&utm_content=19_triage). TinyOps Studio returns a written priority, what to skip, and the fastest useful next step.

If the scope is already clear, TinyOps Studio also offers a fixed-scope [$499 business automation build](https://reworkdigital.io/services/i-will-build-one-business-automation-workflow-58/?utm_source=github&utm_medium=repository&utm_campaign=workflow_scope_demo&utm_content=499_build) with written requirements, QA evidence, and handoff. Larger broken or partially shipped workflows can use the [Automation Rescue Sprint](https://tinyopsstudio.com/automation-rescue-sprint?utm_source=github&utm_medium=repository&utm_campaign=workflow_scope_demo&utm_content=rescue_sprint).

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
