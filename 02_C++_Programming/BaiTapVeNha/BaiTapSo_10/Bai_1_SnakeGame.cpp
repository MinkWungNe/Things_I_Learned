// Write a C++ program to implement the classic Snake game in the console.
// The game should allow the player to control the snake using the keyboard,
#include <iostream>
#include <conio.h>
#include <windows.h>
using namespace std;

bool gameover;
const int width = 20;
const int height = 17;
int x, y, fruitX, fruitY, score;
int tailX[100], tailY[100]; // snake coordinates
int nTail;

enum eDirecton
{
    STOP = 0,
    LEFT,
    RIGHT,
    UP,
    DOWN
}; // Controls
eDirecton dir;

void Setup()
{
    gameover = false;
    dir = STOP;
    x = width / 2;
    y = height / 2;
    fruitX = rand() % width; // display fruit in a random place
    fruitY = rand() % height;
    score = 0;
}

void Draw()
{
    system("cls");      // Xoá toàn bộ frame cũ để vẽ frame mới
    for (int i = 0; i < width + 2; i++)     // In Tường trên của Game
        cout << "#";
    cout << endl;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (j == 0)                     // In tường bên trái của Game
                cout << "#"; // walls
            if (i == y && j == x)
                cout << "o"; // snake head
            else if (i == fruitY && j == fruitX)
                cout << "@"; // change it to change the fruit
            else
            {
                bool print = false;
                for (int k = 0; k < nTail; k++)
                {
                    if (tailX[k] == j && tailY[k] == i)
                    {
                        cout << "*";    // snake body and tails
                        print = true;
                    }
                }
                if (!print)
                    cout << " ";
            }
            if (j == width - 1)             // In tường bên phải của game
                cout << "#";
        }
        cout << endl;
    }

    for (int i = 0; i < width + 2; i++)     // In tường dưới của game
        cout << "#";
    cout << endl;
    cout << "Score:" << score << endl;
}

void Input()        // Nhận tín hiệu từ bàn phím
{
    if (_kbhit())                   // Bàn phím được bấm
    {
        switch (_getch())           // Nhận tín hiệu và xét trường hợp
        {
        case 'a':                   // Bấm a -> hướng di chuyển thành LEFT
            dir = LEFT;
            break;
        case 'd':                   // Bấm d -> hướng di chuyển thành RIGHT
            dir = RIGHT;
            break;
        case 'w':                   // Bấm w -> hướng di chuyển thành UP
            dir = UP;
            break;
        case 's':                   // Bấm s -> hướng di chuyển thành DOWN
            dir = DOWN;
            break;
        case 'x':                   // Bấm x -> Thoát game
            gameover = true;
            break;
        }
    }
}
void algorithm()
{
    int prevX = tailX[0];   // Lưu toạ độ "trước đó" vào 2 biến prev
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = x;           // Cập nhật toạ độ ĐẦU mới vào mảng         
    tailY[0] = y;      
    for (int i = 1; i < nTail; i++) // cập nhật lại MẢNG TOẠ ĐỘ
    {
        prev2X = tailX[i];  // Lưu toạ độ "trước trước đó" vào 2 biến prev2
        prev2Y = tailY[i];
        tailX[i] = prevX;   // Gắn toạ độ "trước đó" vào mảng ở vị trí i
        tailY[i] = prevY;
        prevX = prev2X;     // Trả toạ độ "trước trước đó" về 2 biến "trước đó" (prev)
        prevY = prev2Y;
    }
    switch (dir)            // Nhận tín hiệu từ Input
    {
    case LEFT:              // Nếu LEFT thì update vị trí mới cho Player    = qua trái ở mỗi khung hình
        x--;
        break;
    case RIGHT:             // Nếu RIGHT thì update vị trí mới cho Player   = qua phải ở mỗi khung hình
        x++;
        break;
    case UP:                // Nếu UP thì update vị trí mới cho Player      = lên trên ở mỗi khung hình
        y--;
        break;
    case DOWN:              // Nếu DOWN thì update vị trí mới cho Player    = xuống dưới ở mỗi khung hình
        y++;
        break;
    default:
        break;
    }
    if (x >= width)         // Nếu player ra khỏi map từ bên trái, dịch chuyển player sang bên phải map
        x = 1;
    else if (x < 0)         // ngược lại
        x = width - 1;
    if (y >= height)        // Nếu player ra khỏi map từ bên trên, dịch chuyển player xuống cuối map
        y = 1;
    else if (y < 0)         // ngược lại
        y = height - 1;
    for (int i = 0; i < nTail; i++)         // Nếu player va chạm với phần thân -> Game Over
        if (tailX[i] == x && tailY[i] == y)
            gameover = true;
    if (x == fruitX && y == fruitY)         // Nếu player ăn được "trái cây", tăng score và spawn 1 quả mới, tăng độ dài player
    {
        score += 10;
        fruitX = rand() % width;
        fruitY = rand() % height;
        nTail++;
    }
}
int main()
{
    Setup();
    while (!gameover)
    {
        Draw();
        Input();
        algorithm();
        Sleep(70);          // Delay mỗi khung hình khoảng 70ms đồng thời chỉnh tốc độ game :))
    }
    return 0;
}