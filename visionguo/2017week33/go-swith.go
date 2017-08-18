package main

import "fmt"

func main() {
    i := 6
    switch i {
    case 4:
        fmt.Println("The i is <= 4")
    fallthrough
    case 5:
        fmt.Println("The i is <= 5")
    fallthrough
    case 6:
        fmt.Println("The i is <= 6")
    fallthrough
    case 7:
        fmt.Println("The i is <= 7")
    fallthrough
    case 8:
        fmt.Println("The i is <= 8")
    fallthrough
    default:
    fmt.Println("default case")
}
}
