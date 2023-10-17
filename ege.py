# buyurtma = input("buyurtmani kiriting : ")
# ismlar=[]
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print(ismlar)

buyurtmalar = []
print("Buyurmalaringizni kiriting : ")
n = 1
while True:
    buyurtma_nomi = f"{n} - bizning dukonimizdan nima buyurtimoqchisiz : "
    buyurtma = input(buyurtma_nomi)
    buyurtmalar.append(buyurtma)
    buyurtmaberishni_istaysizmi = input(("yana buyurtma berishni istaysizmi? (yes/no)"))
    if buyurtmaberishni_istaysizmi == "yes":
        n += 1
        continue
    else:
        break
print("buyurtmalaringiz ro`yxati :")
for buyurtma in buyurtmalar:
    print(buyurtma.title())
