#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>
#include <windows.h>
using namespace std;

int main()
{
    char app_location[50];
    string app_name;
    ifstream read_file("TempApp.txt");
    while (getline (read_file, app_name)) {
    cout << "Opening " << app_name << endl;
    }
    string app_location_string = ("start " + app_name + ".exe");
    strcpy(app_location, app_location_string.c_str());
    //system(app_location);
    
    system(app_location);
    //start chrome.exe
    cout<<app_location;

    
    
}