#include <algorithm>
#include <array>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <optional>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

void part1(const vector<string>& lines) {
  vector<int> cycles = {20, 60, 100, 140, 180, 220};

  int x = 1;
  deque<int> q(3, 0);
  // [0, 0, 3]
  // [0, 3, -5]
  // [3, -5, 0]
  int cycle = 1;
  size_t sum = 0;
  for (int i = 0; i < lines.size(); i++) {
    const string line = lines[i];
    stringstream ss(line);
    string op;
    ss >> op;

    if (find(cycles.begin(), cycles.end(), cycle) != cycles.end()) {
      sum += (x * cycle);
    }
    else if (find(cycles.begin(), cycles.end(), cycle+1) != cycles.end() && op == "addx") {
      sum += (x * (cycle + 1));
    }

    int val;
    int inc = 0;
    if(op == "noop") {
      val = 0;
      //inc = 1;
      cycle++;
    } else if (op == "addx") {
      ss >> val;
      //inc = 2;
      cycle+= 2;
    }

    x += val;

    cout << "Cycle " << cycle << " x: " << x << endl; 
  }

  cout << sum << endl;
}

void update(vector<string>& v,int cycle, int x) {
  int pos_w = (cycle - 1) % 40;
  int pos_h = (cycle - 1) / 40;
  if (pos_w == (x-1) || pos_w == x || pos_w == (x+1)) {
    v[pos_h][pos_w] = '#';
  }
}

void part2(const vector<string>& lines) {

  vector<string> v(6, string(40, '.'));

  int x = 1;
  int cycle = 1;

  for (int i = 0; i < lines.size(); i++) {
    const string line = lines[i];
    stringstream ss(line);
    string op;
    ss >> op;

    cout << "Cycle " << cycle << " x: " << x << endl; 
    //update(v, cycle, x);

    int val = 0;
    if(op == "noop") {
      val = 0;
      update(v, cycle, x);
      cycle++;
    } else if (op == "addx") {
      update(v, cycle, x);
      ss >> val;
      cycle++;
      update(v, cycle, x);
      cycle++;
    }

    x += val;

  }

  for (auto s : v) {
    cout << s << endl;
  }
}

int main(int argc, char** argv) {
  ifstream ifs("input", ios::in);
  string line;
  vector<string> lines;

  while (getline(ifs, line)) {
    lines.push_back(line);
  }

  // part1(lines);
  part2(lines);

  return 0;
}
