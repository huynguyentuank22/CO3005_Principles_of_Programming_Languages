package main

type Person struct {
	Name string
	Age int
	func (p *Person) SayHello() {
		fmt.Println("Hello, my name is", p.Name)
	}
}