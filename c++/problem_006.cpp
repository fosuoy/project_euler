#include<time.h>
#include<stdio.h>
#include<cmath>
/* Template for creating problem solutions */

void blurb()
{
    const char * blurb = R"(

    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten natural
    numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.

    )";
    printf("%s \n", blurb);
}

int sum_of_squares(int upper_limit) {
    int sum = 0;
    for (int number = upper_limit; number > 0 ; number = number - 1) {
        sum += pow(number, 2);
    }
    return sum;
}

int square_of_sum(int upper_limit) {
    int sum = 0;
    for (int number = upper_limit; number > 0 ; number = number - 1) {
        sum += number;
    }
    return pow(sum, 2);
}

int problem_006(int x)
{
    return square_of_sum(x) - sum_of_squares(x);
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    int result = problem_006(100);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    printf("Result: %d \n", result);
    printf("Completed in: %f seconds. \n", elapsed_secs);
}
