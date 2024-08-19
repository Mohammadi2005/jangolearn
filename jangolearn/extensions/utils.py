from . import jalali

def change_to_jalali(time):  #  برای تغییر اطلاعات به شمسی
    time_to_string = f"{time.year},{time.month},{time.day}" # فرمت رو به استرینگ تبدیل میکنه
    time_to_tuple = jalali.Gregorian(time_to_string).persian_tuple()  #  به شمسی تبدیل میکنه

    jmonth = ["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","ابان","اذر","دی","بهمن","سفند"]

    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonth): # enumerate به هر عنصر از ارایه یک اندیس میده و month میشه نام هر عنصر
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output = f"{time_to_list[0]},{time_to_list[1]},{time_to_list[2]} , ساعت , {time.hour}:{time.minute}"
    return output