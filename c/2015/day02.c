#include "aoc.h"

i32 main(i32 argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Invalid arguments\n");
    exit(1);
  }

  struct file f = file_open(argv[1]);
  file_assert_open(f);

  i32 i = 0;
  char *it = array_begin(f.buffer);
  char *end = array_end(f.buffer);
  u64 value1 = 0;
  u64 value2 = 0;
  while (it != end) {
    u64 s1, s2, s3;
    it = parse_u64_x(it, end, &s1);
    it = parse_skip(it, end, "x\r\n");
    it = parse_u64_x(it, end, &s2);
    it = parse_skip(it, end, "x\r\n");
    it = parse_u64_x(it, end, &s3);
    it = parse_skip(it, end, "x\r\n");

    if (s1 > s2) {
      SWAP(s1, s2);
    }
    if (s2 > s3) {
      SWAP(s2, s3);
    }
    if (s1 > s2) {
      SWAP(s1, s2);
    }

    u64 s12 = s1 * s2;
    u64 s23 = s2 * s3;
    u64 s31 = s3 * s1;

    if (s12 > s23) {
      SWAP(s12, s23);
    }
    if (s23 > s31) {
      SWAP(s23, s31);
    }
    if (s12 > s23) {
      SWAP(s12, s23);
    }

    value1 += 2 * (s12 + s23 + s31) + s12;
    value2 += 2 * (s1 + s2) + s1 * s2 * s3;
  }
  printf("2025 day 01 part 1: %ld\n", value1);
  printf("2025 day 01 part 2: %ld\n", value2);
}
