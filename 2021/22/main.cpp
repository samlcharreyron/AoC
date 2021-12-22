#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

template <class T>
inline void hash_combine(std::size_t& seed, const T& v) {
  std::hash<T> hasher;
  seed ^= hasher(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

struct hash_pair {
  size_t operator()(const pair<int, int>& p) const {
    size_t seed = std::hash<int>{}(p.first);
    hash_combine(seed, p.second);
    return seed;
  }
};

struct Cuboid {
    int x_min, x_max;
    int y_min, y_max;
    int z_min, z_max;
    bool is_on;
};

void part1() {
  ifstream ifs("input.txt");

  string line;
  vector<Cuboid> cuboids;
  while(getline(ifs, line)) {
    Cuboid c;
    c.is_on = line.find("on") != line.npos;
    line = line.substr(line.find("x=")+2);
    {
      istringstream iss(line);
      iss >> c.x_min;
    }
    line = line.substr(line.find("..")+2);
    {
      istringstream iss(line);
      iss >> c.x_max;
    }
    line = line.substr(line.find("y=")+2);
    {
      istringstream iss(line);
      iss >> c.y_min;
    }
    line = line.substr(line.find("..")+2);
    {
      istringstream iss(line);
      iss >> c.y_max;
    }
    line = line.substr(line.find("z=")+2);
    {
      istringstream iss(line);
      iss >> c.z_min;
    }
    line = line.substr(line.find("..")+2);
    {
      istringstream iss(line);
      iss >> c.z_max;
    }

    if (c.x_min >= -50 && c.x_max <= 50 &&
      c.y_min >= -50 && c.y_max <= 50 &&
      c.z_min >= -50 && c.z_max <= 50) {
      cuboids.push_back(c);
    }
  }

  int grid[101][101][101] = {0};
  for (auto c : cuboids) {
    for (int x=c.x_min; x <= c.x_max; x++) {
      for (int y=c.y_min; y <= c.y_max; y++) {
        for (int z=c.z_min; z <= c.z_max; z++) {
          grid[x+50][y+50][z+50] = c.is_on;
        }
      }
    }
  }

  size_t ret = 0;
  for (int i=0; i < 101; i++) {
    for (int j=0; j < 101; j++) {
      for (int k=0; k < 101; k++) {
        if (grid[i][j][k] > 0) {
          ret++;
        }
      }
    }
  }
  cout << ret << endl;
}

int main() {
  part1();
  return 0;
}
