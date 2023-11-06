def ctr_to_percentage(ctr):
    percentage = ctr * 100
    return percentage

ctr1 = 0.05
ctr2 = 0.10

percentage1 = ctr_to_percentage(ctr1)
percentage2 = ctr_to_percentage(ctr2)

print(f"CTR {ctr1} correspond à {percentage1}%")
print(f"CTR {ctr2} correspond à {percentage2}%")