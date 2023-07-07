def splitPeople(s):
    upperString = str.upper(s)
    return str.split(upperString, ';')

def toNameAndSurname(s):
    people = splitPeople(s)
    return tuple([str.split(person, ":") for person in people])

def sortNamesAndSurnames(s):
    people = toNameAndSurname(s)
    return tuple(sorted(people, key=lambda x: (x[1], x[0])))

def changeOrder(s):
    tuples = sortNamesAndSurnames(s)
    tuples = [(t[1], t[0]) for t in tuples]
    res = "(" + ")(".join([f"{name}, {surname}" for (name, surname) in tuples]) + ")"
    return res

s= "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

print(changeOrder(s))