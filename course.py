import datetime

def create_course(courseinfo):
    newcourse = Course(courseinfo['code'], courseinfo['naam'],
                courseinfo['sbu'], courseinfo['startdatum'],
                courseinfo['einddatum'])
    newcourse.add_required_courses(courseinfo['voorkennisverplicht'])
    newcourse.add_desired_courses(courseinfo['voorkennisgewenst'])
    newcourse.add_exams(courseinfo['tentamens'])
    return newcourse

# functions for lists of courses
def print_courses(courselist):
    """ Function which prints a list of objects of the Course class"""
    for course in courselist:
        print(course)

def determine_courses_to_do(availablecourses, coursesdone):
    """ Function that determines which courses are not yet done 
        based on available courses and courses allready done
        :returns list with courses not done yet
    """
    coursestodo = [x for x in availablecourses if x.get_code() not in coursesdone]
    return coursestodo


def determine_required_pre_knowledge_not_done(coursestodo, coursesdone):
    """ Function that determines which courses of the required preknowledge are not done yet """
    allrequiredcodes = []
    for x in coursestodo:
        for y in x.get_required_courses():
            if y not in allrequiredcodes:
                allrequiredcodes.append(y)
    requirednotdone = [z for z in allrequiredcodes if z not in coursesdone]
    return requirednotdone

def determine_desired_knowledge_not_done(coursestodo, coursesdone):
    """ Function that determines which courses of the desired preknowledge are not done yet """
    alldesiredcodes = []
    for x in coursestodo:
        for y in x.get_desired_courses():
            if y not in alldesiredcodes:
                alldesiredcodes.append(y)
    desirednotdone = [z for z in alldesiredcodes if z not in coursesdone]
    return desirednotdone

def required_done (coursesdone, cours):
    """ Return True if all required courses are done """
    return min([c for c in cours.required if cours.required in coursesdone])

def desired_done (coursesdone, cours):
    """ Return True if all desired courses are done """
    return min([c for c in cours.desired if cours.desired in coursesdone])

def determine_possible_courses(coursesdone, coursestodo, requirednotdone, desirednotdone):
    """ Function that determines which courses are possible based on courses done and required or desired preknowledge """
    return [c for c in coursestodo if required_done(cours, coursesdone) and desired_done(cours, coursesdone)]



def determine_variable_courses(possiblecourses):
    """ Function that determines which variable courses could be done
        based on the current pre knowledge
        :returns list of variable courses which could be done
    """
    variablecourses = [x for x in possiblecourses if x.get_fixed_or_variable() == 'variable']
    return variablecourses


def determine_fixed_courses(possiblecourses):
    """ Function that determines which courses with a fixed startdate could be done
        based on the current pre knowledge
        :returns list of fixed date courses which could be done
    """
    fixedcourses = [x for x in possiblecourses if x.get_fixed_or_variable() == 'fixed']
    return fixedcourses





class Start_and_enddate:
    """ Class for objects with a startdate and an enddate """
    def __init__(self, startdate=None, enddate=None):
        self.startdate = None
        self.enddate = None
        if startdate:
            self.startdate = datetime.date.fromisoformat(startdate)
        if enddate:
            self.enddate = datetime.date.fromisoformat(enddate)

    def __str__(self):
        """ String representation
        no startdate and enddate: returns variable
        otherwise: returns startdate,  enddate """
        if self.nodates():
            return 'variable'
        return str(self.startdate) + ', ' + str(self.enddate)

    def nodates(self):
        """ true when there is no startdate and no enddate """
        return (not self.startdate) and (not self.enddate)

    def nostartdate(self):
        """ true when there is no startdate  """
        return (not self.startdate)

    def quartile(self):
        """ Compute quartile
        startdate in month 9: return 1
        startdate in month 11: return 2
        startdate in month 2: return 3
        startdate in month 4: return 4
        otherwise: return -1
        """
        if self.startdate.month == 9:
            quartile = 1
        elif self.startdate.month == 11:
            quartile = 2
        elif self.startdate.month == 2:
            quartile = 3
        elif self.startdate.month == 4:
            quartile = 4
        else:
            quartile = -1
        return quartile


class Course:
    # TODO: implement and extend with attributes and methods

    def __init__(self, code, title, sbu, startdate=None, enddate=None):
        # TODO: implement
        self.code = code
        self.title = title
        self.sbu = sbu
        self.dates = Start_and_enddate(startdate, enddate)
        if self.dates.nostartdate():   # not so pretty, but no month attribute when empty
            self.period = -1
        else:
            self.period = self.dates.quartile()
        self.requiredcourses = []
        self.desiredcourses = []
        self.exams = []

    def get_fixed_or_variable(self):
        """ method to to determine if course is vast or variabel
            :returns variabel when there is no startdate, else vast
        """
        if self.dates.nostartdate():
            return ('variable')
        else:
            return('fixed')

    def get_quartile(self):
        """ method to to determine what the quartile of the startdate of the course is
            :returs period, period for the quartile is already determined in the init function
        """
        return self.period

    def get_code(self):
        """ returns course code """
        return self.code

    def get_required_courses(self):
        """ returns the required courses (pre knowledge) for the current course """
        return self.requiredcourses

    def get_desired_courses(self):
        """ returns the desired courses (pre knowledge) for the current course """
        return self.desiredcourses


    def add_required_courses(self, verplichtevoorkennis):
        """ method to add required courses for current course"""
        self.requiredcourses = verplichtevoorkennis

    def add_desired_courses(self, gewenstevoorkennis):
        """ method to add desired courses for current course"""
        self.desiredcourses = gewenstevoorkennis

    def add_exams(self, tentamendata):
        """ method to add exam dates to current course """
        self.exams = tentamendata

    def __str__(self):
        """ string with:
        - code,
        - title,
        - period,
        - new line
        - codes of required foreknowledge or 'geen verplichte voorkennis'
        - new line
        - codes of desired foreknowledge or 'geen gewenste voorkennis'
        - new line
        """
        return str(self.code) + ', ' + str(self.title) + ', ' + str(self.period) + '\n' + str(self.requiredcourses or 'geen verplichte voorkennis') + '\n' + str(self.desiredcourses or 'geen gewenste voorkennis') + '\n'

