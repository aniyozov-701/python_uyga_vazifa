# def salom_ber():
#     """Salom beruvchi fungsiya"""
#     print("Asolom alekum!")
#
# salom_ber()

# def salom_ber(ism):
#     """fodyalanuvchi ismini qabul qilib unga salom beruvchi fungsiya"""
#     print(f"Asalomu alekum hurmatli {ism.title()}!")
# salom_ber('hasan')
# print(salom_ber.__doc__)
#
#
#
# salom_ber('beki')
# salom_ber('aji')
# salom_ber('zafar')


# /def ismlar(ism,familiya='valiyov',t_yili):
#     """foydalanuvchining ism va familiyasini chiqarish"""
#     print(f"Foydalanuvchini ismi: {ism.title()}\n"
#           f"foydalanuvchi familiyasi: {familiya.title()}"
#           f"yili: {t_yili}")
# print(ismlar.__doc__)
# ismlar('hali',"kjhiugui", 1993)


# def yosh_hisobla (tugulgan_yil,joriy_yil=2022):
#     """foydalanuvchini tug'ulgan yilidan uni yoshini hisoblaydi."""
#     print(f"siz {joriy_yil-tugulgan_yil} yoshdasiz")
# print(yosh_hisobla.__doc__)
# yosh_hisobla(2004,2500)


# ism_fam degan funksiya yarating. Funksiya parametrlari ism, familiya bo'lsin. Familiyaga deaulft qiymat berib keting.
# Funksiyaga bir agrumentli  hamda ikki argumentli qilib yuklab javobni chiqaring ikkala holatda

def ism_familiya(ism,familiya='zafaripov'):
     """familiyani va ismini qaytaruvchi fungsiya"""
     print(f"salom {ism.title()}\n"
           f"salom {familiya.title()}")
print(ism_familiya.__doc__)
ism_familiya('shexnazar')

ism_familiya("shexnazar","bekijfn")