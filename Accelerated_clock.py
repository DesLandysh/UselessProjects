# Author: Des Kitten
# Program that count new time when you set other than 1.0 speed while watching video/listening audio
"""
    TODO:
    - Try/Exception
        - done! by length
        - done! by negative values
        - by letters
    - undone! Refactor sum_of_minutes
    - undone! Refactor time_acceleration
    - Return the Ru in other branch
"""


def replace_missclicks(*args) -> str:
    """
    Function returns string with replaced separator
    """
    tup_of_missclicks = ',', '?', '/', '@', '<', '>', 'б', 'ю', 'Б', 'Ю', '%',\
                        '^', '&', ':', ';', 'Ж', 'ж', '*', '+', "\\", '"', "'", "."
    x, y = args
    for i in tup_of_missclicks:
        if x.find(str(i)):
            x = x.replace(str(i), y)
            # print(x, "is the x value") # Debug_line
    return x


# Start, requesting input data
time_txt_input = input("Input the time value in format HH:MM: ")
axel_mod = input("Input the speed value in format X.Y or X.YY: ")

try:
    len(time_txt_input) > 10
except TypeError:
    time_txt_input = "00:01"
finally:
    time_txt_input = input("Please, type using HH:MM format:")

try:
    time_txt_input.find([0] == "-")
except ValueError:
    print("You enter the negative value of time")
finally:
    print('If you insist of your value, type "Y", otherwise press "N" to set new value')
    is_choice = input()
    if is_choice == "N" or "n":
        time_txt_input = input("Please, type using HH:MM format:")
    elif is_choice == "Y" or "y":
        time_txt_input = time_txt_input[:[1]]
    else:
        print("Don't trick me out!")
        time_txt_input = input("Type with >> HH:MM << this format:")

try:
    len(axel_mod) > 4
except TypeError:
    axel_mod = 1.0
finally:
    axel_mod = input("Please, type using X.Y or X.YY format:")

try:
    axel_mod.find([0] == "-")
except ValueError:
    print("You enter the negative value of time")
finally:
    print('If you insist of your value, type "Y", otherwise press "N" to set new value')
    is_choice_a = input()
    if is_choice_a == "N" or "n":
        axel_mod = input("Please, type using X.YY or Y.X format:")
    elif is_choice_a == "Y" or "y":
        axel_mod = axel_mod[:[1]]
    else:
        print("Don't trick me out!")
        axel_mod = input("Type with >> Y.XX << this format:")

# Checking the missclicks
axel_mod = replace_missclicks(axel_mod, '.')
time_txt_input = replace_missclicks(time_txt_input, ':')

# Converting the acceleration modifier
acceleration_mod = float(axel_mod)

# Find & count minutes in hours and sums them all
sep_marker = time_txt_input.find(":")
num_of_hours = int(time_txt_input[:sep_marker])
num_of_minutes = int(time_txt_input[(sep_marker + 1):])
sum_of_minutes = num_of_hours * 60 + num_of_minutes


# Separation the new sum of minutes onto hours and minutes
h_output, m_output = 1, 1
time_acceleration = int(sum_of_minutes // acceleration_mod)
if time_acceleration >= 60:
    h_output: int = int(time_acceleration / 60)
    m_output: int = int(time_acceleration % 60)

# Calculating the saving time and separating it onto hours and minutes
h_saved, m_saved = 1, 1
saved_time = sum_of_minutes - time_acceleration
if saved_time >= 60:
    h_saved: int = int(saved_time / 60)
    m_saved: int = int(saved_time % 60)

# Output
print("On the speed of", acceleration_mod, "from base value, you'll spend only:", h_output, "hour/-s", " and", m_output,
      "minute/-s")
print("You save", h_saved, "hour/-s", m_saved, "minute/s for other things")
quit()
