package main

import "fmt"

var a Person

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

func (huy Huy) print(c float32, d int) {
	return
}
func main() {
	// q := Person{"John", 30}
	// q.print() // 🔹 Gọi phương thức print()
}
