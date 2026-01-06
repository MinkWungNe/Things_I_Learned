'''
Hãy xây dựng một chương trình quản lý thư viện với các yêu cầu sau:
1.	Xây dựng các lớp sau:
    o	Lớp Book có các thuộc tính:
        -	book_id (mã sách)
        -	title (tên sách)
        -	author (tác giả)
        -	price (giá bán)
    o	Thêm phương thức:
        -	display_info() để in thông tin sách.
    o	Lớp Library có thuộc tính:
        -	books: danh sách các đối tượng Book.
    o	Thêm các phương thức:
        -	add_book(book): thêm sách vào thư viện.
        -	search_by_author(author_name): trả về danh sách các sách của tác giả đó.
        -	get_total_value(): tính tổng giá trị của tất cả các sách trong thư viện.
2.	Viết chương trình chính (main):
    o	Tạo ít nhất 3 đối tượng Book.
    o	Thêm chúng vào Library.
    o	In ra toàn bộ thông tin sách.
    o	Tìm và in ra các sách của tác giả "Nguyễn Nhật Ánh".
    o	In tổng giá trị của các sách trong thư viện.
'''

# 1. Build class
class Book:
    def __init__(self, book_id = "", title = "", author = "", price = ""):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
    
    def displayInfo(self):
        print("ID: {:s}\nTitle: {:s}\nAuthor: {:s}\nPrice: {:.2f}\n".format(self.book_id, self.title, self.author, self.price))
        
class Library:
    def __init__(self, books = []):
        self.books = books
        
    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            
    def search_by_author(self, author_name):
        for book in self.books:
            if book.author == author_name:
                book.displayInfo()

    def get_total_value(self):
        sum = 0
        for book in self.books:
            sum += book.price
        return sum

# -------- TEST ---------
book1 = Book('1', 'Book1', 'Nguyễn Nhật Ánh', 20000)
book2 = Book('2', 'Book2', 'Nguyễn Nhật Ánh', 25000)
book3 = Book('3', 'Book3', 'Chi', 1000)

lib = Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

print('---------- All books Info -----------------')
for book in lib.books:
    book.displayInfo()

print('---------- Book by Nguyễn Nhật Ánh --------')
lib.search_by_author('Nguyễn Nhật Ánh')
print('Total Books Value:', lib.get_total_value())

#Note: Ôn thêm 'Danh sách', 'từ điển'.
# Không cần ôn prolog

