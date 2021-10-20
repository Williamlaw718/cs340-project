

class Classes:

    def __init__(self, ID, teacher):
        self.ID= ID
        self.teacher= teacher
        self.timeslot= -1
        self.room= -1
        self.prefVal= 0
        self.stu_list= 0

    def assignStudents(self, stu_list, timeslot, room):
        self.stu_list= stu_list
        self.prefVal= len(stu_list)
        self.timeslot= timeslot+1
        self.room= room+1
        # once we assign this, we will never reassign because greedy


def assignClass(room, timeslot, student_pref_list, schedule, tsClasses, sClasses, P):
    print(tsClasses)
    if len(tsClasses[timeslot]) == 0:
        cur_class_id= student_pref_list[0][0]
        schedule[cur_class_id].assignStudents(student_pref_list[0][1], timeslot, room[0])
        tsClasses[timeslot].append(cur_class_id)

        # students who will be taking the assigned class
        for student in student_pref_list[0][1]:
            sClasses[student-1].append(cur_class_id)

        return student_pref_list[1:]

    return




# R is room_sizes
# T is num_timeslots
# C is num_classes
# S is student_pref
# P is class_to_teacher
def scheduler(R, T, C, S, P):
    finalized_schedule= []
    classes_of_student_pref= []
    for i in range(C):
        finalized_schedule.append(Classes(i, P[i]))
        classes_of_student_pref.append([i, []]) # this creates an id for each class before we sort based on preference population

    for i in range(len(S)):
        for c in S[i]:
            classes_of_student_pref[c-1][1].append(i)

    classes_of_student_pref.sort(key= lambda x: len(x[1]), reverse = True)

    # list of classes at each timeslot
    tsClasses= []
    for i in range(T):
        tsClasses.append([])
    # list of classes a student takes
    sClasses= []
    for i in range(len(S)):
        sClasses.append([])

    for room in R:
        for i in range(T):
            classes_of_student_pref= assignClass(room, i, classes_of_student_pref, finalized_schedule, tsClasses, sClasses, P)

    for c in finalized_schedule:
        print(str(c.ID) + " " + str(c.stu_list))
