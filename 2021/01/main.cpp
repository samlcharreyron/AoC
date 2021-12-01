#include <iostream>
#include <fstream>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

int main() {
  ifstream ifs("input.txt");

  vector<int> v;
  transform(istream_iterator<string>(ifs), istream_iterator<string>(), back_inserter(v), [](const auto &s) {return std::stoi(s);});
  vector<int> adj;
  auto it = adjacent_difference(v.begin(), v.end(), back_inserter(adj));
  int res = count_if(adj.begin()+1, adj.end(), [](const int x) { return x > 0; });

  cout << res << endl;

  return 0;
}
