

def is_neg_input(x) -> str:
    """
    Function checks if the length is much than needed, if there's negative numbers
    :param x: user data input
    :return x: str-to-be-sure new input data
    """
    while "-" in x:
        x = input("Please, enter the positive numbers: ")
    else:
        return str(x)


def is_letter_input(x):
    """
    Function checks if user input letters, and aks user again
    :param x: user input data
    :return x: str-to-be-sure new input data
    """
    while x.isalpha():
        x = input("Please, use numbers instead of letters: ")
    else:
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
        return str(x)


def is_no_hours(x):
    """
    Function checks if user input data without separator and hours
    :param x: user data input
    :return: x: str
    """
    sep_marker = ',', '?', '/', '@', '<', '>', 'б', 'ю', 'Б', 'Ю', '%', \
        '^', '&', ':', ';', 'Ж', 'ж', '*', '+', "\\", '"', "'", "."
    if x.isdigit():
        y = "0:"
        x = str(y + x)
    else:
        for i in sep_marker:
            if x.find(str(i)):
                y = "0"  # It prevents ".55 is valid" bug
            else:
                y = "0"
                x = (y + x)
    return str(x)


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
    return x


def is_valid_input(x):
    """
    Function returns valid str
        is_length_valid checks if the len > 6
        is_letter_input checks if the data has letters
        is_neg_input checks if there's "-" sign
        is_no_hours checks if time_txt_input looks like '.55'
    :param x: user data input
    :return x: str-to-be-sure the valid result
    """
    for i in range(4):
        x = is_length_valid(x)
        x = is_letter_input(x)
        x = is_neg_input(x)
        x = is_no_hours(x)
        i += 1
    return str(x)


def count_minutes(base_time_data: int):
    """
    Function takes time_acceleration or saved_time
    :return int-to-be-sure: separated hours and minutes data
    """
    hh = int(base_time_data / 60)
    mm = int(base_time_data % 60)
    return hh, mm


# Requesting input data
print()
time_txt_input = input("Input the time value: ")
print()
time_txt_input = is_valid_input(time_txt_input)

axel_mod = input("Input the speed value: ")
print()
axel_mod = is_valid_input(axel_mod)

# Checking the missclicks
axel_mod = replace_missclicks(axel_mod, '.')
time_txt_input = replace_missclicks(time_txt_input, ':')

# Converting the acceleration modifier
acceleration_mod = float(axel_mod)

# Find & count minutes in hours and sums them all
num_of_hours = int(time_txt_input.split(':')[0])
num_of_minutes = int(time_txt_input.split(':')[1])
sum_of_minutes = num_of_hours * 60 + num_of_minutes

# Separation the new sum of minutes onto hours and minutes
time_acceleration = int(sum_of_minutes // acceleration_mod)
saved_time = sum_of_minutes - time_acceleration
