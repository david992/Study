# 判断闰年
# 四年一闰  每百年不闰 每400年闰
Y=int(input("年份："))
if (Y % 4 ==0 and Y % 100 != 0) or Y % 400 ==0:
    print(Y,"年是闰年")
else:
    print(Y, "年不是闰年")