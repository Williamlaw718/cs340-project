import re
import os
import sys

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
            room_sizes.append(int(constraints[i].split()[-1]))

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
    print(num_timeslots)
    print(num_rooms)
    print(room_sizes)
    print(num_classes)
    print(num_teachers)
    print(class_to_teacher)
    print(student_pref)





    schedule_output= sys.argv[3]

if __name__ == "__main__":

    main()
