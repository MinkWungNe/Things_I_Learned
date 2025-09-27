// Write a C++ program to represent a directed graph using an adjacency matrix.
// Implement a function to transpose the adjacency matrix of the graph.

#include <iostream>
#include <vector>
using namespace std;

void addEdge(vector<vector<int>> &mat, int i, int j)
{
    mat[i][j] = 1;  // Đồ thị có hướng nên vào = -1 | ra = 1
    mat[j][i] = -1;
}

// Hiển thị ma trận
void printMatrix(vector<vector<int>> &mat)
{
    int V = mat.size();
    for (int i = 0; i < V; i++)
    {
        cout << i << "| ";
        for (int j = 0; j < V; j++)
        {
            cout << mat[i][j];
            if (mat[i][j] == 1 || mat[i][j] == 0)
            {
                cout << "  ";
            }
            else
            {
                cout << " ";
            }
        }
        cout << endl;
    }
}

// Chuyển vị ma trận
vector<vector<int>> ChuyenViMaTran(vector<vector<int>> &mat)
{
    int size = mat.size();
    vector<vector<int>> maTranChuyenVi(size, vector<int>(size, 0)); // Khai báo vector để chuyển vị
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            maTranChuyenVi[j][i] = mat[i][j];
        }
    }
    return maTranChuyenVi;
}

int main()
{

    // Tạo đồ thị 4 đỉnh
    int V = 4;
    vector<vector<int>> mat(V, vector<int>(V, 0));  // để in ma trận
    vector<vector<int>> matrixDaChuyenVi; // để lưu ma trận đã chuyển vị

    // Them canh
    addEdge(mat, 0, 1);
    addEdge(mat, 0, 2);
    addEdge(mat, 1, 2);
    addEdge(mat, 2, 3);

    // Chuyển vị
    matrixDaChuyenVi = ChuyenViMaTran(mat);
    
    cout << "Ma tran: " << endl;
    printMatrix(mat);

    cout << "Ma tran da chuyen vi: " << endl;
    printMatrix(matrixDaChuyenVi);

    return 0;
}