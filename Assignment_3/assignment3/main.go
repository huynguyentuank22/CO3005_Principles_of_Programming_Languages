package main

import "fmt"

var a Person

var c = a.age + 23

type Person struct {
	name string
	age  int
}
type Huy struct {
	name string
	age  int
}

type Haha interface {
	abc()
}

func (ha Huy) abc() {
	return
}
func (e Employee) a() {
	fmt.Println(e.salary)
}
func cd() {
	return
}

type Employee struct {
	salary int
}
type Human interface {
	print(a, b int)
}
var array = [3]int{1, 2, 3}
func (huy Huy) print(c float32, d int) {
	for i, i := range array {
		fmt.Println(i, array)
	}
	return
}
func main() {
	// q := Person{"John", 30}
	// q.print() // 🔹 Gọi phương thức print()
}
