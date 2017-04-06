#! /usr/bin/python
# -*- coding: utf-8 -*-

import re

class Person:
    "Person class."
    def __init__(self, number, name, date, amount):
        self.number = number
        self.name = name
        self.date = date
        self.amount = amount
    def addUpdate(self, amount, currentdate):
        self.amount = self.amount + amount
        self.date = currentdate

class Update:
    "Update class."
    def __init__(self, number, name, amount):
        self.number = number
        self.name = name
        self.amount = amount

def getPerson(number, people):
    for person in people :
        if person.number == number :
            return person
    return None

def addPerson(personToAdd, people):
    i = 0
    for person in people:
        if person.number >= personToAdd.number :
            people[i:i] = [personToAdd]
            return
        else :
            i = i + 1
    people[i:i] = [personToAdd]


ppl = open("data.txt","r")
upd = open("update")

people = []
updates = []

for line in ppl:
    tmp = line.strip()
    m = re.match("(\d{5}-\d{5})\s(\D+)\s(\d{4}\.\d{2}\.\d{2}\.)\s(\d+)", tmp)
    if m :
        people.append(Person(m.group(1), m.group(2), m.group(3), int(m.group(4))))
   # else :
        #print("Not matching...")

for line in upd:
    tmp = line.strip()
    m = re.match("(\d{4}\.\d{2}\.\d{2}\.)", tmp)
    if m :
        currentdate = m.group(1)
    else :
        m = re.match("(\d{5}-\d{5})\s(\D+)\s(\+\d+|\-\d+)", tmp)
        if m :
            updates.append(Update(m.group(1), m.group(2), int(m.group(3))))

#print "_________BEFORE UPDATE__________"
#for person in people:
    #print person.number, " ", person.name, " ", person.date, " ", person.amount

#print "_________UPDATE__________"
for update in updates:
    person = getPerson(update.number, people)
    if person != None :
        person.addUpdate(update.amount, currentdate)
    else : 
        addPerson(Person(update.number, update.name, currentdate, int(update.amount)), people)

    #print update.number, " ", update.name, " ", update.amount


#print "_________AFTER UPDATE__________"
nwdt = open("newdata", "w")
i = 0
for person in people:
    #print person.number, " ", person.name, " ", person.date, " ", person.amount
    if i != 0 : 
        nwdt.write("\n")

    nwdt.write(person.number+ " "+ person.name+ " "+ person.date+ " "+ str(person.amount))

    i = i + 1


ppl.close()
upd.close()