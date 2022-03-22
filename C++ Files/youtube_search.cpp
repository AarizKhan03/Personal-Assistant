#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{   
    char search[int(200)];
    string keywords;
    ifstream read_file("TempYoutubeSearch.txt");
    while (getline (read_file, keywords)) {
    cout << "Searching For " <<keywords <<endl;
    }
   
        string keywords_string = ("start chrome https://www.youtube.com/results?search_query=" + keywords);

    //cout<< site_url_string;
    strcpy(search,keywords_string.c_str());
    system(search);

    
}