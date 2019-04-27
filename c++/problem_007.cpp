#include<time.h>
#include<stdio.h>
#include<vector>
#include<iostream>
#include<cmath>

void blurb()
{
    const char * blurb = R"(
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?
    )";
    printf("%s \n", blurb);
}

std::vector<int> eratosthenes_sieve(int number) {
    std::vector<bool> sieve(number + 1, true);
    std::vector<int> primes;
    sieve[0] = false;
    sieve[1] = false;
    for (int p=2; p*p<=number; p++) { 
        if (sieve[p] == true) { 
            for (int i=p*p; i<=number; i += p) 
                sieve[i] = false; 
        } 
    } 
    for (int p=2; p<=number; p++) {
        if (sieve[p]) {
            primes.push_back(p);
        }
    }
    return primes;
}

int problem_007(int x)
{
    std::vector<int> primes = eratosthenes_sieve(pow(x, 1.5));
    return primes[x - 1];
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    int result = problem_007(10001);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    printf("Result: %d \n", result);
    printf("Completed in: %f seconds. \n", elapsed_secs);
}
