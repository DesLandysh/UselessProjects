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


def match(text_to_check, alphabet=None):
    """
    Function checks if the inputting value have any letters
    :param text_to_check: is the time_txt_input
    :param alphabet: eng/ru
    :return:
    """
    if alphabet is None:
        alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                       'abcdefghijklmnopqrstuvwyxz'
                       'АБВГДЕЁЖЗИЙКЛАМНОПРСТУФХЦЧЩЪЫЬЭЮЯ'
                       'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return not alphabet.isdisjoint(text_to_check)


def replace_missclicks(*args) -> str:
    """
    Function returns string with replaced separator
    """
    tup_of_missclicks = ',', '?', '/', '@', '<', '>', 'б', 'ю', 'Б', 'Ю', '%', \
                        '^', '&', ':', ';', 'Ж', 'ж', '*', '+', "\\", '"', "'", "."
    x, y = args
    for i in tup_of_missclicks:
        if x.find(str(i)):
            x = x.replace(str(i), y)
            # print(x, "is the x value") # Debug_line
    return x


# Start, requesting input data
time_txt_input = input("Input the time value in format HH:MM: ")

# Defence by checking length, letter fill and negative values
if len(time_txt_input) > 7:
    try:
        len(time_txt_input) > 7
    except TypeError:
        print("Length alert")
    finally:
        time_txt_input = input("Please, type using HH:MM format (6 symbols max):")
elif match(time_txt_input):
    try:
        match(time_txt_input)
    except TypeError:
        print("Letters alert")
    finally:
        time_txt_input = input("Please, type using only numbers HH:MM format:")
elif time_txt_input.find("-", 0):
    try:
        time_txt_input.find("-", 0)
    except ValueError:
        print("Negative number alert")
    finally:
        time_txt_input = input("Please, type using positive numbers for HH:MM format:")
else:
    print("time_txt_input")

# Requesting speed value and checking is_valid by length, negative num and letter includings
axel_mod = input("Input the speed value in format X.Y or X.YY: ")
if len(axel_mod) > 4:
    try:
        len(axel_mod) > 4
    except TypeError:
        print("Length alert")
    finally:
        axel_mod = input("Please, type using X.Y or X.YY format (3 symbols max):")
elif axel_mod.find("-", 0):
    try:
        axel_mod.find("-", 0)
    except ValueError:
        print("Negative number alert")
    finally:
        axel_mod = input("Please, type using positive numbers for X.Y or X.YY format:")
elif match(axel_mod):
    try:
        match(axel_mod)
    except TypeError:
        print("Letters alert")
    finally:
        axel_mod = input("Please, type using only numbers X.Y or X.YY format:")
else:
    print("time_txt_input")

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
