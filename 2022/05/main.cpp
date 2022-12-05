#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <set>
#include <algorithm>
#include <numeric>
#include <tuple>

using namespace std;

int main(int argc, char** argv) {
  ifstream ifs("input", ios::in);
  string line;
  vector<string> lines;
  while (getline(ifs, line)) {
    lines.push_back(line);
  }

  const auto mid = find(lines.begin(), lines.end(), "");

  const int crates = 10;
  vector<vector<char> > v(crates, vector<char>());
  for(auto it = lines.begin(); it != (mid-1); it++) {
    int iv = 0;
    for(int i=1; i < 34; i+=4) {
      if ((*it)[i] != ' ') {
        v[iv].push_back((*it)[i]);
      }
      iv++;
    }
  }

  for (auto& vv : v) {
    reverse(vv.begin(), vv.end());
    // copy(vv.begin(), vv.end(), ostream_iterator<char>(cout, " "));
    // cout << endl;
  }

  // parse moves
  vector<tuple<int, int, int> > moves;
  auto it = mid+1;
  for (; it != lines.end(); it++) {
    stringstream ss(*it);
    string word;
    int num;
    int from;
    int to;
    ss >> word;
    ss >> num;
    ss >> word;
    ss >> from;
    ss >> word;
    ss >> to;
    // cout << num << " " << from << " " << to << endl;
    moves.push_back(make_tuple(num, from-1, to-1));
  }

  for (const auto& m : moves) {
    int num, from, to;
    tie(num, from, to) = m;
    for (int i=0; i < num; i++) {
      char val = v[from].back();
      v[from].pop_back();
      v[to].push_back(val);
    }
  }


  string result;
  for (int i=0; i < crates; i++) {
    if (v[i].size() == 0) {
      continue;
    }
    result += v[i].back();
  }
  cout << result << endl;
}
