import random

class Person:
    def __init__ (self, id, startmoney):
        self.id = id
        self.money = startmoney

    def give_money (self, amount):
        self.money -= amount

    def recieve_money (self, amount):
        self.money += amount

    def you_need_money_to_live (self):
        return self.money < 0

def transfer_money (amount, giver, receiver):
    giver.give_money(amount)
    receiver.recieve_money(amount)

no_of_people = 100
startmoney = 10
amount = 1
length = 1000

people = []
for i in range(no_of_people):
    people.append(Person(i, startmoney))

for i in range(length):
    index_list = list(range(len(people)))
    for person in people:
        other_person = person
        while other_person == person:
            other_person = people[random.choice(index_list)]
        transfer_money(amount, person, other_person)

    for person in people:
        if person.you_need_money_to_live():
            people.remove(person)

    if i % 100 == 0 or i == length - 1:
        print("Round " + str(i) + " outcome:")
        for person in people:
            print("ID " + str(person.id) + " has " + str(person.money))
        print("---")
