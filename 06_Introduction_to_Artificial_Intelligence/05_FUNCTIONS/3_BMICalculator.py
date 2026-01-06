'''
Gọi BMI là chỉ số cân đối cơ thể. Yêu cầu đầu vào nhập là chiều cao và cân nặng, hãy cho  biết người này như thế nào, biết rằng:
BMI = weight/(height^2)
Phân loại:
- 18.5 <= BMI <= 24.9: Bình thường
- 25 <= BMI <= 29.9: Hơi Béo
- 30 <= BMI <= 34.9: Béo Phì Cấp Độ 1
- 35 <= BMI <= 39.9: Béo Phì Cấp Độ 2
- BMI >= 40: Béo Phì Cấp độ 3
Nguy cơ bệnh:
- BMI < 18.5: Thấp
- 18.5 <= BMI <= 24.9: Trung Bình
- 25 <= BMI <= 29.9: Cao
- 30 <= BMI <= 34.9: Cao
- 35 <= BMI <= 39.9: Rất cao
- BMI >= 40: Nguy Hiểm
'''
'''
Let BMI be the body mass index. The input requirements are height and weight, please tell how this person is, knowing that:
BMI = weight/(height^2)
Classification:
- 18.5 <= BMI <= 24.9: Normal
- 25 <= BMI <= 29.9: Slightly Fat
- 30 <= BMI <= 34.9: Obesity Level 1
- 35 <= BMI <= 39.9: Obesity Level 2
- BMI >= 40: Obesity Level 3
Disease risk:
- BMI < 18.5: Low
- 18.5 <= BMI <= 24.9: Average
- 25 <= BMI <= 29.9: High
- 30 <= BMI <= 34.9: High
- 35 <= BMI <= 39.9: Very high
- BMI >= 40: Dangerous
'''

def BMI(height,weight):
    return weight/(height**2)
def PhanLoai(bmi):
    if bmi<18.5:
        return "Gầy"
    elif bmi<=24.9:
        return "Bình thường"
    elif bmi<=29.9:
        return "Hơi Béo"
    elif bmi<=34.9:
        return "Béo Phì Cấp Độ 1"
    elif bmi<=39.9:
        return "Béo Phì Cấp Độ 2"
    else:
        return "Béo Phì Cấp độ 3"
def NguyCoBenh(bmi):
    if bmi<18.5:
        return "Thấp"
    elif bmi<=24.9:
        return "Trung Bình"
    elif bmi<=29.9:
        return "Cao"
    elif bmi<=34.9:
        return "Cao"
    elif bmi<=39.9:
        return "Rất cao"
    else:
        return "Nguy Hiểm"
print("Nhập vào chiều cao:")
height=float(input())
print("Nhập vào cân nặng:")
weight=float(input())
bmi=BMI(height,weight)
print("BMI của bạn=",bmi)
print("Phân loại bạn=",PhanLoai(bmi))
print("Nguy cơ bệnh của Thím=",NguyCoBenh(bmi))
