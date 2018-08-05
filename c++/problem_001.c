#include<time.h>
#include<stdio.h>
/* https://projecteuler.net/problem=1 */

int blurb(void)
{
    const char * blurb = R"(
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
    )";
    printf("%s \n", blurb);
}

int problem_001(int upper_bound)
{
    int result = 0;
    for( int a = 1; a < upper_bound ; a = a + 1) {
        if (a % 3 == 0) {
            result += a;
        } else if (a % 5 == 0) {
            result += a;
        }
    }
    return result;
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    int result = problem_001(1000);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    printf("Result: %d \n", result);
    printf("Completed in: %f seconds. \n", elapsed_secs);
    return 0;
}
