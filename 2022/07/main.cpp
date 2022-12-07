#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <set>
#include <algorithm>
#include <numeric>
#include <tuple>
#include <array>
#include <deque>
#include <regex>
#include <optional>

using namespace std;

struct Node {
  string name;
  bool is_dir;
  Node* parent = nullptr;
  vector<Node*> children;
  int file_size = 0;

  Node(const string& name, bool is_dir, Node* parent) : name(name), is_dir(is_dir), parent(parent) {}
};

Node* find_entry(Node* root, const string& path) {
  if (!root) {
    return nullptr;
  }

  if (root->name == path) {
    return root;
  }

  for (auto child: root->children) {
    Node* match = find_entry(child, path);
    if (match) {
      return match;
    }
  }

  return nullptr;
}

Node* find_child(Node* root, const string& name) {
  if (!root) {
    return nullptr;
  }

  for (auto child: root->children) {
    if (child->name == name) {
      return child;
    }
  }

  return nullptr;
}

size_t find_size(Node* root) {
  if (!root) {
    return 0;
  }

  if (root->is_dir) {
    size_t size = 0;
    for (auto child: root->children) {
      size += find_size(child);
    }
    return size;
  } else {
    return root->file_size;
  }
}


Node* build_tree(const vector<string>& lines) {
  Node* root = new Node("/", true, nullptr);
  Node* current = root;

  regex cd_regex("^\\$ cd (.+)$");
  regex dir_regex("^dir (.+)$");
  regex file_regex("^(\\d+) (.+)$");

  size_t file_sum = 0;

  for (auto line: lines) {
    smatch match;
    if (regex_search(line, match, dir_regex)) {
      string dir_name = match[1].str();
      // cout << "adding dir " << dir_name << " to " << current->name << endl;
      if (find_child(current, dir_name)) {
        stringstream ss;
        ss << "Directory " << dir_name << " already exists in " << current->name;
        throw std::runtime_error(ss.str());
      } else {
        current->children.push_back(new Node(dir_name, true, current));
      }
    } else if (regex_search(line, match, file_regex)) {
      string file_size = match[1].str();
      string file_name = match[2].str();
      // cout << "adding file " << file_name << " with size: " << file_size << " to " << current->name << endl;
      if (find_child(current, file_name)) {
        stringstream ss;
        ss << "File " << file_name << " already exists in " << current->name;
        throw std::runtime_error(ss.str());
      } else {
        Node* file = new Node(file_name, false, current);
        file->file_size = stoi(file_size);
        current->children.push_back(file);
      }
  
    } else if (regex_search(line, match, cd_regex)) {
      string dir_name = match[1].str();
      if (dir_name == "..") {
        current = current->parent;
      } else {
        // cout << "checking " << dir_name << " is part of " << current->name << endl;
        Node* match = find_child(current, dir_name);
        if (!match) {
          stringstream ss;
          ss << current->name << " does not contain child: " << dir_name << endl;
          std::runtime_error(ss.str());
        } else {
          current = match;
        }
      }
    }
  }

  return root;
}

void part1(Node* root) {
  stack<Node*> s;
  s.push(root);
  size_t sum = 0;
  while(!s.empty()) {
    Node* current = s.top();
    s.pop();
    if (current->is_dir) {
      size_t current_size = find_size(current);
      if (current_size <= 100000) {
        sum += current_size;
      }
      // return vector of children that have is_dir=true and add them to stack
      for (auto child: current->children) {
        if (child->is_dir) {
          s.push(child);
        }
      }
    }
  }

  cout << sum << endl;
}

void part2(Node* root) {
  // part 2
  size_t unused_space = 70000000 - find_size(root);
  size_t need_size = 30000000 - unused_space;

  stack<Node*> s;
  s.push(root);

  size_t min_size = 1000000000;
  while(!s.empty()) {
    Node* current = s.top();
    s.pop();
    if (current->is_dir) {
      size_t current_size = find_size(current);
      if (current_size >= need_size) {
        if (current_size < min_size) {
          min_size = current_size;
        }
        for (auto child: current->children) {
          s.push(child);
        }
      }
    }
  }

  cout << min_size << endl;
}

int main(int argc, char** argv) {
  ifstream ifs("input", ios::in);
  string line;
  vector<string> lines;
  
  // ignore first line
  getline(ifs, line);

  while (getline(ifs, line)) {
    lines.push_back(line);
  }

  Node* root = build_tree(lines);

  part1(root);
  part2(root);

  return 0;
}
