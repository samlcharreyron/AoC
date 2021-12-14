#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

struct Insertion {
  int pos;
  char c;
};

void part1() {

  ifstream ifs("input.txt");

  string input;
  getline(ifs, input);

  string line;
  // ignore this empty line
  getline(ifs, line);

  unordered_map<string, char> rules;

  while (getline(ifs, line)) {
      rules[line.substr(0, 2)] = line.back();
  }

  for (int k=0; k < 10; k++) {
    vector<pair<int, char>> to_insert;
    for (int i=0; i < (input.size() - 1); i++) {
      auto it = rules.find(input.substr(i, 2));

      if (it != rules.end()) {
        to_insert.push_back({i+1+to_insert.size(), it->second});
      }
    }

    for (auto p : to_insert) {
      input.insert(p.first, 1, p.second);
    }
  }

  unordered_map<char, int> counter;
  for (auto c : input) {
    counter[c]++;
  }

  vector<int> quants;
  transform(counter.begin(), counter.end(), back_inserter(quants), [](auto p) { return p.second;});
  sort(quants.begin(), quants.end());
  cout << quants.back() - quants.front() << endl;
}

int main() {
  part1();

  return 0;
}
