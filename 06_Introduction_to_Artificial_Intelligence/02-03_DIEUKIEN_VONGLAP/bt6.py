x = int(input('Nhập x: '))
y = str(x)

secondWord = ["Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi", "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]
firstWordwithoutSecondWord = ["Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
firstWordwithSecondWord = ["Mốt", "Hai", "Ba", "Bốn", "Lăm", "Sáu", "Bảy", "Tám", "Chín"]

## Dựa vào x in ra chuỗi số bằng chữ
if x > 100 or x < 0:
    print('x KHÔNG HỢP LỆ')
else:
    if x < 10:  ## 1 chữ số
        print(firstWordwithoutSecondWord[x-1])
    else:  ## 2 chữ số
        if x % 10 == 0:  ## 2 chữ số và là bội của 10
            print(secondWord[int(y[0])-1])
        else:  ## 2 chữ số và không là bội của 10
            if y[0] == '1':  ## Số hàng chục là 1
                print(f"{secondWord[0]} {firstWordwithSecondWord[int(y[1])-1]}")
            else:  ## Số hàng chục khác 1
                print(f"{secondWord[int(y[0])-1]} {firstWordwithoutSecondWord[int(y[1])-1]}")