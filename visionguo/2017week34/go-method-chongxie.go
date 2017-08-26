package main
import "fmt"

type  Human  struct {
    name  string
    age int
    phone string
}

type Student  struct {
    Human  //匿名字段
    school string
}

type  Employee  struct {
    Human //匿名字段
    company  string
}

//Human定义method
func (h *Human) SayHi() {
    fmt.Printf("Hi,I am %s you can call me on %s\n", h.name, h.phone)
}

//Employee的method重写Human的method
func (e *Employee) SayHi () {
    fmt.Printf("Hi,I am %s, I work at %s, Call me on %s\n", e.name, e.company, e.phone)  
}

func main()  {
    leo := Student{Human{"leo", 30, "010-xxxx-xxxx"},"peking"}
    messi := Employee{Human{"messi",29,"029-yyyy-yyyy"}, "Barcelona"}

    leo.SayHi()
    messi.SayHi()
}
