package main
import (
    "fmt"
    "math"
)

type Rectangle struct {
    width,height float64
}

type Circle struct {
    radius float64
}

func (r Rectangle) area() float64 {
    return r.width*r.height
}

func (c Circle) area() float64 {
    return c.radius * c.radius * math.Pi
}

func main() {
    r1 := Rectangle{12,2}
    r2 := Rectangle{9,4}
    C1 := Circle{10}
    C2 := Circle{25}
    
    fmt.Println("Area of r1 is:", r1.area())
    fmt.Println("Area of r2 is:", r2.area())
    fmt.Println("Area of C1 is:", C1.area())
    fmt.Println("Area of C2 is:", C2.area())
}
