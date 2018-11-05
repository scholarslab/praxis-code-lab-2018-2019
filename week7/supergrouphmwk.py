class historical_figures:
    def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name
       self.century = []
       self.expertises = []
    def get_full_name(self):
        return self.first_name +' '+self.last_name
    def set_century(self, century):
        centuries = ['long 19th century','even longer 18th century', 'Medieval Times', '1999']
        if century in centuries:
            self.century = self.century + century
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

hildie = historical_figures("Hildegard","Von Bingen")
hildie.set_century(['Medieval Times'])
hildie.add_expertises(['Jesus','music','science','languages'])
print(hildie.get_info())
#Use your class to create three historical figures.
#Print out all three figures' information when you run the script.
#Write the historical figures' information to a text file using the python "io" library.