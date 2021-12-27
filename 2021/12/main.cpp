#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
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

size_t dfs(const string name, const Nodes& nodes, const unordered_set<string>& visited) {

  if (name == "end") {
    return 1;
  }

  if (visited.find(name) != visited.end()) {
    return 0;
  }

  unordered_set<string> visited_(visited);
  if (all_of(name.begin(), name.end(), [](const auto c) { 
    return islower(c); })) {
    visited_.insert(name);
  }

  return accumulate(nodes.at(name).children.begin(),
    nodes.at(name).children.end(), 0, [&nodes, &visited_](const auto lhs, const auto pc) {
    return lhs + dfs(pc->name, nodes, visited_);
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

  unordered_set<string> visited;
  cout << dfs("start", nodes, visited) << endl;
}

int main() {
  part1();
  return 0;
}
