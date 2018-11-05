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

hildie = historical_figures('Hildegard','Von Bingen')
hildie.set_century('Medieval Times')
hildie.add_expertises(['Jesus','music','science','languages'])
print(hildie.get_info())

jane = historical_figures('Jane','Austen')
jane.set_century('even longer 18th century')
jane.add_expertises(['writing','gender','sarcasm'])
print(jane.get_info())

marx = historical_figures('Karl','Marx')
marx.set_century('long 19th century')
marx.add_expertises(['economics','persuasion'])
print(marx.get_info())

f = open('historical_figures_results.txt','w')
with open('historical_figures_results.txt','w') as file:
    file.write(str(hildie.get_info()))
    file.write(str(jane.get_info()))
    file.write(str(marx.get_info()))