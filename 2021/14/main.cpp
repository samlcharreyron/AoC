#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

// Only for pairs of std::hash-able types for simplicity.
// You can of course template this struct to allow other hash functions
struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        // Mainly for demonstration purposes, i.e. works but is overly simple
        // In the real world, use sth. like boost.hash_combine
        return h1 ^ h2;  
    }
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

using Counter = unordered_map<char, size_t>;

struct Dfs {
  unordered_map<string, char> rules;
  unordered_map<string, unordered_map<int, Counter>> cache;
  //Counter counter;

  Counter dfs(const string& s, int steps) {
    if (steps == 0) {
      return Counter();
    }

    auto s_it = cache.find(s);
    if (s_it != cache.end()) {
      auto c_it = s_it->second.find(steps);
      if (c_it != s_it->second.end()) {
        //cout << "cache hit for " << s << " " << steps << endl;
        return c_it->second;
      }
    }

    auto it = rules.find(s);
    if (it == rules.end()) {
      return Counter();
    }

    string s1 = s.substr(0, 1) + string(1, it->second);
    string s2 = string(1, it->second) + s.substr(1, 1);
    Counter count = dfs(s1, steps - 1);
    Counter count2 = dfs(s2, steps - 1);

    for (auto p : count2) {
      count[p.first] += p.second;
    }

    count[it->second]++;
    cache[s][steps] = count;

    return count;
  }
};

void part2() {
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

  Dfs dfs;
  dfs.rules = rules;
  Counter counter;
  for (auto c : input) {
    counter[c]++;
  }

  const int steps = 40;
  for (int i=0; i < (input.size() - 1); i++) {
    Counter count2 = dfs.dfs(input.substr(i, 2), steps);
    for (auto p : count2) {
      counter[p.first] += p.second;
    }
  }

  vector<size_t> quants;
  // for (auto p : counter) {
  //   cout << p.first << " " << p.second << endl;
  // }

  transform(counter.begin(), counter.end(), back_inserter(quants), [](auto p) {
      return p.second;});
  sort(quants.begin(), quants.end());
  cout << quants.back() - quants.front() << endl;

}


int main() {
  part1();
  part2();

  return 0;
}
