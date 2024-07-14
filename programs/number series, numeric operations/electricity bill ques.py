units = int(input("please enter the number of units you consumed in a month"))
days=int(input("Enter number of days: "))
fixedcharge = 150
if (units <= 100):
    payAmount = units * 0.43

elif (100 < units <= 200):
    payAmount = units * 0.67

elif (200 < units <= 350):
    payAmount = units * 0.92
elif units >= 450:
    payAmount = units * 1.25
total = payAmount + fixedcharge
if days <= 7:
    discount = 0.03 * total
    total = total - discount
print("\nElecticity bill=%.2f" % total)
