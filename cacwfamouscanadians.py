query = input("Enter the name or profession you want more info about.")

famouscanadians = {'celebrity1': {'name': 'Céline Dion', 'birth_year':'1968', 'death_year':'', 'profession':['performer','goddess'],'nationality':'Canadien/ne'},'celebrity2': {'name': 'Drake','birth_year':'1986','death_year':'','profession':['performer'],'nationality':'Canadian'},'celebrity3': {'name': 'Justin Trudeau','birth_year':'1971','death_year':'','profession':['Prime Minister','snowboard instructor'],'nationality':'Canadian'},'celebrity4':{'name': 'Sandra Oh','birth_year':'1971','death_year':'','profession':['actor','goddess'],'nationality':'Canadian'},'celebrity5':{'name': 'Nathan Fillion','birth_year':'1971','death_year':'','profession':['actor'],'nationality':'Canadian'},'celebrity6':{'name': 'John A. Macdonald','birth_year':'1815','death_year':'1891','profession':['Prime Minister','colonizer'],'nationality':'Canadian'}}

for key,value in famouscanadians.items():
    if value['name'] == query:
        print(value['name'],value['birth_year'],value['death_year'],value['profession'],value['nationality'])
    elif query in value['profession']:
        print(value['name'],value['birth_year'],value['death_year'],value['profession'],value['nationality'])
if query not in value['name'] or value['profession']:
    print("Nope.")