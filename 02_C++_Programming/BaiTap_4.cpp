// We have a directed graph represented by an adjacency matrix.
// Write a function to check if the adjacency matrix is symmetric.

#include <iostream>
#include <vector>
using namespace std;

void addEdge(vector<vector<int>> &mat, int i, int j)
{
    mat[i][j] = 1;  // Đồ thị có hướng nên vào = -1 | ra = 1
    mat[j][i] = -1;
}

// Kiểm tra đối xứng (nếu ma trận = ma trận chuyển vị thì = TRUE)
bool checkSymmetry(vector<vector<int>> &mat)
{
    int size = mat.size();
    for (int i = 0; i < size; ++i) 
    {
        for (int j = 0; j < size; ++j) 
        {
            if (mat[i][j] != mat[j][i]) // Chạy từng phần tử, nếu phần tử đối xứng khác -> FALSE
            {
                return false;   
            }
        }
    }
    return true;    // Chạy hết ma trận, không có phần tử khác -> TRUE
}

int main()
{

    // Tạo đồ thị 4 đỉnh
    int V = 4;
    vector<vector<int>> mat(V, vector<int>(V, 0));  // để in ma trận

    // Them canh
    addEdge(mat, 0, 1);
    addEdge(mat, 0, 2);
    addEdge(mat, 1, 2);
    addEdge(mat, 2, 3);
    
    cout << "Ket qua kiem tra: " << endl;
    if (checkSymmetry(mat)) // TRUE
    {
        cout << "Ma tran doi xung!" << endl;
    }
    else
    {
        cout << "Ma tran khong doi xung!" << endl;
    }



    return 0;
}