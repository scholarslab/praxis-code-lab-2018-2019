nameprof = input("Please enter the name or profession of a Canadian to see if they are famous!")

Canadians = {
    "Celine Dion": {
        "name": "Celine Dion",
        "birth year": "1968",
        "death year": "N/A",
        "profession": "performer, goddess"
    },
    "Drake": {
        "name": "Drake",
        "birth year": "1971",
        "death year": "N/A",
        "profession": "performer"
    },
    "Justin Trudeau": {
        "name": "Justin Trudeau",
        "birth year": "1971",
        "death year": "N/A",
        "profession": "Prime Minister, snowboard instructor"
    },
    "Sandra Oh": {
        "name": "Sandra Oh",
        "birth year": "1971",
        "death year": "N/A",
        "profession": "actor, goddess"
    },
    "Nathan Fillion": {
        "name": "Nathan Fillion",
        "birth year": "1971",
        "death year": "N/A",
        "profession": "actor"
    },
    "John A. Macdonald": {
        "name": "John A. Macdonald",
        "birth year": "1815",
        "death year": "1891",
        "profession": "Prime Minister"
    }
}
#output all the information for a person

for name, details in Canadians.items():

    if nameprof in details["profession"]:

        print("name", name)
        print("details", details)

    elif nameprof in details["name"]:

        print("name", name)
        print("details", details)

    else:
        print("That is not a famous Canadian!")
