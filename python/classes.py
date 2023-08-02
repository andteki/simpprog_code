class Plan:
    def __init__(self, max):
        self.max = max
        self.employees = []

    def add_employee(self, name):
        if not self.open_workplace():
            return False
        self.employees.append(name)
        return True

    def open_workplace(self):
        return self.max - len(self.employees)

uzem1 = Plan(3)

employees = ['Mari', 'Kati', 'Dani', 'Piri']
for emp in employees:
    success = uzem1.add_employee(emp)
    if success:
        print('Siker')
    else:
        print(f'Nem megy: {emp}')

