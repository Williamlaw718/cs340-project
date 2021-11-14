# modified4_algorithm

## Run Command

### Extension 1

sh run_modified.sh fall/[Insert_Year]/constraints.txt fall/[Insert_Year]/student_preferences.txt fall/[Insert_Year]/scheduleSubject.txt


### Extension 2

sh run_modified.sh fall/[Insert_Year]/constraints.txt fall/[Insert_Year]/student_preferences.txt fall/[Insert_Year]/scheduleLevel.txt

### Extension 3

sh run_modified.sh fall/[Insert_Year]/constraints.txt fall/[Insert_Year]/student_preferences.txt fall/[Insert_Year]/scheduleRoom.txt

### Extension 4

sh run_modified.sh fall/[Insert_Year]/constraintsSizeUp.txt fall/[Insert_Year]/student_preferencesSizeUp.txt fall/[Insert_Year]/scheduleSizeUp.txt

## Valid Schedule Confirmation Command
perl is_valid.pl fall/[Insert_Year]/constraintsNew.txt fall/[Insert_Year]/student_preferencesNew.txt fall/[Insert_Year]/scheduleLevel.txt
perl is_valid.pl fall/[Insert_Year]/constraintsSNew.txt fall/[Insert_Year]/student_preferencesNew.txt fall/[Insert_Year]/scheduleRoom.txt
perl is_valid.pl fall/[Insert_Year]/constraintsNew.txt fall/[Insert_Year]/student_preferencesNew.txt fall/[Insert_Year]/scheduleSubject.txt
perl is_valid.pl fall/[Insert_Year]/constraintsSizeUpNew.txt fall/[Insert_Year]/student_preferencesSizUpNew.txt fall/[Insert_Year]/scheduleSizeUp.txt



