

class Classes:

    def __init__(self, ID, teacher, subject, viableRooms):
        self.ID= ID
        self.teacher= teacher
        self.timeslot= -1
        self.room= -1
        self.prefVal= 0
        self.stu_list= 0
        self.subject= subject
        self.viableRooms= viableRooms # a list of rooms that this class can be put in

    def assignStudents(self, stu_list, timeslot, roomName):
        self.stu_list= stu_list # need to add 1 to the students when we print out the statement
        self.prefVal= len(stu_list)
        self.timeslot= timeslot+1
        self.room= roomName
        # once we assign this, we will never reassign because greedy

    def viable(self, room):
        return room in self.viableRooms

    def getLevel(self):
        return self.subject[-1]

    def getSubject(self):
        return self.subject[:len(self.subject)-1]



def assignClass(room, timeslot, student_pref_list, schedule, pTimeslots, sTimeslots, tSubjects):

    # we delete elements from student_pref_list, so we will only iterate if there is an available class
    for i in range(len(student_pref_list)):
        cur_class_id= student_pref_list[i][0]

        # comment out this if statement to remove room constraint
        #if not schedule[cur_class_id].viable(room[0]): # this makes it so we have to assign a viable class
        #    continue

        if schedule[cur_class_id].getSubject() in tSubjects[timeslot]:
            continue


        # if a professor is already teaching at this timeslot, move on to the next most popular class
        for pSlots in pTimeslots[schedule[cur_class_id].teacher-1]:
            if pSlots == timeslot:
                break
        else:
            # if the professor passes, then we assign the class to the timeslot and room
            pTimeslots[schedule[cur_class_id].teacher-1].append(timeslot)

            # at this timeslot append to tSubject the subject of this class
            tSubjects[timeslot].append(schedule[cur_class_id].getSubject())

            # need to check if each student can take the course
            idx= 0
            for j in range(len(student_pref_list[i][1])):

                for time in sTimeslots[student_pref_list[i][1][idx]]: # at most 3
                    if time == timeslot:
                        student_pref_list[i][1].pop(idx) # remove student from the class to finalize class in schedule
                        break # then we do not check anymore and go onto the next student
                else:
                    idx+= 1

            # if the number of students exceed room size, then we s
            if (len(student_pref_list[i][1]) > room[1]):
                student_pref_list[i][1]= student_pref_list[i][1][:room[1]]

            # adds this timeslot to the student's schedule at student_pref_list[i][1][j]
            for j in range(len(student_pref_list[i][1])):
                sTimeslots[student_pref_list[i][1][j]].append(timeslot)
                student_pref_list[i][1][j]+= 1


            schedule[cur_class_id].assignStudents(student_pref_list[i][1], timeslot, room[0])

            student_pref_list.pop(i)

            return

    return




# R is room_sizes
# T is num_timeslots
# C is num_classes
# S is student_pref
# P is class_to_teacher
def scheduler_modified(R, T, C, S, P):
    finalized_schedule= []
    classes_of_student_pref= []
    for i in range(C):
        finalized_schedule.append(Classes(i, P[i][0], P[i][1], P[i][2]))
        classes_of_student_pref.append([i, []]) # this creates an id for each class before we sort based on preference population

    bestPrefVal= 0
    for i in range(len(S)):
        for c in S[i]:
            classes_of_student_pref[c-1][1].append(i)
            bestPrefVal+= 1

    classes_of_student_pref.sort(key= lambda x: len(x[1]), reverse = True)

    # list of professors and the timeslots they were already assigned
    pTimeslots= []
    for i in range(len(P)):
        pTimeslots.append([])
    # list of students and the timeslots they were already assigned
    sTimeslots= []
    for i in range(len(S)):
        sTimeslots.append([])

    # comment this out to remove timeslot constraint
    tSubjects = []
    for i in range(T):
        tSubjects.append([]) # each time we assign a class we'll update the subjects in the timeslot

    for room in R:
        for i in range(T):
            assignClass(room, i, classes_of_student_pref, finalized_schedule, pTimeslots, sTimeslots, tSubjects)



    sumPrefVal= 0
    for c in finalized_schedule:
        sumPrefVal+= c.prefVal
        print("Class ID: " + str(c.ID+1))
        print("Subject: " + c.subject)
        print("Room  ID: " + str(c.room))
        print("Timeslot: " + str(c.timeslot))
        print("Preference Value: " + str(c.prefVal))
        print("Students: " + str(c.stu_list))
        print("Teacher: " + str(c.teacher))
        print()

    print("\nAlgo Preference Value: " + str(sumPrefVal))
    print("Best Preference Value: " + str(bestPrefVal))
    print("Percent Preference Score: " + str((float(sumPrefVal)/float(bestPrefVal)*float(100))))

    return finalized_schedule
