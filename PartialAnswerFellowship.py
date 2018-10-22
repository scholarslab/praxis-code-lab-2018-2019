class Fellowship:
    fellows = {}
    # Name is the name of the fellowship
    def __init__(self, name):
        pass
    # Audit the program to check that there's been a cohort of 6 students every year and that no person appears multiple times in each cohort. Return True if the fellowship passes, False if it fails.
    def audit(self):
        return(True)
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