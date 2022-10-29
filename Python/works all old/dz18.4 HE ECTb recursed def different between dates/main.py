def leapYear(year):                 #проверка на високосный год
    if year % 4 == 0:
        return False
    else:
        return True


def daysFromDate(day1, month1, year1, day2, month2, year2):
    days = 0
    if year1 > year2:                                                                           #за основу идут переменные которые оканчиваются на "1" по этому
        day1, month1, year1, day2, month2, year2 = day2, month2, year2, day1, month1, year1     #при вводе даты "Д1 М1 Г1 > Д2 М2 Г2" они меняются местами
    elif year1 == year2:
        if month1 > month2:
            day1, month1, year1, day2, month2, year2 = day2, month2, year2, day1, month1, year1
        elif month1 == month2:
            if day1 > day2:
                day1, month1, year1, day2, month2, year2 = day2, month2, year2, day1, month1, year1
            elif day1 == day2:
                return print("Дата одинаковая")

    while True:                             #само решение задачи
        if year1 < year2:                   # НЕ ПОДСЧИТЫВАЕТ последний день включительно по этому в конце return days + 1
            if leapYear(year1):
                if month1 < 12:
                    if 1 <= month1 <= 8:
                        if month1 % 2 == 1:
                            if day1 == 31:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 31:
                                day1 += 1
                                days += 1
                        elif month1 == 2:
                            if day1 == 29:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 29:
                                day1 += 1
                                days += 1
                        elif month1 % 2 == 0 and month1 != 2:
                            if day1 == 30:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 30:
                                day1 += 1
                                days += 1
                    elif 9 <= month1 <= 12:
                        if month1 % 2 == 1:
                            if day1 == 30:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 30:
                                day1 += 1
                                days += 1
                        elif month1 % 2 == 0:
                            if day1 == 31:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 31:
                                day1 += 1
                                days += 1

                elif month1 == 12:
                    if day1 == 31:
                        day1 = 1
                        month1 = 1
                        year1 += 1
                        days += 1
                    elif day1 < 31:
                        day1 += 1
                        days += 1

            else:
                if month1 < 12:
                    if 1 <= month1 <= 8:
                        if month1 % 2 == 1:
                            if day1 == 31:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 31:
                                day1 += 1
                                days += 1
                        elif month1 % 2 == 0:
                            if day1 == 30:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 30:
                                day1 += 1
                                days += 1
                    elif 9 <= month1 <= 12:
                        if month1 % 2 == 1:
                            if day1 == 30:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 30:
                                day1 += 1
                                days += 1
                        elif month1 % 2 == 0:
                            if day1 == 31:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 31:
                                day1 += 1
                                days += 1

                elif month1 == 12:
                    if day1 == 31:
                        day1 = 1
                        month1 = 1
                        year1 += 1
                        days += 1
                    elif day1 < 31:
                        day1 += 1
                        days += 1

        elif year1 == year2:
            if leapYear(year1):
                if month1 < month2:
                    if 1 <= month1 <= 8:
                        if month1 % 2 == 1:
                            if day1 == 31:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 31:
                                day1 += 1
                                days += 1
                        elif month1 == 2:
                            if day1 == 29:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 29:
                                day1 += 1
                                days += 1
                        elif month1 % 2 == 0 and month1 != 2:
                            if day1 == 30:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 30:
                                day1 += 1
                                days += 1
                    elif 9 <= month1 <= 12:
                        if month1 % 2 == 1:
                            if day1 == 30:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 30:
                                day1 += 1
                                days += 1
                        elif month1 % 2 == 0:
                            if day1 == 31:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 31:
                                day1 += 1
                                days += 1

                elif month1 == month2:
                    if day1 < day2:
                        day1 += 1
                        days += 1
                    elif day1 == day2:
                        return days+1

            else:
                if month1 < month2:
                    if 1 <= month1 <= 8:
                        if month1 % 2 == 1:
                            if day1 == 31:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 31:
                                day1 += 1
                                days += 1
                        elif month1 % 2 == 0:
                            if day1 == 30:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 30:
                                day1 += 1
                                days += 1
                    elif 9 <= month1 <= 12:
                        if month1 % 2 == 1:
                            if day1 == 30:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 30:
                                day1 += 1
                                days += 1
                        elif month1 % 2 == 0:
                            if day1 == 31:
                                day1 = 1
                                month1 += 1
                                days += 1
                            elif day1 < 31:
                                day1 += 1
                                days += 1

                elif month1 == month2:
                    if day1 < day2:
                        day1 += 1
                        days += 1
                    elif day1 == day2:
                        return days+1

print(daysFromDate(1, 1, 2001, 31, 12, 2001))