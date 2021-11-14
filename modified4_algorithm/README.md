# modified4_algorithm

## Run Command

### Extension 1

sh run_modified.sh ../brynmawr/fall/[Insert_Year]/constraints.txt  ../brynmawr/fall/[Insert_Year]/student_preferences.txt  ../brynmawr/fall/[Insert_Year]/scheduleSubject.txt


### Extension 2

sh run_modified.sh  ../brynmawr/fall/[Insert_Year]/constraints.txt  ../brynmawr/fall/[Insert_Year]/student_preferences.txt  ../brynmawr/fall/[Insert_Year]/scheduleLevel.txt

### Extension 3

sh run_modified.sh  ../brynmawr/fall/[Insert_Year]/constraints.txt  ../brynmawr/fall/[Insert_Year]/student_preferences.txt  ../brynmawr/fall/[Insert_Year]/scheduleRoom.txt

### Extension 4

sh run_modified.sh  ../brynmawr/fall/[Insert_Year]/constraintsSizeUp.txt  ../brynmawr/fall/[Insert_Year]/student_preferencesSizeUp.txt  ../brynmawr/fall/[Insert_Year]/scheduleSizeUp.txt

## Valid Schedule Confirmation Command
perl is_valid.pl  ../brynmawr/fall/[Insert_Year]/constraintsNew.txt ../brynmawr/fall/[Insert_Year]/student_preferencesNew.txt ../brynmawr/fall/[Insert_Year]/scheduleLevel.txt

perl is_valid.pl ../brynmawr/fall/[Insert_Year]/constraintsSNew.txt ../brynmawr/fall/[Insert_Year]/student_preferencesNew.txt ../brynmawr/fall/[Insert_Year]/scheduleRoom.txt

perl is_valid.pl ../brynmawr/fall/[Insert_Year]/constraintsNew.txt ../brynmawr/fall/[Insert_Year]/student_preferencesNew.txt ../brynmawr/fall/[Insert_Year]/scheduleSubject.txt

perl is_valid.pl ../brynmawr/fall/[Insert_Year]/constraintsSizeUpNew.txt ../brynmawr/fall/[Insert_Year]/student_preferencesSizUpNew.txt ../brynmawr/fall/[Insert_Year]/scheduleSizeUp.txt



