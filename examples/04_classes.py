# examples/04_classes.py
class Expense:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount

    def __repr__(self):
        return f"Expense(title={self.title!r}, amount={self.amount})"

    def summary(self):
        return f"{self.title}: GHS{self.amount:.2f}"

e = Expense("Electric bill", 120.5)
print(e)
print(e.summary())
