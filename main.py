import re
import os
import sys
from scheduler import scheduler

def main():

    # this is reading the constraints
    with open(sys.argv[1], 'r') as file:
        constraints= file.readlines()

        # we always know that the first line has the number of timeslots
        num_timeslots= int(constraints[0].split()[-1])

        # we know that the second line has the number of classrooms
        num_rooms= int(constraints[1].split()[-1])

        room_sizes= []
        for i in range(2, 2+num_rooms):
            room_sizes.append((i-2, int(constraints[i].split()[-1])))

        # remember to plus 1
        room_sizes.sort(key = lambda x : x[1], reverse = True)

        # after end of room and their sizes
        num_classes= int(constraints[2+num_rooms].split()[-1])

        # will be after classes
        num_teachers= int(constraints[3+num_rooms].split()[-1])

        class_to_teacher= [] # indices are class, values are professor teaching that class
        for i in range(4+num_rooms, len(constraints)):
            class_to_teacher.append(int(constraints[i].split()[-1]))



    # this is reading the student preferences
    student_pref= []
    with open(sys.argv[2], 'r') as file:

        for s_pref in file.readlines()[1:]:
            cur_s_pref= []
            for pref in s_pref.split()[1:]:
                cur_s_pref.append(int(pref))
            student_pref.append(cur_s_pref)

    schedule= scheduler(room_sizes, num_timeslots, num_classes, student_pref, class_to_teacher)

    with open(sys.argv[3], 'a') as file:
        file.write("{}\t{}\t{}\t{}\t{}\n".format("Course", "Room", "Teacher", "Time", "Students"))
        for c in schedule:
            students= ""
            for s in c.stu_list:
                students= students + str(s) + " "
            file.write("{}\t{}\t{}\t{}\t{}\n".format(c.ID+1, c.room, c.teacher, c.timeslot, students))



if __name__ == "__main__":

    main()
