# Denis "Des Kitten" Trebushnikov © 2021
# Program that count new time when you set other than 1.0 speed while watching video/listening audio

import sytlib
import decoration


decoration.start_menu()

# Requesting input data
print()
time_txt_input = input("Input the time value: ")
print()
time_txt_input = sytlib.is_valid_input(time_txt_input)

axel_mod = input("Input the speed value: ")
print()
axel_mod = sytlib.is_valid_input(axel_mod)

# Checking the missclicks
axel_mod = sytlib.replace_missclicks(axel_mod, '.')
time_txt_input = sytlib.replace_missclicks(time_txt_input, ':')

# Converting the acceleration modifier
acceleration_mod = float(axel_mod)

# Find & count minutes in hours and sums them all
num_of_hours = int(time_txt_input.split(':')[0])
num_of_minutes = int(time_txt_input.split(':')[1])
sum_of_minutes = num_of_hours * 60 + num_of_minutes

decoration.print_input_values()  # Sugar

# Separation the new sum of minutes onto hours and minutes
time_acceleration = int(sum_of_minutes // acceleration_mod)
decoration.output_axel_count()

# Calculating the saving time and separating it onto hours and minutes
saved_time = sum_of_minutes - time_acceleration
decoration.output_saved_result()

quit()
