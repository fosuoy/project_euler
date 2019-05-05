#include<time.h>
#include<stdio.h>
#include<iostream>
/* Template for creating problem solutions */

void blurb()
{
    const char * blurb = R"(
        blurb.
    )";
    printf("%s \n", blurb);
}

long problem_xxx(int x)
{
    return x;
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    long result = problem_xxx(1);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    std::cout << "Result: " << result << "\n";
    std::cout << "Completed in: " << elapsed_secs << " seconds." << "\n";
}
