'''
Tách lấy tên bài hát
Cho một chuỗi là đường dẫn của 1 file nhạc, ví dụ: d:\\music\muabui.mp3
Hãy viết 2 hàm để:
-	Lấy ra muabui.mp3
-	Lấy ra muabui
Lưu ý đường dẫn bài hát là bất kỳ. Nên khi truyền vào bài hát nào thì lấy chính xác theo bài hát đó.
------------------------------------------------
Attract song name
Given a string representing the path of a music file, for example: d:\\music\muabui.mp3
Write 2 functions to:
- Extract muabui.mp3
- Extract muabui
Note that the music file path can be any. So when passing in any song, extract exactly according to that song.
'''

def get_full_song_name(file_path):
    # Lấy tên file đầy đủ (bao gồm phần mở rộng)
    return file_path.split('\\')[-1]

def get_song_name(file_path):
    # Lấy tên file không bao gồm phần mở rộng
    full_name = get_full_song_name(file_path)
    return full_name.split('.')[0] 

# Ví dụ sử dụng
file_path = "d:\\music\\muabui.mp3"
print(get_full_song_name(file_path))  # Output: muabui.mp3
print(get_song_name(file_path))       # Output: muabui