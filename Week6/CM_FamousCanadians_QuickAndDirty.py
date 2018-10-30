name= input("Enter a name: ")

famous_canadians= {'Celine Dion': ['1968', 'performer', 'goddess'], 
'Drake': ['1968', 'performer'], 
'Justin Trudeau': ['1971', 'Prime Minister', 'snowboard instructor'],
'Sandra Oh': ['1971', 'actor', 'goddess'],
'Nathan Fillion': ['1971', 'actor'],
'John A. Macdonald': ['1815', '1891', 'Prime Minister']}

if name in famous_canadians:
    print(famous_canadians[name])
else:
    print("I don't know anything about that person")