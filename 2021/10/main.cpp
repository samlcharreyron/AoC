#include <fstream>
#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

pair<int, stack<char>> process_line(const string& line) {
  stack<char> st;

  for (auto c : line) {
    if (c == '(' || c == '[' || c == '{' || c == '<') {
      st.push(c);
    }

    if (c == ')') {
      if (st.empty() || st.top() != '(') {
        return {3, st};
      } else {
        st.pop();
      }
    }

    if (c == ']') {
      if (st.empty() || st.top() != '[') {
        return {57, st};
      } else {
        st.pop();
      }
    }

    if (c == '}') {
      if (st.empty() || st.top() != '{') {
        return {1197, st};
      } else {
        st.pop();
      }
    }

    if (c == '>') {
      if (st.empty() || st.top() != '<') {
        return {25137, st};
      } else {
        st.pop();
      }
    }
  }
  return {0, st};
}

void part1() {
  ifstream ifs("input.txt");

  string line;
  int res = 0;

  while (getline(ifs, line)) {
    auto [r, st] = process_line(line);
    res += r;
  }

  cout << res << endl;
}

void part2() {
  ifstream ifs("input.txt");

  vector<size_t> scores;
  string line;
  while (getline(ifs, line)) {
    auto [r, st] = process_line(line);
    
    if (r == 0) {
      size_t res = 0;
      while (!st.empty()) {
        if (st.top() == '(') {
          res = res * 5 + 1;
        } else if (st.top() == '[') {
          res = res * 5 + 2;
        } else if (st.top() == '{') {
          res = res * 5 + 3;
        } else if (st.top() == '<') {
          res = res * 5 + 4;
        }
        st.pop();
      }
      scores.push_back(res);
    }
  }

  sort(scores.begin(), scores.end());
  cout << scores[scores.size() / 2] << endl;

}

int main() {
  part1();
  part2();
  return 0;
}
