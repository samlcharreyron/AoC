#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <set>
#include <algorithm>
#include <numeric>
#include <tuple>

using namespace std;

int main(int argc, char** argv) {

  ifstream ifs("test", ios::in);
  string line;

  vector<string> lines;
  while(getline(ifs, line)) {
    lines.push_back(line);
  }

  return 0;
}
