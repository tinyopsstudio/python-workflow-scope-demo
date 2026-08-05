import json


def analyze_workflow(data):
    runs_per_month = max(0, int(data.get("runs_per_month", 0)))
    minutes_per_run = max(0.0, float(data.get("minutes_per_run", 0)))
    hourly_cost = max(0.0, float(data.get("hourly_cost", 0)))
    error_rate = min(100.0, max(0.0, float(data.get("error_rate", 0))))
    implementation_cost = max(0.0, float(data.get("implementation_cost", 0)))

    manual_hours_month = runs_per_month * minutes_per_run / 60
    recoverable_hours_year = manual_hours_month * 0.75 * 12
    labor_value_year = recoverable_hours_year * hourly_cost
    preventable_errors_year = runs_per_month * (error_rate / 100) * 0.70 * 12
    monthly_value = labor_value_year / 12
    payback_months = implementation_cost / monthly_value if monthly_value else None

    if labor_value_year >= implementation_cost * 2 and recoverable_hours_year >= 120:
        recommendation = "Prioritize for implementation"
        priority = "high"
    elif labor_value_year >= implementation_cost and recoverable_hours_year >= 60:
        recommendation = "Validate with a short pilot"
        priority = "medium"
    else:
        recommendation = "Keep manual and simplify first"
        priority = "low"

    return {
        "workflow": str(data.get("workflow", "Workflow")).strip() or "Workflow",
        "manual_hours_month": round(manual_hours_month, 1),
        "recoverable_hours_year": round(recoverable_hours_year, 1),
        "labor_value_year": round(labor_value_year, 2),
        "preventable_errors_year": round(preventable_errors_year, 1),
        "payback_months": round(payback_months, 1) if payback_months is not None else None,
        "recommendation": recommendation,
        "priority": priority,
        "assumptions": {
            "time_recovery_rate": 0.75,
            "error_prevention_rate": 0.70,
        },
    }


if __name__ == "__main__":
    example = {
        "workflow": "Invoice intake",
        "runs_per_month": 800,
        "minutes_per_run": 6,
        "hourly_cost": 45,
        "error_rate": 4,
        "implementation_cost": 5000,
    }
    print(json.dumps(analyze_workflow(example), indent=2))
