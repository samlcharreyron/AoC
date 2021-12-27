#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <numeric>

using namespace std;

struct Node {
  string name;
  vector<Node*> children;
  Node() = default;
  Node(string n) : name(n) {}
};

using Nodes = unordered_map<string, Node>;
using Visited = map<string, int>;

bool is_lower(const string& s) {
  return all_of(s.begin(), s.end(), [](const auto c) { 
    return islower(c); });
}

size_t dfs(const string name, const Nodes& nodes, const Visited& visited, const int visits=1) {

  if (name == "end") {
    //for (auto p : visited) {
    //  cout << p.first << " (" << p.second << ") ";
    //}
    //cout << endl;
    return 1;
  }

  bool already_full = any_of(visited.begin(), visited.end(), 
    [visits](auto p) { return is_lower(p.first) && p.second == visits; });

  auto it = visited.find(name);
  if (name == "start" && it != visited.end() && it->second == 1) {
    return 0;
  }

  if (already_full && is_lower(name) && it != visited.end()) {
    return 0;
  }

  Visited visited_(visited);
  visited_[name]++;

  return accumulate(nodes.at(name).children.begin(),
    nodes.at(name).children.end(), 0, [&nodes, &visited_, visits](const auto lhs, const auto pc) {
    return lhs + dfs(pc->name, nodes, visited_, visits);
  });
}


void part1() {
  Nodes nodes;
  ifstream ifs("input.txt");

  string line;
  while(getline(ifs, line)) {
    int dash = line.find('-');
    string from = line.substr(0, dash);
    string to = line.substr(dash+1);

    if (nodes.find(from) == nodes.end()) {
      nodes[from] = Node(from);
    }

    if (nodes.find(to) == nodes.end()) {
      nodes[to] = Node(to);
    }

    nodes[from].children.push_back(&nodes[to]);
    nodes[to].children.push_back(&nodes[from]);
  }

  Visited visited;
  cout << dfs("start", nodes, visited, 1) << endl;
}

void part2() {
  Nodes nodes;
  ifstream ifs("input.txt");

  string line;
  while(getline(ifs, line)) {
    int dash = line.find('-');
    string from = line.substr(0, dash);
    string to = line.substr(dash+1);

    if (nodes.find(from) == nodes.end()) {
      nodes[from] = Node(from);
    }

    if (nodes.find(to) == nodes.end()) {
      nodes[to] = Node(to);
    }

    nodes[from].children.push_back(&nodes[to]);
    nodes[to].children.push_back(&nodes[from]);
  }

  Visited visited;
  cout << dfs("start", nodes, visited, 2) << endl;
}

int main() {
  part1();
  part2();
  return 0;
}
