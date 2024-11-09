#include "aoc.h"

i32 main(i32 argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Invalid arguments\n");
    exit(1);
  }

  struct file f = file_open(argv[1]);
  file_assert_open(f);

  i32 value = 0;
  i32 basement_index = 0;
  i32 index = 1;
  for (char *it = array_begin(f.buffer); it != array_end(f.buffer);
       ++it, ++index) {
    if (*it == '(')
      ++value;
    if (*it == ')')
      --value;

    if (value == -1 && basement_index == 0)
      basement_index = index;
  }

  printf("2025 day 01 part 1: %d\n", value);
  printf("2025 day 01 part 2: %d\n", basement_index);
}
