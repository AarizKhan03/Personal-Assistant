#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{   
    char site_url[50];
    string site_name;
    string site_url_string;
    ifstream read_file("TempWebsite.txt");
    while (getline (read_file, site_name)) {
    cout << "Opening " <<site_name <<endl;
    }
    if (site_name.find(".") != string::npos) {
        site_url_string = ("start chrome " + site_name);
    }
    else{site_url_string = ("start chrome " + site_name +".com");
    }
    
    //cout<< site_url_string;
    strcpy(site_url,site_url_string.c_str());
    system(site_url);

    
}