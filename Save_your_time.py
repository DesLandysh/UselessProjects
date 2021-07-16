# Author: Des Kitten
# Program that count new time when you set other than 1.0 speed while watching video/listening audio

# !!! A Crunch while is_valid_input is broken
print("""
        *******************************************
        Save your time!
        Use HH:MM type for time,
            where HH - hours
            MM - minutes
            in your video
        Use ':' or '.' as a separator
        And watch tech video faster
        Use X.YY or Y.X type for accelerated speed
            where X. or Y. - whole part
            .YY or .X - decimal part
        Enjoy,
            yours Des Kitten
        ******************************************
        """)


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


'''
This doesn't work yet

def is_valid_input(*args) -> str:
    """
    Function checks if the length is much than needed, if there's negative numbers, and if there's letters.
    :return: x: string
    """
    x = str(args)
    if len(x) > 11:
        # print(len(x))  # Debug_line
        while len(x) > 11:
            x = input("Too much symbols, enter new values: ")
            args = str(x)
    elif not x.find("-", 0, 1):
        while x.find("-", 0, 1):
            x = input("Please, enter positive numbers: ")
            args = str(x)
    elif match(x):
        while match(x):
            x = input("Use numbers and '.' for value: ")
            args = str(x)
    else:
        return str(x)
'''

# Start, requesting input data
time_txt_input = input("Input the time value in format HH:MM: ")
print("")
# Checking the validness
# !!! time_txt_input = is_valid_input(time_txt_input)

# Requesting speed value and checking is_valid by length, negative num and letter includings
axel_mod = input("Input the speed value in format X.Y or X.YY: ")
print("")
# Checking the validness
# !!! axel_mod = is_valid_input(axel_mod)

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
