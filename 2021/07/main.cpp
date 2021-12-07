#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

void part1() {
  ifstream ifs("input.txt");

  string line;
  vector<int> v;
  while(getline(ifs, line, ',')) {
    v.push_back(stoi(line));
  }

  // min_i (sum_j (xi - xj)^2)
  // min_i sum_j(xi^2 - 2xi xj + xj^2)
  // min_i ( xi^2 - 2xi sum_j(xj) + mu)
  // (x^2 + b*x + c=0)
  // 2sum_j +- sqrt((4sum_j^2) - 4*mu)
  //
  int sum = accumulate(v.begin(), v.end(), 0);
  int sum_sq = inner_product(v.begin(), v.end(), v.begin(), 0);

  auto f = [&] (const auto x) { return x * x - 2*sum*x; };
  auto g = [&v] (const auto x) { return accumulate(v.begin(), v.end(), 0, [x](auto a, auto y) { return a + (x - y) * (x - y);});};
  auto h = [&v] (const auto x) { return accumulate(v.begin(), v.end(), 0, [x](auto a, auto y) { return a + abs(x - y);});};
  auto it = min_element(v.begin(), v.end(), [f,h,g] (const auto lhs, const auto rhs) { return h(lhs) < h(rhs); });

  cout << h(*it) << endl;
}

void part2() {
  ifstream ifs("input.txt");

  string line;
  vector<int> v;
  while(getline(ifs, line, ',')) {
    v.push_back(stoi(line));
  }

  // min_i (sum_j (xi - xj)^2)
  // min_i sum_j(xi^2 - 2xi xj + xj^2)
  // min_i ( xi^2 - 2xi sum_j(xj) + mu)
  // (x^2 + b*x + c=0)
  // 2sum_j +- sqrt((4sum_j^2) - 4*mu)
  //
  int sum = accumulate(v.begin(), v.end(), 0);
  int sum_sq = inner_product(v.begin(), v.end(), v.begin(), 0);
  int v_max = *max_element(v.begin(), v.end());

  auto f = [&] (const auto x) { return x * x - 2*sum*x; };
  auto g = [&v] (const auto x) { return accumulate(v.begin(), v.end(), 0, [x](auto a, auto y) { return a + (x - y) * (x - y);});};
  auto h = [&v] (const auto x) { return accumulate(v.begin(), v.end(), 0, 
      [x](auto a, auto y) { int d = abs(x - y); return a + (d * (d+1))/2;});};

  vector<int> xv(v_max);
  iota(xv.begin(), xv.end(), 0);
  auto it = min_element(xv.cbegin(), xv.cend(), [f,h,g] (const auto lhs, const auto rhs) { return h(lhs) < h(rhs); });

  cout << h(*it) << endl;
}

int main() {
  part1();
  part2();
  return 0;
}
