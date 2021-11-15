

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
        return int(self.subject[-1])

    def getSubject(self):
        return self.subject[:len(self.subject)-1]

# comment out lines 41 and 42 to remove the room constraint
# comment out lines 47, 48, 63, 64, 65 to remove subject constraint
# comment out lines 51, 52, 68, 69, 70 to remove level constraint

def assignClass(room, timeslot, student_pref_list, schedule, pTimeslots, sTimeslots, tSubjects, tLevels, numTimeslots):

    # we delete elements from student_pref_list, so we will only iterate if there is an available class
    for i in range(len(student_pref_list)):
        cur_class_id= student_pref_list[i][0]

        # comment out this if statement to remove room constraint
        if not schedule[cur_class_id].viable(room[0]): # this makes it so we have to assign a viable class
            continue


        # comment out this if statement to remove the subject constraint
        if tSubjects[2][timeslot][schedule[cur_class_id].getSubject()] == tSubjects[0][schedule[cur_class_id].getSubject()]:
            continue

        # comment out this if statement to remove the level constraint
        if tLevels[2][timeslot][schedule[cur_class_id].getLevel()-1] == tLevels[0][schedule[cur_class_id].getLevel()-1]:
            continue

        # if a professor is already teaching at this timeslot, move on to the next most popular class
        for pSlots in pTimeslots[schedule[cur_class_id].teacher-1]:
            if pSlots == timeslot:
                break
        else:
            # if the professor passes, then we assign the class to the timeslot and room
            pTimeslots[schedule[cur_class_id].teacher-1].append(timeslot)

            # at this timeslot append to tSubject the subject of this class, comment this out to remove subject constraint
            tSubjects[2][timeslot][schedule[cur_class_id].getSubject()]+= 1
            tSubjects[1][schedule[cur_class_id].getSubject()]+= 1
            tSubjects[0][schedule[cur_class_id].getSubject()]= tSubjects[1][schedule[cur_class_id].getSubject()]//numTimeslots + 1 # if all timeslots at subject capacity, increase cap by 1

            # adding level of course to tLevels and if all timeeslots have reached capacity, increment respective level counter by 1, comment this out to remove level constraint
            tLevels[2][timeslot][schedule[cur_class_id].getLevel()-1]+= 1
            tLevels[1][schedule[cur_class_id].getLevel()-1]+= 1
            tLevels[0][schedule[cur_class_id].getLevel()-1]= tLevels[1][schedule[cur_class_id].getLevel()-1]//numTimeslots + 1 # if all timeslots are at capacity, increase capacity by 1



            # need to check if each student can take the course
            idx= 0
            for j in range(len(student_pref_list[i][1])):

                for time in sTimeslots[student_pref_list[i][1][idx]]: # at most 3
                    if time == timeslot:

                        #print("Student " + str(student_pref_list[i][1][idx]) + " not able to take course " + str(cur_class_id))
                        student_pref_list[i][1].pop(idx) # remove student from the class to finalize class in schedule

                        break # then we do not check anymore and go onto the next student
                else:
                    idx+= 1

            # if the number of students exceed room size, then we slice the list of students to that size
            if (len(student_pref_list[i][1]) > room[1]):
                #print(room[0] + " capacity: " + str(room[1]))
                #print(str(cur_class_id) + " " + str(schedule[cur_class_id].getSubject()) + " popularity: " + str(len(student_pref_list[i][1])))
                #print(str(student_pref_list[i][1][room[1]:]) + " not able to take course " + str(cur_class_id))
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
    tally_subjects= {}
    for i in range(C):
        finalized_schedule.append(Classes(i, P[i][0], P[i][1], P[i][2]))
        classes_of_student_pref.append([i, []]) # this creates an id for each class before we sort based on preference population
        if finalized_schedule[i].getSubject() not in tally_subjects:
            tally_subjects[finalized_schedule[i].getSubject()]= 0

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

    # 0 index of tSubjects corresponds to subject capacities
    # 1 index of tSubjects corresponds to total courses for a particular subject
    # 2 index of tSubjects corresponds to the number of courses for a particular subject at a timeslot
    # comment this out to remove timeslot constraint
    subject_capacities= {}
    for key in tally_subjects:
        subject_capacities[key]= 1
    tSubjects = [subject_capacities, tally_subjects, []]
    for i in range(T):
        tSubjects[2].append(tally_subjects.copy()) # each time we assign a class we'll update the subjects in the timeslot

    # this 3D array holds the level capacities, the total amount of courses for a particular level across all timeslots, and the amount of courses for a particular level at a timeslot
    # the first index of tLevels corresponds to the capacities (if a timeslot has less courses with that level than the capacity, then we are able to add that course)
    # the second index is a running tally of the total number of courses with a particular level among all timeslots
    # the third index holds the amount of courses with the same level in each timeslot
    # NOTE: level 100 courses corresponds to index 0, level 200 courses corresponds to index 1, and level 300 courses corresponds to index 2 (in the 3D array)
    tLevels= [[1, 1, 1], [0, 0, 0], []]
    for i in range(T):
        tLevels[2].append([0, 0, 0])

    for room in R:
        for i in range(T):
            assignClass(room, i, classes_of_student_pref, finalized_schedule, pTimeslots, sTimeslots, tSubjects, tLevels, T)


    sumPrefVal= 0
    for c in finalized_schedule:
        sumPrefVal+= c.prefVal
        #if (c.room == -1):
        #    print("Did not assign class " + str(c.ID+1))
    #    print("Class ID: " + str(c.ID+1))
    #    print("Subject: " + c.subject)
    #    print("Room  ID: " + str(c.room))
    #    print("Timeslot: " + str(c.timeslot))
    #    print("Preference Value: " + str(c.prefVal))
    #    print("Students: " + str(c.stu_list))
    #    print("Teacher: " + str(c.teacher))
    #    print()

    print("\nAlgo Preference Value: " + str(sumPrefVal))
    print("Best Preference Value: " + str(bestPrefVal))
    print("Percent Preference Score: " + str((float(sumPrefVal)/float(bestPrefVal)*float(100))))

    return finalized_schedule
