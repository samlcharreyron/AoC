#include <iostream>
//#include <fstream>

using namespace std;

void part1() {
  //int x_min = 20;
  //int x_max = 30;
  //int y_min = -10;
  //int y_max = -5;
  int x_min = 209;
  int x_max = 238;
  int y_min = -86;
  int y_max = -59;

  int vx_max = 2000;
  int vy_max = 2000;
  int best_y = 0;

  for (int vx0=10; vx0 <= vx_max; vx0++) {
    for (int vy0=10; vy0 <= vy_max; vy0++) {
      int x = 0;
      int y = 0;
      int vx = vx0;
      int vy = vy0;
      int best_y_ = 0;
      bool reached = false;

      while( x <= x_max && y >= y_min ) {
        if (x <= x_max && x >= x_min 
          && y <= y_max && y >= y_min)  {
          reached = true;
          break;
        }
        x += vx;
        y += vy;
        if (y > best_y_) {
          best_y_ = y;
        }
        if (vx > 0) {
          vx--;
        } else if (vx < 0) {
          vx++;
        }
        vy--;
      }

      if (reached && best_y_ > best_y) {
          best_y = best_y_;
      }

        //cout << "reached: " << reached << " with y: " << best_y << endl;
    }
  }

  cout << best_y << endl;

}

void part2() {
  //int x_min = 20;
  //int x_max = 30;
  //int y_min = -10;
  //int y_max = -5;
  int x_min = 209;
  int x_max = 238;
  int y_min = -86;
  int y_max = -59;

  int vx_max = 2000;
  int vy_max = 2000;
  size_t num_valid = 0;

  for (int vx0=1; vx0 <= vx_max; vx0++) {
    for (int vy0=-vy_max; vy0 <= vy_max; vy0++) {
      int x = 0;
      int y = 0;
      int vx = vx0;
      int vy = vy0;
      int best_y_ = 0;
      bool reached = false;

      while( x <= x_max && y >= y_min ) {
        if (x <= x_max && x >= x_min 
          && y <= y_max && y >= y_min)  {
          reached = true;
          num_valid++;
          break;
        }
        x += vx;
        y += vy;
        if (vx > 0) {
          vx--;
        } else if (vx < 0) {
          vx++;
        }
        vy--;
      }
        //cout << "reached: " << reached << " with y: " << best_y << endl;
    }
  }

  cout << num_valid << endl;

}

int main() {
  part1();
  part2();
  return 0;
}
