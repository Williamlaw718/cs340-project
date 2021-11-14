import random

class Classes:

    def __init__(self, ID, teacher, subject):
        self.ID= ID
        self.teacher= teacher
        self.timeslot= -1
        self.room= -1
        self.roomCap= -1
        self.stu_list= []
        self.subject= subject

    def assignStudents(self, stu_list, timeslot, roomName):
        self.stu_list= stu_list # need to add 1 to the students when we print out the statement
        self.timeslot= timeslot+1
        self.room= roomName
        # once we assign this, we will never reassign because greedy

    def assignRoomTime(self, timeslot, room):
        self.room= room[0]
        self.roomCap= room[1]
        self.timeslot= timeslot+1

    def addStudent(self, student):
        self.stu_list.append(student)

    def getTeacher(self):
        return self.teacher

    def viable(self, room):
        return room in self.viableRooms

    def getLevel(self):
        return int(self.subject[-1])

    def getSubject(self):
        return self.subject[:len(self.subject)-1]

    def getTimeslot(self):
        return self.timeslot

    def isAtRoomCap(self): # or greater when room and roomcap is not assigned
        return len(self.stu_list) >= self.roomCap


# R is room_sizes
# T is num_timeslots
# C is num_classes
# S is student_pref
# P is class_to_teacher
def scheduler_constraint5(R, T, C, S, P):
    finalized_schedule= []
    for i in range(C):
        finalized_schedule.append(Classes(i, P[i][0], P[i][1]))

    working_schedule= finalized_schedule.copy()

    working_schedule.sort(key = lambda x: x.getLevel())

    # list of professors and the timeslots they were already assigned
    pTimeslots= []
    for i in range(len(P)):
        pTimeslots.append([])

    # list of students and the timeslots they were already assigned
    sTimeslots= []
    for i in range(len(S)):
        sTimeslots.append([])

    for room in R:
        for i in range(T):
            for c in range(len(working_schedule)):
                if i in pTimeslots[working_schedule[c].getTeacher()-1]:
                    continue

                working_schedule[c].assignRoomTime(i, room)
                pTimeslots[working_schedule[c].getTeacher()-1].append(i)
                working_schedule.pop(c)
                break


    bestPrefVal= 0
    sumPrefVal= 0
    rand_order= list(range(len(S)))
    random.shuffle(rand_order)
    #numStuConflict= 0
    #numRoomCapConflict= 0
    #stu_order_pref= [] # will keep track of how many preferred classes a student got by order in which they registered
    for i in rand_order:
        exp_pref= 0
        for c in S[i]:
            if finalized_schedule[c-1].getTimeslot() != -1 and finalized_schedule[c-1].getTimeslot() not in sTimeslots[i] and not finalized_schedule[c-1].isAtRoomCap():
                finalized_schedule[c-1].addStudent(i+1)
                sTimeslots[i].append(finalized_schedule[c-1].getTimeslot())
                sumPrefVal+= 1
                #exp_pref+= 1
            #else:
                #reason= "Student " + str(i+1) + " could not register for course " + str(c)
                #if finalized_schedule[c-1].getTimeslot() in sTimeslots[i]:
                #    reason = reason + " b/c student timeslot conflict "
                #    numStuConflict+= 1
                #if finalized_schedule[c-1].isAtRoomCap():
                #    reason = reason + " b/c of room cap conflict"
                #    numRoomCapConflict+= 1
                #print(reason)
            bestPrefVal+= 1
        #stu_order_pref.append((exp_pref, len(S[i]))) # index i of stu_order_pref represents when they registered and the first index of the tuple represents how mnany
        #preferred classes the student got and the second index of the tuple represents the total number of preferred classes they got

    for c in finalized_schedule:
        if (c.room == -1):
            print("Did not assign class " + str(c.ID+1))
        #print("Class ID: " + str(c.ID+1))
        #print("Level: " + str(c.getLevel()))
        #print("Room  ID: " + str(c.room))
        #print("Timeslot: " + str(c.timeslot))
        #print("Students: " + str(c.stu_list))
        #print("Teacher: " + str(c.teacher))
    print()

    print(stu_order_pref)
    #print("Number of Student Timeslot Conflict: " + str(numStuConflict))
    #print("Number of Room Cap Conflict: " + str(numRoomCapConflict))

    print("\nAlgo Preference Value: " + str(sumPrefVal))
    print("Best Preference Value: " + str(bestPrefVal))
    print("Percent Preference Score: " + str((float(sumPrefVal)/float(bestPrefVal)*float(100))))

    return finalized_schedule
