#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <set>
#include <algorithm>
#include <numeric>
#include <tuple>
#include <array>
#include <deque>

using namespace std;

void part1(const string& line, int size) {
  array<int, 256> arr = {0};
  for (int i=0; i < size; i++) {
    arr[line[i] - 'a']++;
  }

  for (int i=size; i < line.size(); i++) {
    if (*max_element(arr.begin(), arr.end()) == 1) {
      cout << i << endl;
      return;
    }
    arr[line[i] - 'a']++;
    arr[line[i-size]-'a']--;
  }
}

int main(int argc, char** argv) {
  ifstream ifs("input", ios::in);
  string line;
  getline(ifs, line);

  part1(line, 4);
  part1(line, 14);

  return 0;
}
