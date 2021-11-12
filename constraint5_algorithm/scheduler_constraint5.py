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
    for i in rand_order:
        for c in S[i]:
            if finalized_schedule[c-1].getTimeslot() != -1 and finalized_schedule[c-1].getTimeslot() not in sTimeslots[i] and not finalized_schedule[c-1].isAtRoomCap():
                print("hi")
                finalized_schedule[c-1].addStudent(i+1)
                sTimeslots[i].append(finalized_schedule[c-1].getTimeslot())
                sumPrefVal+= 1

            bestPrefVal+= 1


    for c in finalized_schedule:
        if (c.room == -1):
            print("Did not assign class " + str(c.ID+1))
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
