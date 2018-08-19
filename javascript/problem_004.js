#!/usr/bin/env node

function printBlurb() {
    var blurb = `
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    `
    console.log(blurb)
}

function reverseString(string) {
    var reversedString = string.split("").reverse().join("")
    return reversedString
}

function findPalindromicNumbers(lowerBound, upperBound) {
    var palindromicNumbers = []
    for (var i = lowerBound ; i < upperBound ; i ++) {
        iString = i.toString()
        if (iString == reverseString(iString)) {
            palindromicNumbers.push(i)
        }
    }
    return palindromicNumbers

}

function numSort(a, b) {
    return a - b
}

function findLargestFactor(palindromicNumbers, lowerBound, upperBound) {
    var palindromicNumbersSorted = palindromicNumbers.sort(numSort).reverse()
    for (var i = 0 ; i < palindromicNumbersSorted.length ; i++) {
        var palindromicNumber = palindromicNumbersSorted[i]
        for (var j = upperBound ; j >= lowerBound ; j--) {
            if (palindromicNumber % j == 0) {
                var divisor = palindromicNumber / j
                if (lowerBound <= divisor && divisor <= upperBound) {
                    console.log("%d * %d == %d\n", j, divisor, palindromicNumber)
                    return palindromicNumber
                }
            }
        }
    }
}

function problem_004(lowerBound, upperBound) {
    palindromicNumbers = findPalindromicNumbers(lowerBound*lowerBound, upperBound*upperBound)
    return findLargestFactor(palindromicNumbers, lowerBound, upperBound)
}

printBlurb()
console.time('Completed in')
result = problem_004(100, 999)
console.log(`Result: ${result}`)
console.timeEnd('Completed in')
