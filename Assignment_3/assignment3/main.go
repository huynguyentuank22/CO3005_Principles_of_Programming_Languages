package main

import "fmt"

type Person struct {
	name string
	age  int
}
type Huy struct {
	name string
	age  int
}
type Employee struct {
	salary int
}

func (p Person) print() {
	fmt.Println(p.name, p.age)
}
func (e Employee) print() {
	fmt.Println(e.salary)
}

type Human interface {
	print(a, b int)
}

func (huy Huy) print(c float32, d int) {
	return
}
func main() {
	q := Person{"John", 30}
	q.print() // 🔹 Gọi phương thức print()
}
