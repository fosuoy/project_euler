#include<time.h>
#include<stdio.h>
#include<stdbool.h>
/* Template for creating problem solutions */

void blurb()
{
    const char * blurb = R"(
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    )";
    printf("%s \n", blurb);
}

bool Divisible(int test, int upper_bound)
{
    bool div_by_all = true;
    for (int i = upper_bound ; i >= 1 ; i = i - 1) {
        if (test % i != 0) {
            div_by_all = false;
            break;
        }
    }
    return div_by_all;
}

int problem_005(int upper_bound)
{
    bool solution_reached = false;
    int i;
    int result;
    while (solution_reached == false) {
        i = i + 1;
        if (i <= upper_bound) {
            continue;
        }
        bool is_divisible_by_all = Divisible(i, upper_bound);
        if (is_divisible_by_all == true) {
            result = i;
            break;
        }
    }
    return result;
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    int result = problem_005(20);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    printf("Result: %d \n", result);
    printf("Completed in: %f seconds. \n", elapsed_secs);
}
