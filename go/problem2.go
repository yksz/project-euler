// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
package main

import (
	"container/list"
	"fmt"
)

func main() {
	num := 4000000

	l := fibonacci(num)
	sum := 0
	for e := l.Front(); e != nil; e = e.Next() {
		val := e.Value.(int)
		if val%2 == 0 {
			sum += val
		}
	}
	fmt.Println(sum)
}

func fibonacci(num int) *list.List {
	list := list.New()

	low, high := 1, 1
	for high < num {
		low, high = high, low+high
		list.PushBack(low)
	}
	return list
}
