# Author: Des Kitten
# Program that count new time when you set other than 1.0 speed while watching video/listening audio



# Checking the missclicks

def replace_missclicks(x: str) -> str:
    """
    Funsction returns string with replaced separator
    :type x: string
    """
    tup_of_missclicks = ',', '?', '/', '@', '<', '>', 'б', 'ю', 'Б', \
                        'Ю', '%', '^', '&', ':', ';', 'ж', 'Ж', '*'
    for i in tup_of_missclicks:
        if x.find(str(i)):
            x = x.replace(str(i), '.')


# Start, requesting input data
time_txt_input = input("Введите время видео в формате ЧЧ:ММ: ")

axel_mod = input("Введите скорость воспроизведения: ")

""" Previous code before it def as function above
for i in tup_of_missclicks:
    if axel_mod.find(str(i)):
        axel_mod = axel_mod.replace(str(i), '.')
    elif time_txt_input.find(str(i)):
        time_txt_input = time_txt_input.replace(str(i), ':')
"""

replace_missclicks(axel_mod)
replace_missclicks(time_txt_input)
print(axel_mod, "time", time_txt_input) ## DEBUG: function

# Converting the acceleration modifier
acceleration_mod = float(axel_mod)
print(acceleration_mod)

# Find & count minutes in hours and sums them all
clock_sep = time_txt_input.find(":")

num_of_hours = int(time_txt_input[:clock_sep])
num_of_minutes = int(time_txt_input[(clock_sep + 1):])

sum_of_minutes = num_of_hours * 60 + num_of_minutes

# Separation the new sum of minutes onto hours and minutes
h_output, m_output = 1, 1
time_acceleration = int(sum_of_minutes // acceleration_mod)
if time_acceleration >= 60:
    h_output: int = int(time_acceleration / 60)
    m_output: int = int(time_acceleration % 60)

# Разложение на падежи
print("На скорости", acceleration_mod, "вы просмотрите видео за:", h_output, "час/-ов/-а/", ",", m_output,
      "минут/-ы/-у")
quit()
