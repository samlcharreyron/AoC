#include <bitset>
#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <string>
#include <vector>

using namespace std;

void part1() {
  ifstream ifs("input.txt");

  constexpr size_t N = 12;

  vector<bitset<N>> v;
  transform(istream_iterator<string>(ifs), istream_iterator<string>(),
            back_inserter(v), [](const string& s) { return bitset<N>(s); });

  vector<size_t> nums(N, 0);
  for (auto bs : v) {
    for (int b = 0; b < N; b++) {
      if (bs[b]) {
        nums[b]++;
      }
    }
  }

  bitset<N> r;
  for (int b = 0; b < N; b++) {
    if (nums[b] > v.size() / 2) {
      r[b] = true;
    }
  }

  /*bitset<N> r = accumulate(begin(v), end(v), bitset<N>(),
      [] (const auto a, const auto b) {
      return a ^ b;
      });*/

  cout << r.to_ulong() * (~r).to_ulong() << endl;
}

unsigned long get_ox() {
  ifstream ifs("input.txt");

  constexpr size_t N = 12;

  vector<bitset<N>> v;
  transform(istream_iterator<string>(ifs), istream_iterator<string>(),
            back_inserter(v), [](const string& s) { return bitset<N>(s); });

  int b = N - 1;
  vector<size_t> nums(N);
  while (v.size() > 1) {
    nums[b] = count_if(begin(v), end(v), [b](const auto bs) { return bs[b]; });

    bool mc = nums[b] >= double(v.size()) / 2;

    auto it = remove_if(begin(v), end(v), [mc, b](const auto bs) { return bs[b] ^ mc ; });
    v.erase(it, v.end());
    b--;
  }

  return v[0].to_ulong();
}

unsigned long get_co2() {
  ifstream ifs("input.txt");

  constexpr size_t N = 12;

  vector<bitset<N>> v;
  transform(istream_iterator<string>(ifs), istream_iterator<string>(),
            back_inserter(v), [](const string& s) { return bitset<N>(s); });

  int b = N - 1;
  vector<size_t> nums(N);
  while (v.size() > 1) {
    nums[b] = count_if(begin(v), end(v), [b](const auto bs) { return bs[b]; });

    bool mc = nums[b] < double(v.size()) / 2;

    auto it = remove_if(begin(v), end(v), [mc, b](const auto bs) { return bs[b] ^ mc ; });
    v.erase(it, v.end());
    b--;
  }

  return v[0].to_ulong();
}

void part2() {
  unsigned long ox = get_ox();
  unsigned long co2 = get_co2();

  cout << ox * co2 << endl;
}

int main() {
  part2();
  return 0;
}
