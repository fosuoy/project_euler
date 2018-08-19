#include<time.h>
#include<stdio.h>
#include<string.h>
#include<string>
#include<vector>
#include<algorithm>

void blurb()
{
    const char * blurb = R"(
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    )";
    printf("%s \n", blurb);
}

std::vector<int> find_palindromic_numbers(int lower_bound, int upper_bound)
{
    std::vector<int> palindromic_numbers;
    for (int a = upper_bound; a >= lower_bound ; a = a - 1) {
        std::string aString = std::to_string(a);
        std::string reversedAString = aString;
        std::reverse(reversedAString.begin(), reversedAString.end());
        if (aString == reversedAString) {
            palindromic_numbers.push_back(a);
        }
    }
    return palindromic_numbers;
}

int find_largest_factor(std::vector<int> nos, int lower_bound, int upper_bound)
{
    for (std::vector<int>::iterator it = nos.begin(); it != nos.end() ; ++it) {
        int no = *it;
        for (int j = upper_bound; j >= lower_bound; j--) {
            if (no % j == 0) {
                int divisor = no / j;
                if (lower_bound <= divisor && divisor <= upper_bound) {
                    printf("%d * %d == %d\n", j, divisor, no);
                    return no;
                }
            }
        }
    }
    return 0;
}

int problem_004(int lower_bound, int upper_bound)
{
    std::vector<int> palindromic_numbers = find_palindromic_numbers(
                                               lower_bound * lower_bound,
                                               upper_bound * upper_bound);
    return find_largest_factor(palindromic_numbers, lower_bound, upper_bound);
}

int main()
{
    blurb();
    clock_t begin = clock();
    int result = problem_004(100, 999);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    printf("Result: %d \n", result);
    printf("Completed in: %f seconds. \n", elapsed_secs);
}
