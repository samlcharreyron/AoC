#include <iostream>
#include <fstream>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

void part1() {
  ifstream ifs("input.txt");

  vector<int> v;
  transform(istream_iterator<string>(ifs), istream_iterator<string>(), back_inserter(v), [](const auto &s) {return std::stoi(s);});
  vector<int> adj;
  auto it = adjacent_difference(v.begin(), v.end(), back_inserter(adj));
  int res = count_if(adj.begin()+1, adj.end(), [](const int x) { return x > 0; });

  cout << res << endl;
}

void part2() {
  ifstream ifs("input.txt");

  vector<int> v;
  transform(istream_iterator<string>(ifs), istream_iterator<string>(), back_inserter(v), [](const auto &s) {return std::stoi(s);});

  auto it1 = v.begin();
  auto it2 = it1 + 1;
  auto it3 = it2 + 1;

  vector<int> o;
  for(; it3 != v.end(); it1++, it2++, it3++) {
    o.push_back(*it1 + *it2 + *it3);
  }

  vector<int> adj(o.size());
  adjacent_difference(begin(o), end(o), adj.begin());

  int res = count_if(adj.begin() + 1, end(adj), [](const int x) { return x > 0; });

  cout << res << endl;

}


int main() {

  part1();

  part2();

  return 0;
}
