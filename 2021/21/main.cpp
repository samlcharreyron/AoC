#include <iostream>
#include <vector>
#include <numeric>
#include <functional>
#include <array>

using namespace std;
  
void part1() {
  //vector<int> positions {4, 8};
  vector<int> scores {0, 0};
  vector<int> positions {7, 5};

  //vector<int> dice(100);
  //iota(dice.begin(), dice.end(), 1);
  
  int dice = 1;
  size_t rolls = 0;

  while(true) {
    for (int p=0; p < positions.size(); p++) {
      int roll = 3 * dice + 3;
      positions[p] = 1 + (positions[p] + roll - 1) % 10;
      scores[p] += positions[p];
      dice = 1 + (dice + 2) % 100;
      rolls += 3;
      //cout << scores[p] << endl;
      if (scores[p] >= 1000) {
        cout << rolls * *min_element(scores.begin(), scores.end()) << endl;
        //cout << "rolls: " << rolls << " scores: ";
        //copy(scores.begin(), scores.end(), ostream_iterator<int>(cout, " "));
        return;
      }
    }
  }

  cout << "rolls: " << rolls << " scores: ";
  copy(scores.begin(), scores.end(), ostream_iterator<int>(cout, " "));
  //cout << rolls * *min_element(scores.begin(), scores.end()) << endl;

}

constexpr array<int, 27> getRolls() {
  array<int, 27> a{0};
    for (auto i=1; i < 4; i++) {
      for (auto j=1; j < 4; j++) {
        for (auto k=1; k < 4; k++) {
          auto idx = (i-1) * 9 + (j-1) * 3 + k-1;
          a[idx] = (i + j + k);
        }
      }
    }
  return a;
}

struct DFS {

  size_t grid[10][10][21][21][2];
  
  vector<size_t> dfs(int p1, int p2, int s1, int s2) {

    if (s1 >= 21) {
      return {1, 0};
    }
    if (s2 >= 21) {
      return {0, 1};
    }

    auto s_0 = grid[p1-1][p2-1][s1-1][s2-1][0];
    auto s_1 = grid[p1-1][p2-1][s1-1][s2-1][1];

    if (s_0 > 0 || s_1 > 0) {
      // cout << positions[0] << " " << positions[1] << " ";
      // cout << scores[0] << " " << scores[1] << " early exit " << s_0 << " " << s_1 << endl;
      return {s_0, s_1};
    }

    size_t n1 = 0;
    size_t n2 = 0;
    for (int r=0; r < 27; r++) {
      //positions_[p] = 1 + (positions[p] + ConstArray().rolls[r] - 1) % 10;
      int p1_new = 1 + (p1 + getRolls()[r] - 1) % 10;
      int s1_new = s1 + p1_new;

      auto nums_d = dfs(p2, p1_new, s2, s1_new);
      n1 += nums_d[1];
      n2 += nums_d[0];
      //transform(nums.begin(), nums.end(), nums_d.begin(), nums.begin(), 
      //std::plus<int>());

    }

    grid[p1-1][p2-1][s1-1][s2-1][0] = n1;
    grid[p1-1][p2-1][s1-1][s2-1][1] = n2;

    return {n1, n2};
  }
};

void part2() {
  int p1 = 7, p2 = 5;
  int s1 =0, s2 = 0;

  auto dfs = DFS();
  auto nums = dfs.dfs(p1, p2, s1, s2);
  //cout << nums[0] << " " << nums[1] << endl;
  cout << *max_element(nums.begin(), nums.end()) << endl;
}

int main() {
  part1();
  part2();
  return 0;
}
