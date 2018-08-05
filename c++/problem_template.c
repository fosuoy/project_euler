#include<time.h>
#include<stdio.h>
/* Template for creating problem solutions */

int blurb(void)
{
    const char * blurb = R"(
        blurb.
    )";
    printf("%s \n", blurb);
}

int problem_xxx(int x)
{
    return x;
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    int result = problem_xxx(1);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    printf("Result: %d \n", result);
    printf("Completed in: %f seconds. \n", elapsed_secs);
    return 0;
}
