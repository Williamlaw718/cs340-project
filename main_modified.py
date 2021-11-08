import re
import os
import sys
import time
from scheduler_modified import scheduler_modified

convert_class_ID= {}
def main_modified():

    # this is reading the constraints
    with open(sys.argv[1], 'r') as file:
        constraints= file.readlines()

        # we always know that the first line has the number of timeslots
        num_timeslots= int(constraints[0].split()[-1])

        # we know that the second line has the number of classrooms
        num_rooms= int(constraints[1].split()[-1])

        room_sizes= []
        for i in range(2, 2+num_rooms):
            room_sizes.append((constraints[i].split()[0], int(constraints[i].split()[-1])))

        # remember to plus 1
        room_sizes.sort(key = lambda x : x[1], reverse = True)

        # after end of room and their sizes
        num_classes= int(constraints[2+num_rooms].split()[-1])

        # will be after classes
        num_teachers= int(constraints[3+num_rooms].split()[-1])

        class_teacher_subject= [] # indices are class, values are professor teaching that class
        cID= 1
        pID= 1
        convert_prof_ID = {}
        for i in range(4+num_rooms, len(constraints)):
            if int(constraints[i].split()[1]) in convert_prof_ID: # means we have already considered this professor
                class_teacher_subject.append([convert_prof_ID[int(constraints[i].split()[1])], constraints[i].split()[2], constraints[i].split()[3:]])
            else: # need to add a new professor
                class_teacher_subject.append([pID, constraints[i].split()[2], constraints[i].split()[3:]])
                convert_prof_ID[int(constraints[i].split()[1])]= pID
                pID+= 1
            convert_class_ID[int(constraints[i].split()[0])] = cID
            cID+= 1





    # this is reading the student preferences
    student_pref= []
    with open(sys.argv[2], 'r') as file:

        for s_pref in file.readlines()[1:]:
            cur_s_pref= []
            for pref in s_pref.split()[1:]:
                cur_s_pref.append(convert_class_ID[int(pref)])
            student_pref.append(cur_s_pref)


    start_time= time.time()

    schedule= scheduler_modified(room_sizes, num_timeslots, num_classes, student_pref, class_teacher_subject)

    print("--- %s seconds ---" % (time.time() - start_time))

    with open(sys.argv[3], 'w') as file:
        file.write("{}\t{}\t{}\t{}\t{}\n".format("Course", "Room", "Teacher", "Time", "Students"))
        for c in schedule:
            students= ""
            if c.room == -1:
                continue
            for s in c.stu_list:
                students= students + str(s) + " "
            file.write("{}\t{}\t{}\t{}\t{}\n".format(c.ID+1, c.room, c.teacher, c.timeslot, students))



if __name__ == "__main__":

    main_modified()
