#include<time.h>
#include<stdio.h>
#include<iostream>
#include<vector>
/* Template for creating problem solutions */

void blurb()
{
    const char * blurb = R"(
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    )";
    printf("%s \n", blurb);
}

std::vector<long> eratosthenes_sieve(int number) {
    std::vector<bool> sieve(number + 1, true);
    std::vector<long> primes;
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

long problem_010(int x)
{
    std::vector<long> primes = eratosthenes_sieve(x);
    long sum = 0;
    for (int i = 0 ; i < primes.size() ; i++) {
        sum += primes[i];
    }
    return sum;
}

int main(void)
{
    blurb();
    clock_t begin = clock();
    long result = problem_010(2000000);
    clock_t end = clock();
    float elapsed_secs = ((float)end - (float)begin) / 1000000.0F;
    std::cout << "Result: " << result <<  "\n";
    printf("Completed in: %f seconds. \n", elapsed_secs);
}
