import json
from pathlib import Path

data = {
    "user": "Doris",
    "expenses": [
        {"title": "Transport", "amount": 20.0},
        {"title": "Lunch", "amount": 15.5},
        {"title": "Groceries", "amount": 80.25}
    ]
}

p = Path("expenses.json")
p.write_text(json.dumps(data, indent=2))

raw = p.read_text()
loaded = json.loads(raw)
total = sum(item["amount"] for item in loaded["expenses"])
print(f"User: {loaded['user']}")
print(f"Total expenses: GHS{total:2f}")
