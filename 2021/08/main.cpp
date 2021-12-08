#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

void part1() {
  ifstream ifs("input.txt");

  string line;
  int num_easy = 0;
  while(getline(ifs, line)) {
    string output = line.substr(line.find('|')+2);
    istringstream iss(output);
    string word;
    num_easy += count_if(istream_iterator<string>(iss), istream_iterator<string>(),
        [](const auto s) {
        return s.size() == 2 || s.size() == 3 || s.size() == 4 || s.size() == 7;
        });
  }

  cout << num_easy << endl;
}

int main() {
  part1();
  return 0;
}
