# original_algorithm

Our original algorithm cannot be ran on (real data) the constraints and student preferences inputs parsed by the get_bmc_info.py as they have extra information. We can use Trang's mask_data.py on the parsed constraints and student preferences inputs and then run our original algorithm on the masked constraints and student preferences input. However, we ran our original algorithm on real data by insteaad running our modified algorithm with all the extensions commented on the input files parsed by get_bmc_info.py.

## Run Command to create Schedule
sh run.sh constraints.txt student_preferences.txt schedule.txt

## Valid Schedule Confirmation Command
perl is_valid.pl constraints.txt student_preferences.txt schedule.txt

* Able to run original algorithm on random inputs
