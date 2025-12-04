def get_day_of_week(day_number: int) -> str:
    # if day_number == 1:
    #     day_name = 'Понеділок'
    # elif day_number == 2:
    #     day_name = 'Вівторок'
    # elif day_number == 3:
    #     day_name = 'Середа'
    # elif day_number == 4:
    #     day_name = 'Четвер'
    # elif day_number == 5:
    #     day_name = "П'ятниця"
    # elif day_number in (6, 7):
    #     day_name = 'Вихідний'
    # else:
    #     day_name = "Не вірне значення"
    # return day_name

    # match day_number:
    #     case 1:
    #         day_name = "Понеділок"
    #     case 2:
    #         day_name = "Вівторок"
    #     case 3:
    #         day_name = "Середа"
    #     case 4:
    #         day_name = "Четвер"
    #     case 5:
    #         day_name = "П'ятниця"
    #     case 6 | 7:
    #         day_name = "Вихідний день!"
    #     case _:
    #         day_name = "Не вірне значення"
    # return day_name

    days_of_week = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Вихідний день!",
        7: "Вихідний день!"
    }
    return days_of_week.get(day_number, 'Не вірне значення')



def main():
    print(get_day_of_week(int(input('Введіть номер дня тижня: '))))


if __name__ == "__main__":
    main()
