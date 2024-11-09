#pragma once
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

typedef unsigned char u8;
typedef int i32;
typedef unsigned int u32;
typedef long i64;
typedef unsigned long u64;

_Static_assert(sizeof(u8) == 1, "");
_Static_assert(sizeof(i32) == 4, "");
_Static_assert(sizeof(u32) == 4, "");
_Static_assert(sizeof(i64) == 8, "");
_Static_assert(sizeof(u64) == 8, "");

struct array {
  u64 length;
  void *pointer;
};

static void *array_begin(struct array a) { return a.pointer; }
static void *array_end(struct array a) { return &((u8 *)a.pointer)[a.length]; }

struct file {
  i32 error;
  struct array buffer;
};

static struct file file_open(char *filename) {
  i32 error = 0;
  i32 fd = open(filename, O_RDONLY);
  if (fd == -1) {
    error = errno;
  }

  void *buffer = NULL;
  struct stat buf = {0};
  if (error == 0) {
    if (fstat(fd, &buf) == -1) {
      error = errno;
    }
  }

  if (error == 0) {
    buffer = mmap(NULL, buf.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (buffer == MAP_FAILED) {
      error = errno;
      buffer = NULL;
    }
  }

  if (fd != -1) {
    close(fd);
    fd = -1;
  }

  return (struct file){error, buf.st_size, buffer};
}

static void file_assert_open(struct file f) {
  if (f.error != 0) {
    fprintf(stderr, "%s\n", strerror(f.error));
    exit(f.error);
  }
}

static char *parse_u64(char *it, char *end, u64 *result, bool *overflow) {
  u64 value = 0;
  *overflow = 0;
  while (it != end && '0' <= *it && *it <= '9') {
    *overflow |= __builtin_mul_overflow(value, 10, &value);
    *overflow |= __builtin_add_overflow(value, *it - '0', &value);
    ++it;
  }
  *result = value;
  return it;
}

static char *parse_u64_x(char *begin, char *end, u64 *result) {
  bool overflow = false;
  char *next = parse_u64(begin, end, result, &overflow);
  if (overflow != false) {
    fprintf(stderr, "Overflow\n");
    exit(1);
  }
  if (next == begin) {
    fprintf(stderr, "Number not found\n");
    exit(1);
  }
  return next;
}

static char *parse_skip(char *it, char *end, char *skips) {
  while (it != end) {
    char *s = &skips[0];
    while (*s != '\0' && *s != *it) {
      ++s;
    }
    if (*s == '\0')
      break;
    ++it;
  }
  return it;
}

static void to_string_u64(char *it, char *end, u64 value) {
  char temp[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  i32 i = 1;
  do {
    u64 digit = value % 10;
    value = (value - digit) / 10;
    temp[i++] = digit + '0';
  } while (value != 0);

  while (it != end && i != 0) {
    *it++ = temp[--i];
  }
}

#define MIN(a, b) (a < b ? a : b)
#define MAX(a, b) (a > b ? a : b)

#define SWAP(a, b)                                                             \
  do {                                                                         \
    __auto_type temp = a;                                                      \
    a = b;                                                                     \
    b = temp;                                                                  \
  } while (0)
