"""
Bu dastur yangi oshhonalar uchun elektron menyu vazifasini bajaradi
"""

salomlashish = input("Assalomu alayko'm Mr.Five Ozuqa do'koniga hush kelibsiz. Buyurtma qilishni hohlaysizmi: ")

if salomlashish == "Ha":
    print("Milliy Taomlar: \n"
          "Sho'rva = 12000 so'm \n"
          "Norin(1-Po'rsiya uchun) = 24000 so'm \n"
          "Shashlik(Qiyma) = 10000 so'm \n" 
          "Shashlik(Jigar) = 12000 so'm \n"
          "Shashlik(Jaz) = 14000 so'm \n"
          "Menuimizda xozircha shular")



tanlash = input("Tanlang: ")

if tanlash == "Sho'rva":
    son = input("Nechta kosa sho'rva xarid qilmoqchisiz")
    if son == "2":
        print(f"Summa {12000 + 12000}ming so'm")
    elif son == "1":
        print(f"Summa 12000 ming so'm")
    elif son == "3":
        print(f"Summa {12000 * 3}ming so'm")
    elif son == "4":
        print(f"Summa {12000 * 4}ming so'm")
    elif son == "5":
        print(f"Summa {12000 * 4}ming so'm")
    elif son == "6":
        print(f"Summa {12000 * 5}ming so'm")
    elif son == "7":
        print(f"Summa {12000 * 7}ming so'm")
    elif son == "8":
        print(f"Summa {12000 * 3}ming so'm")
    elif son == "9":
        print(f"Summa {12000 * 3}ming so'm")
    elif son == "10":
        print(f"Summa {12000 * 3}ming so'm")
    elif son >= "10":
        print("Maksimal 10tagacha buyurtma bera olasiz")
    raqam = input("Bizga raqamingizni qoldiring: ")
    print("Siz bilan bog'lanishadi")

elif tanlash == "Norin":
    norin_son = input("Necha porsiya norin olmoqchisiz(Son ko'rinishida yozing)")
    if norin_son == "1":
        print("Summa 24000ming so'm")
    elif norin_son == "2":
        print(f"Summa {24000 * 2}")
    elif norin_son == "3":
        print(f"Summa {24000 * 3}")
    elif norin_son == "4":
        print(f"Summa {24000 * 4}")
    elif norin_son == "5":
        print(f"Summa {24000 * 5}")
    elif norin_son >= "5":
        print("Kechirasiz 5 porsiyadan ortig'i ko'p")
    raqam = input("Bizga raqamingizni qoldiring: ")
    print("Siz bilan bog'lanishadi")

elif tanlash == "Shashlik":
    turi = input("Qanday turdagi shashlik harid qilmoqchisiz: ")
    if turi == "Qiyma":
        shashlik_soni = input("Nechta Shashlik sotib olmoqchisiz: ")
        if shashlik_soni == "1":
            print("Summa 10000ming so'm")
        elif shashlik_soni == "2":
            print(f"Summa {10000 * 2}")
        elif shashlik_soni == "3":
            print(f"Summa {10000 * 3}")
        elif shashlik_soni == "4":
            print(f"Summa {10000 * 4}")
        elif shashlik_soni == "5":
            print(f"Summa {10000 * 5}")
        elif shashlik_soni == "6":
            print(f"Summa {10000 * 6}")
        elif shashlik_soni == "7":
            print(f"Summa {10000 * 7}")
        elif shashlik_soni == "8":
            print(f"Summa {10000 * 8}")
        elif shashlik_soni == "9":
            print(f"Summa {10000 * 9}")
        elif shashlik_soni == "10":
            print(f"Summa {10000 * 10}")
        elif shashlik_soni == "11":
            print(f"Summa {10000 * 11}")
        elif shashlik_soni == "12":
            print(f"Summa {10000 * 12}")
        elif shashlik_soni == "13":
            print(f"Summa {10000 * 13}")
        elif shashlik_soni == "14":
            print(f"Summa {10000 * 14}")
        elif shashlik_soni == "15":
            print(f"Summa {10000 * 15}")
        elif shashlik_soni >= "15":
            print("Kechirasiz 15tadan ortiq bera olmayman")
        raqam = input("Bizga raqamingizni qoldiring: ")

        print("Siz bilan bog'lanishadi")

    elif turi == "Jigar":
        jigar_soni = input("Nechta Jigar shashlik xarid qilmoqchisiz: ")
        if jigar_soni == "1":
            print("Summa 11000ming so'm")
        elif jigar_soni == "2":
            print(f"Summa {11000 * 2}")
        elif jigar_soni == "3":
            print(f"Summa {11000 * 3}")
        elif jigar_soni == "4":
            print(f"Summa {11000 * 4}")
        elif jigar_soni == "5":
            print(f"Summa {11000 * 5}")
        elif jigar_soni == "6":
            print(f"Summa {11000 * 6}")
        elif jigar_soni == "7":
            print(f"Summa {11000 * 7}")
        elif jigar_soni == "8":
            print(f"Summa {11000 * 8}")
        elif jigar_soni == "9":
            print(f"Summa {11000 * 9}")
        elif jigar_soni == "10":
            print(f"Summa {11000 * 10}")
        elif jigar_soni == "11":
            print(f"Summa {11000 * 11}")
        elif jigar_soni == "12":
            print(f"Summa {11000 * 12}")
        elif jigar_soni == "13":
            print(f"Summa {11000 * 13}")
        elif jigar_soni == "14":
            print(f"Summa {11000 * 14}")
        elif jigar_soni == "15":
            print(f"Summa {11000 * 15}")
        elif jigar_soni >= "15":
            print("Kechirasiz 15tadan ortiq xarid qila olmaysiz!")
        raqam = input("Bizga raqamingizni qoldiring: ")

        print("Siz bilan bog'lanishadi")
    elif turi == "Jaz":
        jaz_soni = input("Nechta Jaz shashlik sotib olmoqchisiz: ")
        if jaz_soni == "1":
            print("Summa 14000ming so'm")
        elif jaz_soni == "2":
            print(f"Summa {14000 * 2}")
        elif jaz_soni == "3":
            print(f"Summa {14000 * 3}")
        elif jaz_soni == "4":
            print(f"Summa {14000 * 4}")
        elif jaz_soni == "5":
            print(f"Summa {14000 * 5}")
        elif jaz_soni == "6":
            print(f"Summa {14000 * 6}")
        elif jaz_soni == "7":
            print(f"Summa {14000 * 7}")
        elif jaz_soni == "8":
            print(f"Summa {14000 * 8}")
        elif jaz_soni == "9":
            print(f"Summa {14000 * 9}")
        elif jaz_soni == "10":
            print(f"Summa {14000 * 10}")
        elif jaz_soni == "11":
            print(f"Summa {14000 * 11}")
        elif jaz_soni == "12":
            print(f"Summa {14000 * 12}")
        elif jaz_soni == "13":
            print(f"Summa {14000 * 13}")
        elif jaz_soni == "14":
            print(f"Summa {14000 * 14}")
        elif jaz_soni == "15":
            print(f"Summa {14000 * 15}")
        elif jaz_soni >= "15":
            print("Kechirasiz boshqalar ham yeyishi kerak!")
        raqam = input("Bizga raqamingizni qoldiring: ")

        print("Siz bilan bog'lanishadi")





