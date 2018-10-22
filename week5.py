class Fellow:
    # Constructor. Name (in "firstname  lastname" format) and department are self-explanatory. 
    # start_year_g is the year that the student started grad school;
    # start_year_f is the year that the student started Praxis Fellowship;
    # status is the student current status: "student" or "graduate".
    def __init__(self, name, department, start_year_g, start_year_f, status):
        self.name = name
        self.department = department
        self.start_year_g = start_year_g
        self.start_year_f = start_year_f
        self.status = status
        pass
    # Get the student's name
    def get_name(self):
        print(self.name)
    def get_department(self):
        print(self.department)
    # get the student's start year of the graudate school:
    def get_year_graduate_school(self):
        print(self.start_year_g)
    # get the student's start year of the praxis fellowship:
    def get_year_fellowship(self):
        print(self.start_year_f)
    # Get the current status of the fellow. 
    def get_status(self):
        print(self.status)
    # Sets the status of the student to "graduate" and caps get_year_graduate_school at a certain value
    def set_graduate(self, year):
        if self.start_year_g <= 2018 - year:
            print("graduate")
        else:
            print("current student")
        pass
    # Return a string representing all the data for a student in as a single row of a CSV file.
    def printout(self):
        print(self.name + ", " + self.department + ", " + "start year of graduate school in " + str(self.start_year_g) + ", start year of Praxis fellowship in " + str(self.start_year_f) + ", " + self.status)
    # Compare two fellows. If they have all the same data, return true.
    def equals(self,f):
        if self.name == f.name and self.department == f.department and self.start_year_g == f.start_year_g and self.start_year_f==f.start_year_f and self.status==f.status:
            return True
        else:
            return False

# Input our sample data (only 3 fellows) for Fellow class:
p1 = Fellow("Alex Gil", "English", 2010, 2011, "graduate")
p2 = Fellow("Brooke Lestock", "English", 2010, 2011, "graduate")
p3 = Fellow("Lindsay O’Connor", "English", 2010, 2011, "graduate")

# Test some functions above:
p1.get_name()
p1.get_department()
p1.get_year_graduate_school()
p1.get_year_fellowship()
p1.get_status()
p1.set_graduate(5)
p1.printout()
p1.equals(p2)

    
class Fellowship:
    # Name is the name of the fellowship
    self.fellows = {}

    def __init__(self, name):
        self.name = name
        pass
    # Audit the program to check that there's been a cohort of 6 students every year
    # and that no person appears multiple times in each cohort.
    # Return True if the fellowship passes, False if it fails.
    def audit(self):
        if len() == 6
            return (True)
        else
            return(False)
    #Add fellow f to the fellowship in the cohort for year year. 
    def add_fellow(self, f, year):
        if year in self.fellows:
            self.fellows[year].append(f)
        else:
            self.fellows[year] = []
            self.fellows[year].append(f)
        pass
    # Return all the fellows for a particular year's cohort in a list. Figure out what to return if the cohort doesn't exist.
    def get_cohort(self, year):
        return([])
    # Return the total rating for a cohort (add up all the students' individual ratings)
    def get_cohort_rating(self,year):
        return(9)
    # Return the best cohort or cohorts
    def get_best_cohort(self):
        return([2012])
    # Return the cohort or cohorts with fellows from the most number of departments
    def get_most_diverse(self):
        return([2012])
    # Return the cohort or cohorts with fellows from the least number of departments
    def get_most_diverse(self):
        return([2011])
    # Return the department whose students are most frequently chosen
    def get_top_department(self):
        return("Music")
    # Write the data for all the students to a CSV file using the filename parameter
    def write_to_file(self,filename):
        pass
