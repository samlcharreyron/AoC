#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int p1(const vector<string>& lines) {
    int i = 0;
    for(auto line : lines) {
        istringstream iss(line);
        int l, h;
        string sub;
        iss >> sub;
        l = stoi(sub.substr(0, sub.find('-')));
        h = stoi(sub.substr(sub.find('-')+1));
        iss >> sub;
        char c = sub[0];
        string p;
        iss >> p; 
        int n = count(p.cbegin(), p.cend(), c);
        if (n >=l && n <= h)
            i++;
    }

    return i;
}

int main(int argc, char** argv) {

    fstream f("input.txt", ios::in);
    if (!f.is_open()) return -1;

    vector<string> lines;
    string line;
    while(getline(f, line)) {
        lines.push_back(line);
    }

    cout << p1(lines) << endl;

}
