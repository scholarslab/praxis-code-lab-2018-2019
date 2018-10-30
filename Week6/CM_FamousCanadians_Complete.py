# create a dictionary:
famous_canadians = {
    'canadian_1': {
        'name':'Celine Dion',
        'year_born':1968,
        'year_died':None,
        'professions':['performer', 'goddess']
    },
    'canadian_2': {
        'name':'Drake',
        'year_born':1986,
        'year_died':None,
        'professions':['performer']
    },
    'canadian_3': {
        'name':'Justin Trudeau',
        'year_born':1971,
        'professions':['Prime Minister', 'snowboard instructor']
    },
    'canadian_4': {
        'name':'Justin Trudeau',
        'year_born':1971,
        'year_died':None,
        'professions':['actor', 'goddess']
    },
    'canadian_5': {
        'name':'Nathan Fillion',
        'year_born':1971,
        'year_died':None,
        'professions':['actor']
    },
    'canadian_6': {
        'name':'John A. Macdonald',
        'year_born':1815,
        'year_died':1891,
        'professions':['Prime Minister']
    },
}

professions = input('Enter the profession of your interested Canadian: ')

def search(myDict, lookup):
    for key, value in myDict.items():
        for v in value['professions']:
            if lookup in v:
                print('key', key)
                print('value', value)

print(search(famous_canadians, professions))


# add key value to the existing dictionary "famous_canadians"):
# actually, its task is "Add element to a Nested Dictionary":
famous_canadians['canadian_1']['nationality'] = 'Canadian'
famous_canadians['canadian_2']['nationality'] = 'Canadian'
famous_canadians['canadian_3']['nationality'] = 'Canadian'
famous_canadians['canadian_4']['nationality'] = 'Canadian'
famous_canadians['canadian_5']['nationality'] = 'Canadian'
famous_canadians['canadian_6']['nationality'] = 'Canadian'
print(famous_canadians)