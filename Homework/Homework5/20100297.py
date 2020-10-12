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

for line in rf:
    line = line.strip()
    if "</tr>" in line:
        student = Student()
    
    if "'student_id'" in line:
        student_id = line[line.find("'student_id'")+13 : line.find("</td>")]
    if "'section'" in line:
        section = line[line.find("'section'")+10 : line.find("</td>")]
    if "'midterm'" in line:
        midterm = line[line.find("'midterm'")+10 : line.find("</td>")]
    if "'final'" in line:
        final = line[line.find("'final'")+8 : line.find("</td>")]
    if "'lecture'" in line:
        lecture = line[line.find("'lecture'") + 10 : line.find("</td>")]
    if "'lab'" in line:
        lab = line[line.find("'lab'") + 6 : line.find("</td>")]
    if "'homework'" in line:
        homework = line[line.find("'homework'") + 11 : line.find("</td>")]
        student.student_id = student_id
        student.section = section
        student.midterm = midterm
        student.final = final
        student.lecture = lecture
        student.lab = lab
        student.homework = homework
        for line in section_list:
            if student.section == line.section_name:
                line.student_list.append(student)

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
    num1 = len(section.student_list)
    count = 0
    for i in range(num1):
        total = int(section.student_list[i].lecture)+ int(section.student_list[i].lab)+ int(section.student_list[i].homework)
        if total < 320:
            count += 1
    return float(count)/num1
         

def calculateAverage(section, refined):
    num1 = len(section.student_list)
    count = 0
    total = 0
    if refined == False:
        for i in range(num1):
            total += int(section.student_list[i].midterm) + int(section.student_list[i].final)
        return float(total)/2/num1
    else:
        for i in range(num1):
            t_ta = int(section.student_list[i].lecture)+ int(section.student_list[i].lab)+ int(section.student_list[i].homework)
            if t_ta < 320:
                count += 1
                continue
            total += int(section.student_list[i].midterm) + int(section.student_list[i].final)
        return float(total)/2/(num1 -count)
        
    
####################################################################################







#### Define 2 comparing functions for sorting ########################################
#1. compare by the refined average score of the section
#2. compare by the section name
#Refer to the last page in the 6th lecture slide for details
def compare_refined_average(a1,a2):
    ave1 = calculateAverage(a1, True)
    ave2 = calculateAverage(a2, True)
    return cmp(ave1, ave2)
def compare_name(a1,a2):
    return cmp(a1.section_name,a2.section_name)


####################################################################################




#Main loop starts!
command = 1
while 0 < command and  6 > command:
#### Implement all tasks in the menu ###############################################
    command = input("\nWelcome to CS101 Scoring Simulation!\n\n1. View the average score for each section\n2. View the ratio of failed/all for each section\n3. View the refined average score for each section\n4. Sort the section list by the refined average score\n5. Sort the section list by the name\n6. Finish\nSelect the menu : ")
    if command == 1:
        # View the average score for each section
        for line in section_list:
            print line.section_name, calculateAverage(line, False)
    elif command == 2:
        # View the ratio of failed/all for each section
        for line in section_list:
            print line.section_name, getRatioOfFailed(line)
    elif command == 3:
        # View the refined average score for each section
        for line in section_list:
            print line.section_name, calculateAverage(line, True)
    elif command == 4:
        # Sort the section list by the refined average score
        section_list.sort(compare_refined_average)
        list1 = []
        for line in section_list:
            name = line.section_name
            list1.append(name)
        print "Result: " + ",".join(list1)
    elif command == 5:
        # Sort the section list by the name
        section_list.sort(compare_name)
        list1 = []
        for line in section_list:
            name = line.section_name
            list1.append(name)
        print "Result: " + ",".join(list1)
    else:
        print "Bye!"
####################################################################################