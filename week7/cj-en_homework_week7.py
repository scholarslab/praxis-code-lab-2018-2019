class Artist:
    def __init__(self, first_name, last_name, century, expertise):
        self.first_name = first_name
        self.last_name = last_name
        self.century = century
        self.expertise = expertise

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    #check if century exists and if not add it to the list of centuries
    def check_century(self):
        if self.century not in centuries:
            centuries.append(self.century)
        return centuries
        print(centuries)

    def check_expertise(self):
        if self.expertise not in expertises:
            expertises.append(self.expertise)
        return expertises
        print(expertises)

    def return_info(self):
        self_to_dict = {
            "name" : self.first_name + ' ' + self.last_name, "century" : self.century , "expertise" : self.expertise
        }
        return self_to_dict

Vincent = Artist("Vincent van","Gogh","nineteenth century","painting")
Pablo = Artist("Pablo","Picasso", "long nineteenth century","painter and sculptor")
Andy = Artist("Andy","Warhol","twentieth century", "multimedia")
centuries = ["long 19th century","even longer 18th century","Medieval Times","1999"]
expertises = ["painting","sculpture","multimedia","new media"]

Vincent.get_full_name()  
Pablo.get_full_name()
Andy.get_full_name()

Vincent.check_century()
Pablo.check_century()
Andy.check_century()

Pablo.check_expertise()

Andy.return_info()

# try a "manual" way of writing a .txt file:
Vincent_info = Vincent.return_info()
Pablo_info = Pablo.return_info()
Andy_info = Andy.return_info()
input_file = open("artists_info.txt", "w")
input_file.write(str(Vincent_info))
input_file.write(str(Pablo_info))
input_file.write(str(Andy_info))
input_file.close()

# an alternative way (for loop) of writing a .txt file:
input_file = open("artists_info.txt", "w")
for artist in [Vincent, Pablo, Andy]:
    output = str(artist.return_info()) + '\n'
    input_file.write(output)
input_file.close()
