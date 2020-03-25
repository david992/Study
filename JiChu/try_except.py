def div_appple(n):
    print("%d个苹果想分给几个人？" % n)
    s = input("人数：")
    cnt = int(s)
    try:
        result = n / cnt
        print("每个人分了%d个苹果" % result)
    except ZeroDivisionError:
        print("程序出现ZeroDivisionError错误")
try:
    print("开始分苹果")
    div_appple(10)
    print("结束分苹果")
# except (ValueError, ZeroDivisionError):
#     print('程序出现错误')
except ValueError as Error:
    print("程序出现ValueError错误")
    print("错误信息是：",Error)
except ZeroDivisionError as Error:
    print("程序出现被零除错误")
    print("错误信息是：", Error)
except:
    print("发生其他错误")
else:
    print("程序未出现异常")
finally:
    print("finally一定会执行")
print("程序正常退出")