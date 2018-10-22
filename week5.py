class Fellow:
    # Constructor. Name (in "firstname  lastname" format) and department are self-explanatory. Start_year is the year that the student started grad school.
    def __init__(self, name, department, start_year):
        pass
    # Get the student's name
    def get_name(self):
        return("Brandon Walsh")
    def get_department(self):
        return("English")
    # Returns how many years the fellow has spent in their program (1 = "first year", etc) using the current, actual date. If the fellow has graduated, return how many years it took to graduate.
    def get_year(self):
        return(6)
    # Get the current status of the fellow. Fellows all start as "student", but can eventually become a "graduate". Let's not mention the third possibility.
    def get_status(self):
        return("student")
    # Sets the status of the student to "graduate" and caps get_year at a certain value
    def set_graduate(self, year):
        pass
    # Invent a secret algorithm to based on some combination of the fellow's data (number of vowels in name, heiarchy of departments, etc) to generate a secret rating from 0-10 for a fellow. Be creative.
    def get_rating(self):
        return(10)
    # Return a string representing all the data for a student in as a single row of a CSV file.
    def printout(self):
        return("Brandon Walsh, English, etc, etc, etc")
    # Compare two fellows. If they have all the same data, return true.
    def equals(self,f):
        return(False)
    
    
class Fellowship:
    # Name is the name of the fellowship
    def __init__(self, name):
        pass
    # Audit the program to check that there's been a cohort of 6 students every year and that no person appears multiple times in each cohort. Return True if the fellowship passes, False if it fails.
    def audit(self):
        return(True)
    #Add fellow f to the fellowship in the cohort for year year. 
    def add_fellow(self, f, year):
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

praxis = Fellowship("Praxis")
praxis.add_fellow(Fellow("Brandon Walsh","English",2011), 2012)
print(praxis.get_cohort(2012))
print(praxis.get_cohort_rating(2012))
print(praxis.audit())
# Add more code to test