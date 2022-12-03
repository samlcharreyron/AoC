#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <set>
#include <algorithm>
#include <numeric>

using namespace std;

int priority(char c) {
    if (c >= 'a' && c <= 'z') {
      return c - 'a' + 1;
    } else {
      return c - 'A' + 27;
    }
}

void part1(const vector<string>& lines) {
  vector<int> priorities;
  for (const string& line : lines) {
    int N = line.size();
    string s1(line.begin(), line.begin() + N/2);
    string s2(line.begin() + N/2, line.end());
    // find the set intersection of s1 and s2
    set<char> s1_set(s1.begin(), s1.end());
    set<char> s2_set(s2.begin(), s2.end());
    vector<char> intersection;
    set_intersection(s1_set.begin(), s1_set.end(), s2_set.begin(), s2_set.end(), back_inserter(intersection));
    char c = intersection[0];
    priorities.push_back(priority(c));
  }

  size_t sum = accumulate(priorities.begin(), priorities.end(), 0);
  cout << sum << endl;
}

void part2(const vector<string>& lines) {
  vector<int> priorities;
  for (int i=0; i < lines.size(); i+=3) {
    string s1 = lines[i];
    set<char> s1_set(s1.begin(), s1.end());
    string s2 = lines[i+1];
    set<char> s2_set(s2.begin(), s2.end());
    string s3 = lines[i+2];
    set<char> s3_set(s3.begin(), s3.end());

    set<char> intersection;
    set_intersection(s1_set.begin(), s1_set.end(), s2_set.begin(), s2_set.end(), inserter(intersection, intersection.begin()));
    set<char> intersection2;
    set_intersection(intersection.begin(), intersection.end(), s3_set.begin(), s3_set.end(), inserter(intersection2, intersection2.begin()));

    priorities.push_back(priority(*intersection2.begin()));
  }

  size_t sum = accumulate(priorities.begin(), priorities.end(), 0);
  cout << sum << endl;
}

int main(int argc, char** argv) {

  ifstream ifs("input", ios::in);
  string line;

  vector<string> lines;
  while(getline(ifs, line)) {
    lines.push_back(line);
  }

  part1(lines);
  part2(lines);

  return 0;
}
