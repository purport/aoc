#include "aoc.h"
#include <openssl/md5.h>
#include <stdio.h>
#include <string.h>

i32 main() {
  static char input[255] = "ckczppom";
  u32 start = strlen(input);
  bool got5zeros = false;
  bool got6zeros = false;
  for (u64 value1 = 0; value1 != 0xffffffff; ++value1) {

    to_string_u64(&input[start], &input[255], value1);

    unsigned char result[MD5_DIGEST_LENGTH];
    MD5((unsigned char *)input, strlen(input), result);

    if (result[0] == 0 && result[1] == 0 && (result[2] & 0xf0) == 0 &&
        !got5zeros) {
      printf("2025 day 01 part 1: %lu\n", value1);
      got5zeros = true;
    }
    if (result[0] == 0 && result[1] == 0 && result[2] == 0 && !got6zeros) {
      printf("2025 day 01 part 2: %lu\n", value1);
      got6zeros = true;
    }

    if (got5zeros && got6zeros)
      break;
  }
}
