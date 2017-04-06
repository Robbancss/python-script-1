import types
import re
import json

dataL = []
updateL = []

class Szamlaadat:
    def __init__(self, idn, name, date, money):
        self.idn = idn
        self.name = name
        self.date = date
        self.money = money
    def addUpdate(self, newmoney, newdate):
        self.money = self.money + newmoney
        self.date = newdate

class Update:
    def __init__(self, idn, name, diff):
        self.idn = idn
        self.name = name
        self.diff = diff

def getPerson(idn, dataL):
    for person in dataL :
        if person.idn == idn :
            return person
    return None

def addPerson(personAdding, dataL):
    i = 0
    for person in dataL:
        if person.idn >= personAdding.idn :
            dataL[i:i] = [personAdding]
            return
        else :
            i = i + 1
    dataL[i:i] = [personAdding]


dataf = open('data.txt','r',encoding='utf-8-sig')
updatef = open('update','r',encoding='utf-8-sig')

for line in dataf:
    lineLength = len(line.split(" "))
    # print("Teljes sor:",line)

    idn = line.split(" ")[0]
    # print("Szamlaszám:",idn)
    name = (re.search('(\D+)\s',line)).group()
    # print("Név:",name,"\n")
    date = line.split(" ")[lineLength-2]
    # print("Dátum:",date)
    money = int(line.split(" ")[lineLength-1])
    # print("Pénz:",money)

    # sz = Szamlaadat(idn,name,date,money)
    dataL.append(Szamlaadat(idn,name,date,money))

for line in updatef:
    lineLength = len(line.split(" "))
    print("Teljes sor",line)
    tmp = line.strip()
    m = re.match("(\d{4}\.\d{2}\.\d{2}\.)",tmp)
    if m:
        newdate = m.group(1)
        print("New date:",newdate)
    else:
        idn = line.split(" ")[0]
        name = (re.search('(\D+)\s',line)).group()
        diff = int(line.split(" ")[lineLength-1])
        updateL.append(Update(idn,name,diff))

for update in updateL:
    person = getPerson(update.idn, dataL)
    if person != None :
        person.addUpdate(update.diff, newdate)
    else : 
        addPerson(Szamlaadat(update.idn, update.name, newdate, int(update.diff)), dataL)


newdataf = open('newdata','w')
i = 0
for person in dataL:
    if i !=0:
        newdataf.write("\n")
    
    print(person.idn, person.name, person.date, int(person.money))
    newdataf.write(person.idn+" "+person.name+" "+person.date+" "+str(person.money))
    i = i + 1
# for person in updateL:
#     print(person.idn, person.name, int(person.diff))
printnewdataf.encoding()
# Closing files
dataf.close()
updatef.close()

print("Closing files")