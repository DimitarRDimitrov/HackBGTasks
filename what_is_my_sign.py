def what_is_my_sign(date, month):
    if month == 1:
        if date > 20:
            print("Aquarius")
        else:
            print("Capricorn")
    elif month == 2:
        if date > 19:
            print("Pisces")
        else:
            print("Aquarius")
    elif month == 3:
        if date > 20:
            print("Aries")
        else:
            print("Pisces")
    elif month == 4:
        if date > 20:
            print("Taurus")
        else:
            print("Aries") 
    elif month == 5:
        if date > 21:
            print("Gemini")
        else:
            print("Taurus")
    elif month == 6:
        if date > 22:
            print("Cancer")
        else:
            print("Gemini")
    elif month == 7:
        if date > 22:
            print("Leo")
        else:
            print("Cancer")
    elif month == 8:
        if date > 22:
            print("Virgo")
        else:
            print("Leo")
    elif month == 9:
        if date > 23:
            print("Libra")
        else:
            print("Virgo")
    elif month == 10:
        if date > 23:
            print("Scorpio")
        else:
            print("Libra")
    elif month == 11:
        if date > 22:
            print("Sagittarius")
        else:
            print("Scorpio")
    elif month == 12:
        if date > 21:
            print("Capricorn")
        else:
            print("Sagittarius")

print(what_is_my_sign(28, 1))
print(what_is_my_sign(8, 5))
