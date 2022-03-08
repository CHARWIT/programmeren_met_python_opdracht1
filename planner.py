import course


class Planner:
    """ Class for planning objects based on the status of the cources"""
    # TODO: implement and add attributes

    def __init__(self, preparation):
        self.coursesdone = list(preparation.done_codes)
#        print("Planner - courses done:", self.coursesdone)
        self.availablecourses = preparation.available_courses
#        print("Planner - number of available courses:", len(self.availablecourses))
#        course.print_courses(self.availablecourses)

    def compute_current_state(self):
        self.coursestodo = course.determine_courses_to_do(self.availablecourses,self.coursesdone)
        self.requirednotdone = course.determine_required_pre_knowledge_not_done(self.coursestodo,self.coursesdone)
        self.desirednotdone = course.determine_desired_knowledge_not_done(self.coursestodo,self.coursesdone)
        self.courseswithexam = course.return_courses_with_exam(self.coursestodo)
        self.possiblecourses = course.determine_possible_courses(self.coursestodo, self.coursesdone)
        self.fixedcourses = course.determine_fixed_courses(self.possiblecourses)
        self.variablecourses = course.determine_variable_courses(self.possiblecourses)

#        print("Nr of fixed courses:", len(self.fixedcourses))
#        print("Nr of courses to do:",len(self.coursestodo))
#        print("Required pre knowledge not yet done:" ,self.requirednotdone)
#        print("Desired pre knowledge not yet done:" ,self.desirednotdone)
#        print("Possible courses based on preknowledge:", len(self.possiblecourses))
#        print("Nr of variable courses:", len(self.variablecourses))
#        print(self.variablecourses)

    def choose_course(self, quartile):
        """
        :param quartile: int that shows the quartile
        """
        # Als er prio gegeven kan worden obv regels in opdracht dan komen geprioriteerde courses in prio_list

        #Prio a: mogelijke vaste courses dit kwartaal
        fixed_courses_this_quartile = [x for x in self.fixedcourses if x.get_quartile() == quartile]
        #print(f"number of fixed courses for quartile {quartile} is {len(fixed_courses_this_quartile)}")
        if fixed_courses_this_quartile:
            prio_list = fixed_courses_this_quartile
        else:
            prio_list = self.variablecourses

        #Prio b: courses die waarvan de gewenste voorkennis al aanwezig is
        prioritized_courses = course.prioritize_desired_done(prio_list, self.coursesdone)
        if prioritized_courses:
            prio_list = prioritized_courses
        else:
            prio_list = fixed_courses_this_quartile

        #Prio c: courses die vereiste voorkennis voor andere vakken zijn
        future_required_courses = [course for course in prio_list if course.code in self.requirednotdone]
        if future_required_courses:
            prio_list = future_required_courses
        else:
            prio_list = prio_list

        #Prio d: courses die gewenste voorkennis voor andere vakken zijn
        future_desired_courses = [course for course in prio_list if course.code in self.desirednotdone]
        if future_desired_courses:
            prio_list = future_desired_courses
        else:
            prio_list = prio_list

        #Prio e: vakken die een tentamen hebben
        courses_with_exam = [course for course in prio_list if course in self.courseswithexam]
        if courses_with_exam:
            prio_list = courses_with_exam
        else:
            prio_list = prio_list

        if prio_list:
            print("Te volgen cursus:", prio_list[0])
            self.coursesdone.append(prio_list[0].code)
        else:
            print("Geen geschikte cursus dit kwartiel \n")
    # TODO: implement

    def generate_for_quartile(self, quartile):
        """
       :param quartile: int that shows the quartile
       :return: string for this quartile
        """
        self.compute_current_state()
        self.choose_course(quartile)

    # TODO: implement

    def generate(self):
        """
        :return: string showing the planning
        """
        for q in range (1,5):
            print(f"Kwartiel {q}")
            print(f"Voorkennis: {self.coursesdone}")
            self.generate_for_quartile(q)
