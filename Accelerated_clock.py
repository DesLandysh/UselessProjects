# Author: Des Kitten
# Program that count new time when you set other than 1.0 speed while watching video/listening audio
"""
    TODO:
    - Try/Exception
        - by length
        - by negative values
    - Refactor sum_of_minutes
    - Refactor time_acceleration
    - Return the Ru in other branch
"""


def replace_missclicks(*args) -> str:
    """
    Function returns string with replaced separator
    """
    tup_of_missclicks = ',', '?', '/', '@', '<', '>', 'б', 'ю', 'Б', 'Ю', '%',\
                        '^', '&', ':', ';', 'Ж', 'ж', '*', '+', "\\", '"', "'"
    x, y = args
    for i in tup_of_missclicks:
        if x.find(str(i)):
            x = x.replace(str(i), y)
            # print(x, "is the x value") # Debug_line
    return x


def clock_separation():
    """
    Function finds and separates minutes from hours by separation marker
    :get: string
    :return: tuple of two separated integer values
    """
    sep_marker = time_txt_input.find(":")
    num_of_hours = int(time_txt_input[:sep_marker])
    num_of_minutes = int(time_txt_input[(sep_marker + 1):])
    # print(sep_marker, "is the sep;", num_of_hours, "are the hours; and the minutes are ", num_of_minutes) # Debug_line
    return num_of_hours, num_of_minutes


# Start, requesting input data
time_txt_input = input("Input the time value in format HH:MM: ")
axel_mod = input("Input the speed value in format X.Y or X.YY: ")

# Checking the missclicks
axel_mod = replace_missclicks(axel_mod, '.')
time_txt_input = replace_missclicks(time_txt_input, ':')
# print("axel_mod", axel_mod, "and time", time_txt_input) # Debug_line

# Converting the acceleration modifier
acceleration_mod = float(axel_mod)
# print(acceleration_mod, "this is the float num") # Debug_line

# Find & count minutes in hours and sums them all
num_of_hours = num_of_minutes = 0

clock_separation()
sum_of_minutes = num_of_hours * 60 + num_of_minutes

# Separation the new sum of minutes onto hours and minutes
h_output, m_output = 1, 1
time_acceleration = int(sum_of_minutes // acceleration_mod)
if time_acceleration >= 60:
    h_output: int = int(time_acceleration / 60)
    m_output: int = int(time_acceleration % 60)

# Разложение на падежи
print("On the speed of", acceleration_mod, "from base, you'll get only:", h_output, "hour/-s", " and", m_output,
      "minute/-s")
quit()
