
employees = [
    {"name": "Para Béla", "city": "Szeged"},
    {"name": "Erős István", "city": "Szeged"},
    {"name": "Csontos Ferenc", "city": "Szolnok"},
    {"name": "Avas Mária", "city": "Aszód"}
]

employees.sort(key=lambda emp: emp['name'])

print(employees)
