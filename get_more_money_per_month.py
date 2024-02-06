def calc(members = 2, deposit = 2_500_000, rate = 0.175, duration = 6):
    income_per_duration = deposit * rate # rate_int / 100
    duration = 6 # months
    tax = (income_per_duration - 150_000) * 0.13
    return (income_per_duration - tax, tax)


members = 2
deposit = 2_500_000
rate_float = 0.175
duration = 6

fst = calc()
snd = calc()
mono = calc(deposit=5_000_000)

res = 'да' if int(fst[0] + snd[0]) > int(mono[0]) else 'нет'

print(f"""
Вклад:                                                     {deposit:_}
Кол-во вкладчиков                                                  {members}
под процентную ставку:                                        {(rate_float * 100):3.2f}%
налог на проценты свыше 150 000 рублей для 1-го вкладчика:  {fst[1]:_}
налог на проценты свыше 150 000 рублей для 2-го вкладчика:  {snd[1]:_}

итого:
доход за 6 месяцев для 1-го:                               {fst[0]:_}
доход за 1 месяц для 1-го  :                                {(fst[0] / duration):_}

доход за 6 месяцев для 1-го:                               {snd[0]:_}
доход за 1 месяц для 1-го  :                                {(snd[0] / duration):_}


если счет был бы один:
налог на проценты свыше 150 000 рублей для моновклада:      {mono[1]:_}

доход за 6 месяцев для моновклада:                         {mono[0]:_}
доход за 1 месяц для моновклада  :                         {(mono[0] / duration):_}

Выгоднее иметь два вклада чем один ({duration} месяцев): {res} на:      {((fst[0] + snd[0]) - mono[0]):_}

""")
