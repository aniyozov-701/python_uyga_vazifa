# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism_= f"{ism} {familiya}"
#     return toliq_ism_
#
# talaba1 = toliq_ism_yasa(ism:'olim', familiya:'hakimov')
# talaba2 = toliq_ism_yasa(ism:'hakim', familiya:'olimov')
#
# print(f"{talaba1} {talaba2}")


# def toliq_ism_yasa(ism, familiya, otasining ismi=''):
# """Toliq ism qaytaruvchi funksiya"""
# if otasining_ismi:
#     toliq_ism = f"{ism} {otasining ismi} {familiya}"
# else:
#     toliq_ism = f"{ism} {familya}"
# return toliq_ism.title()
#
# talaba1 = toliq_ism_yasa(ism:'olim', familiya:'hakimov')
# talaba2 = toliq_ism_yasa(ism:'hakim', familiya:'olimov', otasining ismi:'abrorovich')
#
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#     avto_= {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'karobka':karobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto_
# #
# # avto1 = avto_info('GM','Malibu', 'Qora', 'Avtomat', 2018 )
# # avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanik', 2016, 15000 )
# # avtolar = [avto1, avto2]
# # print('Onlayn bozordagi')
#
#
# # def oraliq(min, max):
# #     sonlar = []
# #     while min<max:
# #         sonlar.append(min)
# #         min += 1
# #     return sonlar
# #
# # print(oraliq(0, 10))
# # print(oraliq(12, 22))
#
#
# print("Saytimizdagi avtolar royxatini shakllantiramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi malumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi :")
#     model = input("Modeli:")
#     rangi = input("Rangi:")
#     karobka = input("Karobka:")
#     yili = input("Ishlab chiqarilgan yili:")
#     narhi = input("Narhi:")
#
#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
#
#     javob = input("Yana avto qoshasizmi? (yes/no):")
#     if javob == 'no':
#         break
# #         print(avtolar)
#
# print(avto_info)

