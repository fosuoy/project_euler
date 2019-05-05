#include<time.h>
#include<stdio.h>
#include<cmath>
#include<iostream>
/* Template for creating problem solutions */

void blurb()
{
    const char * blurb = R"(
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find
    the product abc.
    )";
    printf("%s \n", blurb);
}

int problem_009(int x)
{
    int result;
    for (int b = 2; b < x ; b++) {
        for (int a = 1; a < b; a++) {
            int c = x - a - b;
            int sides_squared = pow(a, 2) + pow(b, 2);
            if ((sides_squared == pow(c, 2)) && (a < b < c)) {
                std::cout << a << "^2 + " << b << "^2 = " << c << "^2" << "\n";
                result = a * b * c;
                break;
            }
        }
    }
    return result;
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    int result = problem_009(1000);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    printf("Result: %d \n", result);
    printf("Completed in: %f seconds. \n", elapsed_secs);
}
