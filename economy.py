import random
import sys
import matplotlib.pyplot as plt

# person class
class Person:
    def __init__ (self, id, startmoney):
        self.id = id
        self.money = startmoney

    def give_money (self, amount):
        self.money -= amount

    def recieve_money (self, amount):
        self.money += amount

# function to make things easier
def transfer_money (amount, giver, receiver):
    giver.give_money(amount)
    receiver.recieve_money(amount)

# various variables
no_of_people = 1000
startmoney = 10
amount = 1
length = 10000

# people setup
people = []
for i in range(no_of_people):
    people.append(Person(i, startmoney))

# main loop
for i in range(length):
    index_list = list(range(len(people)))
    for person in people:
        if person.money > 0:
            other_person = person
            while other_person == person:
                other_person = people[random.choice(index_list)]
            transfer_money(amount, person, other_person)

    # printing stuff
    sys.stdout.write(str(i) + "\r")
    sys.stdout.flush()

# graphing
people_money = []
for person in people:
    people_money.append(person.money)
people_money.sort()
people_money.reverse()
plt.bar(range(len(people)), people_money)
cur_axes = plt.gca()
cur_axes.axes.get_xaxis().set_ticks([])
cur_axes.axes.get_xaxis().set_ticklabels([])
plt.show()
