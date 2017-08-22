package main
import "fmt"

type Human struct {
    name string
    age int
    weight int
}

type Student struct {
    Human 
    speciality string
}

func main() {
    visionguo := Student{Human{"visionguo",24,126},"Electronic Science and Technology " }
    fmt.Println("His name is", visionguo.name)
    fmt.Println("His age is", visionguo.age)
    fmt.Println("His weight is", visionguo.weight)
    fmt.Println("His speciality is", visionguo.speciality)

    visionguo.speciality = "AI"
    fmt.Println("visionguo changed his speciality")
    fmt.Println("His speciality is", visionguo.speciality)

    visionguo.age = 25
    fmt.Println("visionguo changed his age")
    fmt.Println("His age is", visionguo.age)

    visionguo.weight += 30 
    fmt.Println("visionguo changed his weight")
    fmt.Println("His weight is", visionguo.weight)
}

