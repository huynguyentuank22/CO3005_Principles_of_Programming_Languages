package main

func isPalindrome(n int) bool {
	var reversed int = 0
	var original int = n
	for n > 0 {
		reversed = reversed*10 + n%10
		n = n / 10
	}
	return original == reversed
}

func searchInsert(nums []int, target int) int {
	var left int = 0
	var right int = len(nums) - 1
	for left <= right {
		var mid int = left + (right-left)/2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return left
}

// func isAnagram(s string, t string) {
// 	for var i =2; i<13; i+=1 {
// 		println(i);
// 	}
// }

func isValid(s string) bool {
	var stack []rune
	for _, c := range s {
		if c == '(' || c == '[' || c == '{' {
			stack = append(stack, c)
		} else if len(stack) == 0 {
			return false
		} else if c == ')' && stack[len(stack)-1] != '(' {
			return false
		} else if c == ']' && stack[len(stack)-1] != '[' {
			return false
		} else if c == '}' && stack[len(stack)-1] != '{' {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}
const a int = 10
type Knight struct {
	name string
	age int
}



func (k Knight) Attack() int {
	return k.ATK
}

func (k Knight) Defend() int {
	return k.DEF
}



func (k Knight) IsDead() [4]int {
	if k.HP <= 0 {
		return [4]int{1, 2, 3, 4}
	}
	return [4]int{1, 2, 3, 4}
}
func IsDead() {
	func (k Knight) IsDead2() {
		printlm("Hello");
	}
}

func main() {
	var p Knight = {"huy", 23}
	p.age = 13

	var sum int = 0
	var i = 0
	for ; i < 10; i += 1 {
		sum += i // loop body
	}
	var a = 00002
	var b = Person{name: 20, age: 30}
	println(a)
}
