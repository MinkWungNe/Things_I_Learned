/*
    Write a C++ program to read the candidates' names from the file candData.txt and store them in an array. 
    Then, read the voting data from the file voteData.txt, which contains the candidate's name, region number,
    and the number of votes received. Store this data in a two-dimensional array where rows represent candidates
    and columns represent regions. Finally, calculate the total votes for each candidate and store them in
    a one-dimensional array. Print the candidates' names, their votes by region, and their total votes.
    Assume there are 6 candidates and 4 regions.
    Note: Ensure to handle file reading errors and validate the data format in the files.
*/
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream Input;
    ofstream Output;

    string line;
    string candidatesName[6];
    int i = 0;

    //Array 1 ----------------------------------------------
    //Read and Print
    Input.open("candData.txt");
    if (Input.is_open())
    {
        cout << "candidatesName" << endl;
        while (getline(Input,line))
        {
            candidatesName[i] = line;
            i++;
        }
    }
    for (i = 0; i < 6; i++)
    {
        cout << candidatesName[i] << endl;
    }

    //Sort
    string tmp;
    for (i = 0; i < 6; i++)
    {
        for (int j = i+1; j < 6; j++)
        {
            if( candidatesName[i] > candidatesName[j])
            {
                tmp = candidatesName[i]; candidatesName[i] = candidatesName[j]; candidatesName[j] = tmp;
            }
        }
        Input.close();
    }
    cout << endl;
    for (i = 0; i < 6; i++)
    {
        cout << candidatesName[i] << endl;
    }
    cout << endl;
    //Array 2 -------------------------------------------------------------------
    int voteByRegion[6][4] = {0};
    for (int i =0; i < 6; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cout << voteByRegion[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    string candidatesName2;
    int regionNumber, numberOfVotesForTheCandidate;
    Input.open("voteData.txt");
    while(Input >> candidatesName2 >> regionNumber >> numberOfVotesForTheCandidate)
    {
        cout << candidatesName2 << " " << regionNumber << " " << numberOfVotesForTheCandidate << endl;
        
    }
    //Array 3-----------------------------------------------------------------
    int totalVote[6] = {0};
    for (int i = 0; i < 6; i++)
    {
        cout << totalVote[i] << endl;
    }
}