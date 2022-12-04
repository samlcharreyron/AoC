#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <set>
#include <algorithm>
#include <numeric>
#include <array>
#include <tuple>

using namespace std;

using namespace std;

pair<int, int> getBound(const string& s) {
  string l = s.substr(0, s.find('-'));
  string u = s.substr(s.find('-') + 1);
  return {stoi(l), stoi(u)};
}

void part1(const vector<string>& lines) {
  int valid = 0;

  for (const string& line : lines) {
    string left = line.substr(0, line.find(','));
    string right = line.substr(line.find(',') + 1);

    auto pl = getBound(left);
    auto pr = getBound(right);

    if (pl.first > pr.first) {
      swap(pl, pr);
    }

    bool r_in_l = pr.first <= pl.second && pr.second <= pl.second;
    bool l_in_r = pl.first >= pr.first && pl.second <= pr.second;
    if (r_in_l || l_in_r) {
      valid++;
    } else {
      //cout << line << endl;
    }
  }

  cout << valid << endl;
}

void part2(const vector<string>& lines) {
  int valid = 0;

  for (const string& line : lines) {
    string left = line.substr(0, line.find(','));
    string right = line.substr(line.find(',') + 1);

    auto pl = getBound(left);
    auto pr = getBound(right);

    if (pl.first > pr.first) {
      swap(pl, pr);
    }

    if (pr.first <= pl.second) {
      valid++;
    } else {
      //cout << line << endl;
    }
  }

  cout << valid << endl;
}

int main(int argc, char** argv) {
  ifstream ifs("input", ios::in);
  string line;

  vector<string> lines;
  while(getline(ifs, line)) {
    lines.push_back(line);
  }

  part1(lines);
  part2(lines);
}
