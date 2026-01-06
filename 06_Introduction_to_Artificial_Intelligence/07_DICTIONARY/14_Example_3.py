'''
3. Gia vị và thảo mộc. Bạn làm việc trong một cửa hàng tạp hóa bán gia vị và thảo mộc.
Sau đây là các loại gia vị và thảo mộc trong cửa hàng:
spices_herbs = ["basil", "cinnamon", "licorice", "mint", "rosemary", "thyme",
"cardamom", "turmeric", "cilantro", "oregano", "pepper", "chili", "dill", "cayenne
pepper", "ginger", "garlic", "marjoram", "nutmeg", "sage", "saffron", "star anise", "bay
leaves"]
a. Bạn phải thay đổi nhãn trên hộp đựng và làm cho chúng trông hiện đại hơn. Chiều dài
của nhãn mới tỷ lệ thuận với chiều dài của từ được viết trên đó. Tạo một từ điển trong đó
khóa là độ dài của từ và giá trị là danh sách các từ có độ dài đó.
b. Bạn cần biết cần cắt bao nhiêu nhãn cho mỗi độ dài. Tạo một từ điển khác trong đó
khóa là độ dài của từ theo thứ tự tăng dần, và giá trị là số nhãn bạn phải cắt cho mỗi độ
dài.
c. Nhãn phổ biến nhất là gì? Nó tương ứng với bao nhiêu chữ cái? Hãy tính xem!
Tiếng việt: spices_herbs = ["húng quế", "quế", "cam thảo", "bạc hà", "hương thảo", "húng
tây", "thảo mộc", "nghệ", "rau mùi", "kinh giới cay", "ớt", "ớt", "thì là", "ớt cayenne",
"gừng", "tỏi", "kinh giới cay", "nhục đậu khấu", "xô thơm", "nghệ tây", "đại hồi", "lá
nguyệt quế"]
'''

spices_herbs = ["basil", "cinnamon", "licorice", "mint", "rosemary", "thyme",
"cardamom", "turmeric", "cilantro", "oregano", "pepper", "chili", "dill",
"cayennepepper", "ginger", "garlic", "marjoram", "nutmeg", "sage", "saffron",
"star anise", "bayleaves"]

# a. Make a dictionary with key is length and values is string with that length
lableLengthDict = {}
for herb in spices_herbs:
    if len(herb) not in lableLengthDict.keys():
        lableLengthDict[len(herb)] = [herb]
    else:
        lableLengthDict[len(herb)].append(herb)

print('Length - Herb dictionary ----------------------------------------')
for k, v in lableLengthDict.items():
    print(k, ":", v)

# b. Make a dictionary with key is length and value is amount of lable it need to cut
lableAmountDict = {}
for lengthKey in lableLengthDict.keys():
    lableAmountDict[lengthKey] = len(lableLengthDict[lengthKey])

print('Length - Amount dictionary --------------------------------------')
for k, v in lableAmountDict.items():
    print(k, ":", v)
    
# c. DO something