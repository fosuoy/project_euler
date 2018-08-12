#include<time.h>
#include<stdio.h>
/* Template for creating problem solutions */

int blurb(void)
{
    const char * blurb = R"(
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143.
    )";
    printf("%s \n", blurb);
}

int problem_003(long int prime_factor_of)
{
    int factor_to_test = 2;
    while (factor_to_test * factor_to_test < prime_factor_of) {
        while (prime_factor_of % factor_to_test == 0) {
            prime_factor_of = prime_factor_of / factor_to_test;
        }
        factor_to_test += 1;
    }
    return prime_factor_of;
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    int result = problem_003(600851475143);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    printf("Result: %d \n", result);
    printf("Completed in: %f seconds. \n", elapsed_secs);
    return 0;
}
