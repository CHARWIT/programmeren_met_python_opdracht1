import course


class Planner:
    """ Class for planning objects based on the status of the cources"""
    # TODO: implement and add attributes

    def __init__(self, preparation):
        self.coursesdone = preparation.done_codes
        print("Planner - courses done:", len(self.coursesdone))
        self.availablecourses = preparation.available_courses
        print("Planner - number of available courses:", len(self.availablecourses))
        #course.print_courses(self.availablecourses)

    # TODO: implement

    def compute_current_state(self):
        print('Function compute_current_state called')
        self.coursestodo = course.determine_courses_to_do(self.availablecourses,self.coursesdone)
        print("Courses to do:", self.coursestodo)
        #print("Nr of courses to do:",len(self.coursestodo))
        self.requirednotdone =  course.determine_required_pre_knowledge_not_done(self.coursestodo,self.coursesdone)
        print("Required pre knowledge not yet done:",self.requirednotdone)
        self.desirednotdone =  course.determine_desired_knowledge_not_done(self.coursestodo,self.coursesdone)
        print("Desired pre knowledge not yet done:",self.desirednotdone)

        self.possiblecourses = course.determine_possible_courses(self.coursestodo, self.coursesdone)
        print("Possible courses based on preknowledge:", self.possiblecourses)

    # TODO: implement

    def choose_course(self, quartile):
        """
        :param quartile: int that shows the quartile
        """
        print('Function choose_course called')

    # TODO: implement

    def generate_for_quartile(self, quartile):
        """
       :param quartile: int that shows the quartile
       :return: string for this quartile
        """
        self.compute_current_state()
        print('Function generate_for_quartile called')

    # TODO: implement

    def generate(self):
        """
        :return: string showing the planning
        """
        self.generate_for_quartile(1)
