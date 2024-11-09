#include "aoc.h"

i32 main(i32 argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Invalid arguments\n");
    exit(1);
  }

  struct file f = file_open(argv[1]);
  file_assert_open(f);

#define WIDTH 2000
#define HEIGHT 3000
  char *grid1 = calloc(WIDTH * HEIGHT, 1);
  char *grid2 = calloc(WIDTH * HEIGHT, 1);
  i32 x = 1000, y = 2100;
  i32 santa_x = x, santa_y = y;
  i32 robot_x = x, robot_y = y;
  grid1[y * WIDTH + x] = 1;
  grid2[y * WIDTH + x] = 1;
  i32 turn = 0;
  for (char *it = array_begin(f.buffer); it != array_end(f.buffer); ++it) {
    switch (*it) {
    case '<':
      --x;
      if (turn == 0)
        --santa_x;
      else
        --robot_x;
      break;
    case '>':
      ++x;
      if (turn == 0)
        ++santa_x;
      else
        ++robot_x;
      break;
    case '^':
      --y;
      if (turn == 0)
        --santa_y;
      else
        --robot_y;
      break;
    case 'v':
      ++y;
      if (turn == 0)
        ++santa_y;
      else
        ++robot_y;
      break;
    }
    grid1[y * WIDTH + x] = 1;
    if (turn == 0)
      grid2[santa_y * WIDTH + santa_x] = 1;
    else
      grid2[robot_y * WIDTH + robot_x] = 1;

    ++turn;
    if (turn == 2)
      turn = 0;
  }

  i32 value1 = 0;
  i32 value2 = 0;
  for (i32 i = 0; i != WIDTH * HEIGHT; ++i) {
    if (grid1[i] != 0) {
      ++value1;
    }
    if (grid2[i] != 0) {
      ++value2;
    }
  }
  printf("2025 day 01 part 1: %d\n", value1);
  printf("2025 day 01 part 2: %d\n", value2);
}
