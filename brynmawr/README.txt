For each Fall semester, we parsed the data and created constraints.txt and student_prefs.txt by running the command:
"python get_bmc_info.py" on each of the Fall<year>.csv files to get input constraint and student preference files
Command: "python get_bmc_info.py data/Fall<year>.csv student_prefs.txt constraints.txt"

We get constraints.txt file which contains the 17 timeslots, available rooms and their capacities, classes and their professors, subjects, and viable rooms.

We get student_prefs.txt file which contains the classes that each student prefers based on the classes each student was enrolled in.

We then call our modified algorithm on these two files and create a schedule based on each extension:
"sh run_modified.sh constraints.txt student_prefs.txt schedule.txt"

Then, to see if our output schedule.txt is valid, we have to parse our constraints.txt and student_prefs.txt file to be in a valid format so that we can call the is_valid.pl perl script on the parsed constraints, student prefs and schedule.

We used Trang's mask_data.py script posted on Slack to parse our constraints.txt and student_prefs.txt file to create new constraintsNew.txt and student_prefsNew.txt. We use the command "python mask_data.py constraints.txt student_prefs.txt constraintsNew.txt student_prefsNew.txt" to create the two new input files we need to then call is_valid.pl on our schedule.

The command to validate our schedule is:
"perl is_valid.pl constraintsNew.txt student_prefsNew.txt schedule.txt" (and we can call this script on each schedule for each different extension)


NOTE: we see that the number of professors decreases when we call mask_data.py because some of the professor originally parsed do not actually teach the classes that we parsed, meaning we had professors who did not teach a class we are considering in our constraints files.


For extension 4, we modified the get_bc_info.py script to "get_bmc_info_up_size.py" in order to increase the room capacities by at most 5. We can simply do a similar command to get the sized up constraint input:
"python get_bmc_info_up_size.py data/Fall<year>.csv student_prefs.txt constraintsSizeUp.txt"