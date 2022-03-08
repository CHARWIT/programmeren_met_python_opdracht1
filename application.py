import course
import planner
import preparation

def generate_planning():
    prep = preparation.Preparation()
    prep.load_courses_done()
#    print("Courses done loaded!")
    prep.load_courses_offer()
#    print("Courses offered loaded!")
    my_planner = planner.Planner(prep)
    my_planner.compute_current_state()
    my_planner.generate()

generate_planning()
