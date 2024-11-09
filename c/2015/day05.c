#include "aoc.h"

static bool is_vowel(char ch) {
  switch (ch) {
  case 'a':
  case 'e':
  case 'i':
  case 'o':
  case 'u':
    return true;
  }
  return false;
}

i32 main(i32 argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Invalid arguments\n");
    exit(1);
  }

  struct file f = file_open(argv[1]);
  file_assert_open(f);

  u64 value1 = 0, value2 = 0;
  char *it = array_begin(f.buffer);
  char *end = array_end(f.buffer);

  while (it != end) {
    u32 vowels = 0;
    u32 double_letter = 0;
    bool forbidden = false;
    while (it != end && *it != '\n') {
      if (*it == *(it + 1)) {
        ++double_letter;
      }
      if (*it == 'a' && *(it + 1) == 'b')
        forbidden |= true;
      if (*it == 'c' && *(it + 1) == 'd')
        forbidden |= true;
      if (*it == 'p' && *(it + 1) == 'q')
        forbidden |= true;
      if (*it == 'x' && *(it + 1) == 'y')
        forbidden |= true;

      if (is_vowel(*it++))
        ++vowels;
    }
    ++it;
    // printf("forbidden=%d, vowels=%d, double_letter=%d, %c\n", forbidden,
    // vowels, double_letter, *it);
    if (!forbidden && vowels >= 3 && double_letter >= 1) {
      ++value1;
    }
  }

  printf("2025 day 01 part 1: %ld\n", value1);
  printf("2025 day 01 part 2: %ld\n", value2);
}
