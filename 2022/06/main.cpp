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
  deque<char> q(line.begin(), line.begin()+size);
  for (int i=size; i < line.size(); i++) {
    set<char> s(q.begin(), q.end());
    if (s.size() == size) {
      cout << i << endl;
      return;
    }
    
    q.pop_front();
    q.push_back(line[i]);
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
