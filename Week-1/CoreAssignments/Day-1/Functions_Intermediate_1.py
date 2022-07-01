x = [ [5,2,3], [10,8,9] ] 
students = [
  {'first_name':  'Michael', 'last_name' : 'Bryant'},
  {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
  'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
  'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 30} ]

# print(students[0] ['last_name'])


print('------')

#2
students = [
  {'first_name' :  'Michael', 'last_name ' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'},
  {'first_name' : 'Mark', 'last_name' : 'Guillen'},
  {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# print(students[0].items())

def iterateDictionary(name):
  
  for x in range( 0, len(name)):
    temp = ""
    for key,val in students[x].items():
      
      temp += ( f"{key} - {val} " )
    # print(students[0].keys())
    # print(students[0].values())
    # name[x]['first_name'], name[x]['last_name']

    print(temp)

iterateDictionary(students)


print('-----')

students = [
  {'first_name' :  'Michael', 'last_name' : 'Jordan'},
  {'first_name' : 'John', 'last_name' : 'Rosales'},
  {'first_name' : 'Mark', 'last_name' : 'Guillen'},
  {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, some_list):
  for i in range( 0, len(some_list)):
    for key,val in students[i].items():
      if(key == key_name):
        print(key,val)


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

print('---------')

dojo = {
  'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
  for key,val in dojo.items():
    print(len(val), key)
    for i in range( 0, len(val)):
      print(val[i])

printInfo(dojo)

print('-----------')
