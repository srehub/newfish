package main
import  "fmt"

type  Human struct  {
    name  string
    age  int
    phone  string
}

type Student  struct  {
    Human  //匿名字段
    school  string
}

type  Employee  struct  {
    Human  //匿名字段
    company  string
}

//在human上面定义了一个method
func (h  *Human) SayHi()  {
    fmt.Printf("Hi，I am %s  you can call me on %s\n", h.name, h.phone)
}

func main()  {
    visionguo := Student{Human{"visionguo",24,"188-xxxx-xxxx"},"XUPT"}
    AllenSu := Employee{Human{"AllenSu",33,"133-yyyy-yyyy"},"sydney"}

    visionguo.SayHi()
    AllenSu.SayHi()
}
