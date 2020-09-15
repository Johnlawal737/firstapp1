print('Hello world')
for value in range(1,11,2):
    print(value)
    squares=[]
    for value in range(1,6):
        var=value **2
        squares.append(var)
print(squares)
#Dictionary (is key-value relationship)
users={'name':'John',
'age':30,
'State':'Kogi',
'Occupation':'Pilot,Programmer'}
print(users)
users['name']='Ogirima'
print(users['Occupation'])