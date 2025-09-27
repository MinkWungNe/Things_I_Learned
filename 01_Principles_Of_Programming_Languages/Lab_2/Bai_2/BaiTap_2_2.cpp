//Cho 2 người chơi kéo bao búa. Viết chương trình kiểm tra kết quả trò chơi. (1-Kéo, 2-Búa, 3-Bao)
//Let's play rock-paper-scissors with two players. Write a program to check the result of the game. (1-Rock, 2-Paper, 3-Scissors)
#include <iostream>
using namespace std;

int n1,n2;
string player1 = "Nguoi choi 1 ";
string player2 = "Nguoi choi 2 ";


void PlayerChoose(int player, string playernum)
{
    if (player == 1)
    {
        cout << playernum << "chon Keo" << endl;
    }
    else if (player == 2)
    {
        cout << playernum << "chon Bua"<< endl;
    }
    else
    {
        cout << playernum << "chon Bao"<< endl;
    }
}
int Ketqua()
{
    if (n1 == n2)
    {
        cout <<"Ban da hoa!" << endl;
    }
    else if (n1 == 1 && n2 == 2 || n1 == 2 && n2 == 3 || n1 == 3 && n2 == 1)
    {
        cout << "Nguoi_Choi_1 Thang!" << endl;
    }
    else if (n1 == 3 && n2 == 2 || n1 == 1 && n2 == 3 || n1 == 2 && n2 == 1 )
    {
        cout << "Nguoi_Choi_2 Thang!" << endl;
    }
    return 0;
}

int main()
{
    cout << "Moi Nguoi_Choi_1 chon:" << endl
    << "1.Keo" << endl
    << "2.Bua" << endl
    << "3.Bao" << endl;
    cin >> n1;
    PlayerChoose(n1,player1);
    cout << "Moi Nguoi_Choi_2 chon:" << endl
    << "1.Keo" << endl
    << "2.Bua" << endl
    << "3.Bao" << endl;
    cin >> n2;
    PlayerChoose(n2,player2);
    Ketqua();
    return 0;  
}