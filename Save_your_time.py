# Denis "Des Kitten" Trebushnikov © 2021
# Program that count new time when you set other than 1.0 speed while watching video/listening audio

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


def count_minutes(base_time_data: int):
    """
    Function takes time_acceleration or saved_time
    :return int-to-be-sure: separated hours and minutes data
    """
    hh = int(base_time_data / 60)
    mm = int(base_time_data % 60)
    return hh, mm


def stars_line():
    """
    Draw the line of asterisks
    """
    menu_width = 45
    print('*' * menu_width)


def decor_outputs(foo):
    """
    Decorator takes function and wraps it with lines of asterisks
    """
    def wrapper():
        stars_line()
        foo()
        stars_line()
    return wrapper


@decor_outputs
def start_menu():
    print("""              SAVE YOUR TIME!
    
   Use HH:MM type for time,
       where HH - hours, MM - minutes
   Use ':' or '.' as a separator

   Use X.YY or Y.X type for accelerated speed
       where X. or Y. - whole part
       .YY or .X - decimal part
   Enjoy,
            yours Des Kitten""")


@decor_outputs
def output_axel_count():
    if time_acceleration >= 60:
        time_list = count_minutes(time_acceleration)
        print(f"""    On the speed of {acceleration_mod} from base value,
                you'll spend only:
                    {time_list[0]} hour/-s and
                    {time_list[1]} minute/-s""")
    else:
        print(f"""    On the speed of {acceleration_mod} from base value,
                you'll spend only:
                    {time_acceleration} minute/-s""")


@decor_outputs
def output_saved_result():
    if saved_time >= 60:
        time_list = count_minutes(saved_time)
        print(f"""            Congratulations! You saved:
                    {time_list[0]} hour/-s and
                    {time_list[1]} minute/-s
                of your worthless life!""")
    else:
        print(f"""            Congratulations! You saved:
                    {saved_time} minute/-s
                of your worthless life!""")


@decor_outputs
def print_input_values():
    print(f"""    Your values are:
                    
                      Time: {time_txt_input}
                         or {sum_of_minutes} minutes 
                     Speed: {axel_mod}         
    """)


start_menu()

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

print_input_values()  # Sugar

# Separation the new sum of minutes onto hours and minutes
time_acceleration = int(sum_of_minutes // acceleration_mod)
output_axel_count()

# Calculating the saving time and separating it onto hours and minutes
saved_time = sum_of_minutes - time_acceleration
output_saved_result()

quit()
