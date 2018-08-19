#!/usr/bin/env node

function printBlurb() {
    var blurb = `
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?

    This is going to take ~30 seconds to run, note the difference in runtime
    between this and the c++ solution...
    `
    console.log(blurb)
}

function divisible(test, upperBound) {
    var divisbleByAll = true
    for (var i = upperBound ; i >= 1 ; i--) {
        if (test % i != 0) {
            divisbleByAll = false
        }
    }
    return divisbleByAll
}

function problem_005(upperBound) {
    var i = upperBound
    var solutionReached = false
    while (solutionReached == false) {
        i += 1
        if (divisible(i, upperBound)) {
            solutionReached = true
            var result = i
        }
    }
    return result
}

printBlurb()
console.time('Completed in')
result = problem_005(20)
console.log(`Result: ${result}`)
console.timeEnd('Completed in')
