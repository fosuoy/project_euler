package main


import (
    "fmt"
    "time"
)


func blurb() {
    fmt.Println(`
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    `)
}


func divisibleByInts(test int, upperBound int) (divByAll bool) {
    divByAll = true
    for i := upperBound ; i >= 1 ; i-- {
        if (test % i != 0) {
            divByAll = false
            break
        }
    }
    return divByAll
}


func problem005(upperBound int) (result int) {
    var solutionReached bool = false
    var i int
    for solutionReached != true {
        i += 1
        if (i <= upperBound) {
            continue
        }
        if (divisibleByInts(i, upperBound)) {
            result = i
            solutionReached = true
        }
    }
    return
}


func main() {
    blurb()
    var start time.Time = time.Now()
    var result int = problem005(20)
    var end time.Time = time.Now()
    var elapsed time.Duration = end.Sub(start)
    fmt.Printf("Result: %v\n", result)
    fmt.Printf("Completed in: %v\n", elapsed)
}
