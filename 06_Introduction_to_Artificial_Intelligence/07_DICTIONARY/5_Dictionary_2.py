'''
Bạn của bạn đang lên kế hoạch cho một chuyến đi đến Thụy Sĩ và anh ấy đã hỏi bạn
một số mẹo. Bạn bắt đầu với một từ điển trống để điền vào:
'''
tips = {}

'''
Anh ấy muốn ghé thăm một số thành phố và thưởng thức ẩm thực đặc trưng. Vì vậy, bạn
có thể đưa ra một số gợi ý sau:
'''
tips['cities'] = ['Bern', 'Lucern']
tips['food'] = ['chocolate', 'reclette']

# Vì thời gian lưu trú của anh ấy là bốn ngày, bạn hãy thêm hai thành phố nữa và hai món ăn nữa:
# add two kind of 'food' and two 'cities'
tips['cities'].append('Lugano')
tips['cities'] += ['Geneva']

tips.get('food').append('onion tarte')
tips['food'] = tips.get('food') + ['fondue']

# Print the tips
for k, v in tips.items():    # k: key - v: value
    print(k, v)

# Even more fancy print
for k, v in tips.items():
    print("{:>6}: {}".format(k, v))