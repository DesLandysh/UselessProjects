def calc(deposit, duration, members, rate):
    outcome_per_duration = deposit * rate # rate_int / 100
    duration = 6 # months
    tax = (outcome_per_duration - 150_000) * 0.13
    return (outcome_per_duration - tax, tax)


members = 2
deposit = 2_500_000
rate_float = 0.175
duration = 6

def run():

    fst_outcome, fst_tax = calc(members, deposit, rate_float, duration)
    snd_outcome, snd_tax = calc(members, deposit, rate_float, duration)
    mono_outcome, mono_tax = calc(deposit=deposit*2)

    res = 'да' if int(fst_outcome + snd_outcome) > int(mono_outcome) else 'нет'

    print(f"""
    Вклад:                                                     {deposit:_}
    Кол-во вкладчиков                                                  {members}
    под процентную ставку:                                        {(rate_float * 100):3.2f}%
    налог на проценты свыше 150 000 рублей для 1-го вкладчика:  {fst_tax:_}
    налог на проценты свыше 150 000 рублей для 2-го вкладчика:  {snd_tax:_}

    итого:
    доход за 6 месяцев для 1-го:                               {fst_outcome:_}
    доход за 1 месяц для 1-го  :                                {fst_outcome / duration:_}

    доход за 6 месяцев для 1-го:                               {snd_outcome:_}
    доход за 1 месяц для 1-го  :                                {snd_outcome / duration:_}


    если счет был бы один:
    налог на проценты свыше 150 000 рублей для моновклада:      {mono_tax:_}

    доход за 6 месяцев для моновклада:                         {mono_outcome:_}
    доход за 1 месяц для моновклада  :                         {mono_outcome / duration:_}

    Выгоднее иметь два вклада чем один ({duration} месяцев): {res} на:      {(fst_outcome + snd_outcome) - mono_outcome:_}

    """)


if __name__ == "__main__":
    run()