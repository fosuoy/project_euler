package main


import (
    "fmt"
    "time"
)


func blurb() {
    fmt.Println(`
    blurb
    `)
}


func problemXxx(x int) (result int) {
    result = x
    return
}


func main() {
    blurb()
    var start time.Time = time.Now()
    var result int = problemXxx(1)
    var end time.Time = time.Now()
    var elapsed time.Duration = end.Sub(start)
    fmt.Printf("Result: %v\n", result)
    fmt.Printf("Completed in: %v\n", elapsed)
}
