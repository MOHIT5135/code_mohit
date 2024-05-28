#concatenation 
a = "Mohit"
b = "Kumar"
c = a + b
print(c)

#lower_case
a = "MOHIT"
print(a.lower())

#length of string
print(len(a))

#white space removel left side
st = "  hello LIET  "
print(st)
print(st.lstrip())

#diff b/w insert() and append()

#insert()
animals =["lion","tiger","bear","elephant","fox"]
animals[1] = "deer"
print(animals)

#append()
animals =["lion","tiger","bear","elephant","fox"]
animals.append("deer")
print(animals)

#list within list
animals =["lion","tiger","bear","elephant","fox",["apple","kiwi","banana","litchi"]]
animals = animals[5][1]
print(animals)