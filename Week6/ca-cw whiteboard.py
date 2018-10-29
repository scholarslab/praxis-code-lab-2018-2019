print("Welcome to Scholars' Lab! We have people working on the following methods.")
print('method1', 'method2')

method = input("Enter the method you're interested in working with.")

data = {
    'method1': ['name1','name2'],
    'method2': ['name3','name4']
}

if method in data:
    print (data[method])

else:
    print("Nobody does that!")