#include <algorithm>
#include <bitset>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

void part1() {
  ifstream ifs("input.txt");

  string line;
  int num_easy = 0;
  while (getline(ifs, line)) {
    string output = line.substr(line.find('|') + 2);
    istringstream iss(output);
    string word;
    num_easy += count_if(istream_iterator<string>(iss),
                         istream_iterator<string>(), [](const auto s) {
                           return s.size() == 2 || s.size() == 3 ||
                                  s.size() == 4 || s.size() == 7;
                         });
  }

  cout << num_easy << endl;
}

void part2() {
  ifstream ifs("test.txt");

  string line;
  int res = 0;
  while (getline(ifs, line)) {
    unordered_set<char> chars_4;
    unordered_set<char> chars_1;
    string input = line.substr(0, line.find('|'));
    string output = line.substr(line.find('|') + 2);
    {
      istringstream iss(input);
      string word;
      while (iss >> word) {
        if (word.size() == 2) {
          chars_1 = unordered_set<char>(word.begin(), word.end());
        } else if (word.size() == 4) {
          chars_4 = unordered_set<char>(word.begin(), word.end());
        }
      }
    }
    {
      istringstream iss(output);
      string word;
      string digits;
      while (iss >> word) {
        cout << word << " ";
       
        auto ws = unordered_set<char>(word.begin(), word.end());
        unordered_set<char> si_4;
        unordered_set<char> si_1;
        set_intersection(ws.begin(), ws.end(),
                         chars_4.begin(), chars_4.end(), inserter(si_4, si_4.begin()));
        set_intersection(ws.begin(), ws.end(), 
                         chars_1.begin(), chars_1.end(), inserter(si_1, si_1.begin()));
        cout << "overlap with 4: " << si_4.size() << " ";
        cout << "overlap with 1: " << si_1.size() << " ";
        char dig;
        if (word.size() == 2) {
          dig = '1';
        } else if (word.size() == 3) {
          dig = '7';
        } else if (word.size() == 4) {
          dig = '4';
        } else if (word.size() == 5) {
          if (si_4.size() == 2) {
            dig = '2';
          } else if (si_4.size() == 3 && si_1.size() == 1) {
            dig = '5';
          } else if (si_4.size() == 3 && si_1.size() == 2) {
            dig = '3';
          }
        } else if (word.size() == 6) {
          if (si_4.size() == 4) {
            dig = '9';
          } else if (si_4.size() == 3 && si_1.size() == 1) {
            dig = '6';
          } else if (si_4.size() == 3 && si_1.size() == 2) {
            dig = '0';
          }
        } else if (word.size() == 7) {
          dig = '8';
        }

        cout << "digit: " << dig << " ";

        digits += dig;
      }
      cout << digits << endl;
      res += stoi(digits);
    }
  }

  cout << res << endl;
}

int main() {
  part1();
  part2();
  return 0;
}
