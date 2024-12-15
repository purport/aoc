
#include <stdio.h>
typedef unsigned char u8;
typedef double f64;
typedef int bool;
typedef unsigned int u32;
typedef int i32;

static f64 *tableau_pivot_column(u8 stride, u8 constraints, f64 *tableau) {
  u8 objective_row = stride * constraints;
  f64 most_negative = 0.0;
  f64 *pivot_column = 0;
  for (u8 i = 0; i != stride; ++i, ++tableau) {
    f64 coeff = tableau[objective_row];
    if (coeff < most_negative) {
      most_negative = coeff;
      pivot_column = tableau;
    }
  }
  return pivot_column;
}

static u8 tableau_pivot_row(u8 stride, u8 constraints, f64 *pivot_column,
                            f64 *constraint_column) {
  u8 pivot = constraints;
  f64 least_positive = 0;

  for (u8 i = 0; i != constraints; ++i) {
    if (*pivot_column > 0) {
      f64 ratio = *constraint_column / *pivot_column;
      if ((0 < ratio && ratio < least_positive) ||
          (0 < ratio && least_positive == 0)) {
        least_positive = ratio;
        pivot = i;
      }
    }
    pivot_column += stride;
    constraint_column += stride;
  }
  return pivot;
}

static void elementary_row_multiply(u8 stride, f64 *tableau, u8 row, f64 m) {
  f64 *it = tableau + row * stride;
  for (u8 i = 0; i != stride; ++i) {
    *it *= m;
    ++it;
  }
}

static void elementary_row_multiply_add(u8 stride, f64 *tableau, u8 row1, f64 m,
                                        u8 row2) {
  f64 *it1 = tableau + row1 * stride;
  f64 *it2 = tableau + row2 * stride;
  for (u8 i = 0; i != stride; ++i) {
    printf("%f = %f + %f * %f\n", *it1, *it1, m, *it2);
    *it1 += m * (*it2);
    printf("result %f\n\n", *it1);
    ++it1;
    ++it2;
  }
}

static void tableau_print(u8 stride, u8 constraints, f64 *tableau) {
  for (u8 i = 0; i != constraints + 1; ++i) {
    for (u8 j = 0; j != stride; ++j) {
      printf("%f", tableau[i * stride + j]);
      printf(" ");
    }
    printf("\n");
  }
}

static bool linear_programme_solve(u8 stride, u8 constraints, f64 *tableau) {
  while (1) {
    f64 *pivot_column = tableau_pivot_column(stride, constraints, tableau);
    if (pivot_column == 0) {
      printf("\n");
      return 1;
    }
    u8 pivot = tableau_pivot_row(stride, constraints, pivot_column,
                                 tableau + stride - 1);

    // clang-format off
    printf("r");printf("%d", pivot+1);printf(" -> ");printf("%f", 1.0 / pivot_column[pivot * stride]);printf("*r");printf("%d", pivot+1);printf("\n");
    // clang-format on

    elementary_row_multiply(stride, tableau, pivot,
                            1.0 / pivot_column[pivot * stride]);

    for (u8 i = 0; i != constraints + 1; ++i) {
      if (i == pivot)
        continue;
      // clang-format off
    printf("r");printf("%d", i+1);printf(" -> r");printf("%d", i+1);printf(" + ");printf("%f", -pivot_column[i * stride]);printf("*r");printf("%d", pivot+1);printf("\n");
      // clang-format on
      elementary_row_multiply_add(stride, tableau, i, -pivot_column[i * stride],
                                  pivot);
    }
    printf("\n");
    tableau_print(stride, constraints, tableau);
    printf("\n");
  }
}

// clang-format off
static f64 tableau[] = {
  26,   67,  1, 0, 12748+10000000000000,
  66,   21,  0, 1, 12176+10000000000000,
  -26-67+3,   -67-21+1,  0, 0, 0,
};
// clang-format on

i32 main() {

  tableau_print(4 + 1, 2, tableau);
  printf("\n");
  linear_programme_solve(4 + 1, 2, tableau);

  return 0;
}
