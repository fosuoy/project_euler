#!/usr/bin/env node

function printBlurb() {
    var blurb = `
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    `
    console.log(blurb)
}

function problem_003(primeFactorOf) {
    var factorToTest = 2
    while (factorToTest * factorToTest < primeFactorOf) {
        while (primeFactorOf % factorToTest == 0) {
            primeFactorOf = primeFactorOf / factorToTest
        }
        factorToTest += 1
    }
    return primeFactorOf
}

printBlurb()
console.time('Completed in')
result = problem_003(600851475143)
console.log(`Result: ${result}`)
console.timeEnd('Completed in')
