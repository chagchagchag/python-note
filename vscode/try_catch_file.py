try:
    fd = open("input.txt", mode="a", encoding="utf-8")
    fd.write('aaaaa')
except Exception as e:
    print("예외 발생", e)
finally:
    fd.close()