'''
Máy ra 1 số trong đoạn [1...100]
Người chơi đoán số, chỉ được phép đoán sai 7 lần. Mỗi lần đoán sẽ thông báo số người chơi đoán nhỏ hơn hay lớn hơn số của máy và hiển thị số lần đoán
Game kết thúc khi: Đoán sai quá 7 lần hoặc đoán trúng trước 7 lần.
Sau khi game kết thúc hỏi người chơi có tiếp tục hay không?

A number is randomly chosen in the range [1...100]
The player has to guess the number, with a maximum of 7 wrong guesses. After each guess, the player is informed whether their guess is lower or higher than the chosen number, along with the number of attempts made.
The game ends when the player either guesses the number correctly within 7 attempts or exhausts all 7 attempts. 
After the game ends, ask the player if they want to continue playing.
'''

from random import randrange

while True:
    num = randrange(1, 101)
    print("A number between 1 and 100 has been chosen. You have 7 attempts to guess it.")
    attempts = 0
    for attempts in range(1, 8):
        guess = int(input(f"Attempt {attempts}: Enter your guess: "))
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the number {num} correctly in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all 7 attempts. The correct number was {num}.")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing! Goodbye.")
        break
    