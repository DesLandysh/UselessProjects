# Author: Des Kitten
# Program that count new time when you set other than 1.0 speed while watching video/listening audio


# Start, requesting input data
time_txt_input = input("Введите время видео в формате ЧЧ:ММ: ")

# ввести проверку на ввод минут без часов, несмотря на заданный формат
# set len check
# set print hours&min in text format and axel_mod commented to the end user

axel_mod = input("Введите скорость воспроизведения: ")

# Checking the missclicks
tup_of_missclicks = ',', '?', '/', '@', '<', '>', 'б', 'ю', 'Б', 'Ю', '%', '^', '&', ':', ';'
for i in tup_of_missclicks:
    if axel_mod.find(str(i)):
        axel_mod = axel_mod.replace(str(i), '.')
    elif time_txt_input.find(str(i)):
        time_txt_input = time_txt_input.replace(str(i), ':')

# Converting the acceleration modifier
acceleration_mod = float(axel_mod)

# Find & count minutes in hours and sums them all
clock_sep = time_txt_input.find(":")

num_of_hours = int(time_txt_input[:clock_sep])
num_of_minutes = int(time_txt_input[(clock_sep + 1):])

sum_of_minutes = num_of_hours * 60 + num_of_minutes

# Separation the new sum of minutes onto hours and minutes
time_acceleration = int(sum_of_minutes // acceleration_mod)
if time_acceleration >= 60:
    h_output: int = int(time_acceleration / 60)
    m_output: int = int(time_acceleration % 60)

# Разложение на падежи
print("На скорости", acceleration_mod, "вы просмотрите видео за:", h_output, "час/-ов/-а/", ",", m_output,
      "минут/-ы/-у")
quit()
