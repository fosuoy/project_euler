#!/usr/bin/env node

function printBlurb() {
    var blurb = `
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we
    get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    `
    console.log(blurb)
}

function problem_001(upperBound) {
    var sumResult = 0;
    var i;
    for (i = 1 ; i < upperBound; i++) {
        if (i % 3 == 0) {
            sumResult += i
        } else if (i % 5 == 0) {
            sumResult += i
        }
    }
    return sumResult
}

printBlurb()
console.time('Completed in')
result = problem_001(1000)
console.log(`Result: ${result}`)
console.timeEnd('Completed in')
