# Section class
# - Attributes : section_name, student_list
class Section(object):
    pass

# Student class
# - Attributes : student_id, section, midterm, final, lecture, lab, homework
class Student(object):
    pass
        
#CS101 sections list
section_list = []
section_names = ['A','B','C','D','E','F','G','H','I','J','K','L']
for i in range(len(section_names)):
    sec = Section()
    sec.section_name = section_names[i]
    sec.student_list = []
    section_list.append(sec)
    

#### Read the file ################################################################
#Collect 7 information per one student in the cs101_scoring_simulation.html file, create a new 'Student' instance when '</tr>' tag appears, set all the attributes and add a new instance to the 'student_list' in appropriate section.
rf = open( './cs101_score_simulation.html' )

student_id = 20000000
section = "X"
midterm = 0
final = 0
lecture = 0
lab = 0
homework = 0




rf.close()
####################################################################################




#### Define 2 functions for Section class ############################################
#1. getRatioOfFailed
# - Parameter : Section class instance
# - Return : the ratio of failed student in the section
#2. calculateAverage
# - Parameter : Section class instance, refined(boolean value)
# - Return : the ratio of failed student

def getRatioOfFailed(section):
    pass

def calculateAverage(section, refined):
    pass


####################################################################################







#### Define 2 comparing functions for sorting ########################################
#1. compare by the refined average score of the section
#2. compare by the section name
#Refer to the last page in the 6th lecture slide for details



####################################################################################




#Main loop starts!
command = 1
while 0 < command and  6 > command:
#### Implement all tasks in the menu ###############################################
    command = input("\nWelcome to CS101 Scoring Simulation!\n\n1. View the average score for each section\n2. View the ratio of failed/all for each section\n3. View the refined average score for each section\n4. Sort the section list by the refined average score\n5. Sort the section list by the name\n6. Finish\nSelect the menu : ")
    if command == 1:
        # View the average score for each section
        pass
    elif command == 2:
        # View the ratio of failed/all for each section
        pass
    elif command == 3:
        # View the refined average score for each section
        pass
    elif command == 4:
        # Sort the section list by the refined average score
        pass
    elif command == 5:
        # Sort the section list by the name
        pass
    else:
        print "Bye!"
####################################################################################