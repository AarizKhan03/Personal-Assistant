#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{   
    char search2[int(200)];
    string keywords2;
    ifstream read_file("TempGoogleSearch.txt");
    while (getline (read_file, keywords2)) {
    cout << "Searching For " <<keywords2 <<endl;
    }
   
        string keywords_string2 = ("start chrome https://www.google.com/search?q=" + keywords2);

    //cout<< site_url_string;
    strcpy(search2,keywords_string2.c_str());
    system(search2);

    
}