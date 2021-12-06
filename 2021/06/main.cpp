#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <unordered_map>

using namespace std;

void part1() {

  ifstream ifs("input.txt");

  string line;
  vector<int> ages;
  while(getline(ifs, line, ',')) {
    ages.push_back(stoi(line));
  }

  constexpr int days = 80;
  /*for (int age : ages) {
    cout << (7 + (age - days) % 7) % 7;
    cout << " ";
  }
  cout << endl;*/

  vector<int> temp;
  vector<bool> is_first(ages.size(), false);
  for (int i=0; i < days; i++) {
    // copy(temp.begin(), temp.end(), ostream_iterator<int>(cout, " "));
    // cout << endl;
    ages.insert(ages.end(), temp.begin(), temp.end());
    vector<bool> trues(temp.size(), true);
    is_first.insert(is_first.end(), trues.begin(), trues.end());
    temp.clear();
    for (auto it = ages.begin(); it != ages.end(); it++) {
      if (!is_first[it - ages.begin()]) {
        *it = (7 + (*it - 1) % 7) % 7;
      } else {
        if (*it == 1) {
          is_first[it - ages.begin()] = false;
        }
        (*it)--;
      }
      if (*it == 0) {
        temp.push_back(9);
      }
    }
  }

  // copy(ages.begin(), ages.end(), ostream_iterator<int>(cout, " "));
  // cout << endl;
  cout << ages.size() << endl;
}

struct pairhash {
public:
  template <typename T, typename U>
  std::size_t operator()(const std::pair<T, U> &x) const
  {
    return std::hash<T>()(x.first) ^ std::hash<U>()(x.second);
  }
};

class Part2 {
  unordered_map<pair<size_t, size_t>, size_t, pairhash> cache_;

  public:

  size_t spawn(size_t age, size_t days) {
    auto it = cache_.find(make_pair(age, days));

    if (it != cache_.end()) {
      return it->second;
    }

    //cout << "spawning " << age << " " << days << endl;
    if (age >= days) {
      return 1;
    }

    size_t num_spawns = (days - age) / 7 + 1;

    size_t num_child = 1;
    for (int i=0; i < num_spawns; i++) {
      size_t spawn_time = age + i * 7 + 1;
      if (spawn_time <= days)
        num_child += spawn(8, days -  spawn_time);
    }

    cache_[make_pair(age, days)] = num_child;

    return  num_child;
  }

  void operator()() {
    ifstream ifs("input.txt");

    string line;
    vector<int> ages;
    while(getline(ifs, line, ',')) {
      ages.push_back(stoi(line));
    }

    constexpr int days = 256;
    //cout << spawn(4, days) << endl;
    //size_t num_child = accumulate(ages.begin(), ages.end(), 0, [this](const auto a, const auto b) { return a + this->spawn(b, days); });
    
    size_t num_child = 0;
    for (auto age : ages) {
      num_child += spawn(age, days);
    }
    cout << num_child << endl;
  }

};


int main() {
  part1();
  Part2{}();
  return 0;
}
