package main


import (
    "fmt"
    "time"
)


func blurb() {
    fmt.Println(`
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    `)
}


func problem003(primeFactorOf int) (result int) {
    var factorToTest int = 2
    for (factorToTest * factorToTest < primeFactorOf) {
        for (primeFactorOf % factorToTest == 0) {
            primeFactorOf = primeFactorOf / factorToTest
        }
        factorToTest += 1
    }
    return primeFactorOf
}


func main() {
    blurb()
    var start time.Time = time.Now()
    var result int = problem003(600851475143)
    var end time.Time = time.Now()
    var elapsed time.Duration = end.Sub(start)
    fmt.Printf("Result: %v\n", result)
    fmt.Printf("Completed in: %v\n", elapsed)
}
