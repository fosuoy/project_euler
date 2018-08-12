package main


import (
    "fmt"
    "time"
    "strconv"
)


func blurb() {
    fmt.Println(`
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    `)
}


func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}


func findPalindromicNumbers(lowerBound, upperBound int) []int {
    palindromes := make([]int, 0)
    for i := lowerBound; i < upperBound ; i++ {
        iString := strconv.Itoa(i)
        if iString == Reverse(iString) {
            palindromes = append(palindromes, i)
        }
    }
    return palindromes
}


func findLargestFactor(numbers []int, lowerBound int, upperBound int) int {
    var result int
    for i := len(numbers) - 1 ; i >= 0 ; i-- {
        var palindromicNumber int = numbers[i]
        for j := upperBound ; j >= lowerBound ; j-- {
            if palindromicNumber % j == 0 && lowerBound <= j && j <= upperBound {
                var divisor int = palindromicNumber / j
                if lowerBound <= divisor && divisor <= upperBound {
                    fmt.Printf("%d * %d == %d\n", j, divisor, palindromicNumber)
                    return palindromicNumber
                }
            }
        }
    }
    return result
}


func problem004() (result int) {
    palindromicNumbers := findPalindromicNumbers(100*100, 999*999)
    result = findLargestFactor(palindromicNumbers, 100, 999)
    return
}


func main() {
    blurb()
    var start time.Time = time.Now()
    var result int = problem004()
    var end time.Time = time.Now()
    var elapsed time.Duration = end.Sub(start)
    fmt.Printf("Result: %v\n", result)
    fmt.Printf("Completed in: %v\n", elapsed)
}
