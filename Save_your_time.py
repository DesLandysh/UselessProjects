# Author: Des Kitten
# Program that count new time when you set other than 1.0 speed while watching video/listening audio

# !!! A Crunch while is_valid_input is broken
print("""
        *******************************************
                      SAVE YOUR TIME!
        Use HH:MM type for time,
            where HH - hours, MM - minutes
        Use ':' or '.' as a separator

        Use X.YY or Y.X type for accelerated speed
            where X. or Y. - whole part
            .YY or .X - decimal part
        Enjoy,
            yours Des Kitten
        ******************************************
        """)


def match(x, alphabet=None):
    """
    Function checks if the inputting value have any letters (Stolen from StackOverFlow)
    :param x: input data
    :param alphabet: eng/ru
    :return: True if input data have any letter
    """
    if alphabet is None:
        alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                       'abcdefghijklmnopqrstuvwyxz'
                       'АБВГДЕЁЖЗИЙКЛАМНОПРСТУФХЦЧЩЪЫЬЭЮЯ'
                       'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return not alphabet.isdisjoint(x)


def replace_missclicks(x, y) -> str:
    """
    Function returns string with replaced separator
    :param x: input data
    :param y: needed separator
    """
    tup_of_missclicks = ',', '?', '/', '@', '<', '>', 'б', 'ю', 'Б', 'Ю', '%', \
                        '^', '&', ':', ';', 'Ж', 'ж', '*', '+', "\\", '"', "'", "."
    for i in tup_of_missclicks:
        if x.find(str(i)):
            x = x.replace(str(i), y)
            # print(x, "is the x value") # Debug_line
    return x


# This is crunch
def is_valid_input(x):
    """
    Func must return valid str to use it later, it must do it while it's not valid
    is_length_valid checks if the len > 6
    is_letter_input checks if the data has letters
    is_neg_input checks if there's "-" sign
    :param x: user data input
    :return x: str-to-be-sure the valid result
    """
    # print(x, "x")  # Debug_line
    for i in range(4):
        x = is_length_valid(x)
        x = is_letter_input(x)
        x = is_neg_input(x)
        i += 1
    return str(x)


def is_neg_input(x) -> str:
    """
    Function checks if the length is much than needed, if there's negative numbers
    :param x: user data input
    :return x: str-to-be-sure new input data
    """
    while "-" in x:
        x = input("Please, enter the positive numbers: ")
    else:
        # print(x, "in neg is valid")  # Debug_line
        return str(x)


def is_letter_input(x):
    """
    Function checks if user input letters, and aks user again
    :param x: user input data
    :return x: str-to-be-sure new input data
    """
    while match(x):
        x = input("Please, use numbers instead of letters: ")
    else:
        # print(x, " in is letter")  # Debug_line
        return str(x)


def is_length_valid(x):
    """
    Function checks if user input more symbols than need, and ask user again
    :param x: user input data
    :return x: str-to-be-sure new input data
    """
    while len(x) > 9:
        x = input("Please, use shorter numbers: ")
    else:
        # print(x, "is in length")  # Debug_line
        return str(x)


def is_no_hours(x):
    """
    Function checks if user input data without separator and hours
    :param x: user data input
    :return: x: str
    """
    z = ',', '?', '/', '@', '<', '>', 'б', 'ю', 'Б', 'Ю', '%', \
        '^', '&', ':', ';', 'Ж', 'ж', '*', '+', "\\", '"', "'", "."
    pass


# Start, requesting input data
time_txt_input = input("Input the time value in format HH:MM: ")
print("")
time_txt_input = is_valid_input(time_txt_input)
print(time_txt_input, "after is valid")  # Debug_line

axel_mod = input("Input the speed value in format X.Y or X.YY: ")
print("")
axel_mod = is_valid_input(axel_mod)
print(axel_mod, "after is valid")  # Debug_line


# Checking the missclicks
axel_mod = replace_missclicks(axel_mod, '.')
time_txt_input = replace_missclicks(time_txt_input, ':')
# print(time_txt_input, "after replace missclicks")   # Debug_line

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
# print(time_acceleration, "time", sum_of_minutes, "sumM", acceleration_mod, "acMod")  # Debug_line
if time_acceleration >= 60:
    h_output: int = int(time_acceleration / 60)
    m_output: int = int(time_acceleration % 60)
    print(f"""
            *******************************************
            On the speed of {acceleration_mod} from base value,
            you'll spend only:
                {h_output} hour/-s and
                {m_output} minute/-s
            *******************************************""")
else:
    m_output = time_acceleration
    print(f"""
            *******************************************
            On the speed of {acceleration_mod} from base value,
            you'll spend only:
                {m_output} minute/-s
            *******************************************""")

# Calculating the saving time and separating it onto hours and minutes
h_saved, m_saved = 1, 1
saved_time = sum_of_minutes - time_acceleration
# print(time_acceleration, "time", sum_of_minutes, "sumM", saved_time, "SavedTi")  # Debug_line
if saved_time >= 60:
    h_saved: int = int(saved_time / 60)
    m_saved: int = int(saved_time % 60)
    print(f"""
            *******************************************
                Congratulations! You saved:
                    {h_saved} hour/-s and
                    {m_saved} minute/-s
                of your worthless life!
            *******************************************""")
else:
    m_saved = saved_time
    print(f"""
            *******************************************
                Congratulations! You saved:
                    {m_saved} minute/-s
                of your worthless life!
            *******************************************""")
quit()