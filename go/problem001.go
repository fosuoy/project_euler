package main


import (
    "fmt"
    "time"
)


func blurb() {
    fmt.Println(`
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we
    get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    `)
}


func problem_001(upperLimit int) (sum int) {
    sum = 0
    for i := 1; i < upperLimit; i++ {
        if i % 3 == 0 {
            sum += i
        } else if i % 5 == 0 {
            sum += i
        }
    }
    return sum
}


func main() {
    blurb()
    var start time.Time = time.Now()
    var result int = problem_001(1000)
    var end time.Time = time.Now()
    var elapsed time.Duration = end.Sub(start)
    fmt.Printf("Result: %v\n", result)
    fmt.Printf("Completed in: %v\n", elapsed)
}
