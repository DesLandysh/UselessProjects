import sytlib


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
    if sytlib.time_acceleration >= 60:
        time_list = sytlib.count_minutes(sytlib.time_acceleration)
        print(f"""    On the speed of {sytlib.acceleration_mod} from base value,
                you'll spend only:
                    {time_list[0]} hour/-s and
                    {time_list[1]} minute/-s""")
    else:
        print(f"""    On the speed of {sytlib.acceleration_mod} from base value,
                you'll spend only:
                    {sytlib.time_acceleration} minute/-s""")


@decor_outputs
def output_saved_result():
    if sytlib.saved_time >= 60:
        time_list = sytlib.count_minutes(sytlib.saved_time)
        print(f"""            Congratulations! You saved:
                    {time_list[0]} hour/-s and
                    {time_list[1]} minute/-s
                of your worthless life!""")
    else:
        print(f"""            Congratulations! You saved:
                    {sytlib.saved_time} minute/-s
                of your worthless life!""")


@decor_outputs
def print_input_values():
    print(f"""    Your values are:

                      Time: {sytlib.time_txt_input}
                         or {sytlib.sum_of_minutes} minutes 
                     Speed: {sytlib.axel_mod}         
    """)
