class Historicalfigures:
    # existing logic goes here
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.century = []
        self.expertises = []
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    def set_century(self, century):
        centuries = ['long 19th century','even longer 18th century', 'Medieval Times', '1999']
        if century in centuries:
            self.century.append(century)
        else:
            pass
    def add_expertises(self, expertises):
        if expertises not in self.expertises:
            self.expertises = self.expertises + expertises
        else:
            pass
    def get_info(self):
        self_to_dict = {
            'full_name': self.first_name +' '+self.last_name, 'expertises': ', '.join(self.expertises), 'century': self.century
        }
        return self_to_dict
    
    # new methods - in order to write the JSON representation of the data to the file:
    def serialize(self, filename):
        import json
        json_string = {"first_name": self.first_name, 
                       "last_name": self.last_name,
                       "full_name": self.get_full_name(),
                       "century":self.century,
                       "expertises":self.expertises}
        with open(filename, "w") as write_file:
            json.dump(json_string, write_file, indent=4)
    # read the file and decode the contents as a JSON string, then overwrite the data 
    # in the instance with the decoded JSON data.
    def deserialize(self, filename):
        import json
        with open(filename, "r") as read_file:
            jt = json.load(read_file)
            self.first_name = jt["first_name"]
            self.last_name = jt["last_name"]
            self.century = jt["century"]
            self.expertises = jt["expertises"]


jane = Historicalfigures('Jane','Austen')
jane.set_century('even longer 18th century')
jane.add_expertises(['writing','gender','sarcasm'])
jane.serialize("jane_austen.json")
jane.deserialize("jane_austen.json")
jane_from_disk = Historicalfigures('','')
jane_from_disk.deserialize("jane_austen.json")
jane_from_disk.get_full_name()
jane_from_disk.expertises
jane_from_disk.get_info()
jane_from_disk.get_full_name()
