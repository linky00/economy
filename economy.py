class Person:
    def __init__ (self, startmoney):
        self.money = startmoney

    def give_money (self, amount):
        self.money -= amount

    def recieve_money (self, amount):
        self.money += amount

def transfer_money (amount, giver, receiver):
    giver.give_money(amount)
    receiver.recieve_money(amount)

people = []

for x in range(10):
    people.append(Person(10))
