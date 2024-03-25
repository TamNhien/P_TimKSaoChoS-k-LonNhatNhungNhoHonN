n = int(input("Nhập vào số nguyên dương n : "))

k, S = 0, 0
while (S := S + (k := k + 1)) <= n:
    pass

print("Giá trị của k sao cho S(k) lớn nhất nhưng nhỏ hơn n là : ", k - 1)

