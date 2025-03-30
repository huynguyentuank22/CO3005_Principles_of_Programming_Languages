package main


type A interface{
	getInt() int
}
type B struct {
	x int;
}
func (b B) getInt(b int) int{
	return b.x
}
func (b B) dosth(){
	return;
}

func main() {
	// var a A
	// a = B{x: 5}
	// a.dosth()

}