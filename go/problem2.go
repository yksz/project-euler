// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

package main

import (
	"fmt"
)

func fibonacci(max int) []int {
	slice := make([]int, 10)
	low, high := 1, 1
	for high < max {
		low, high = high, low+high
		slice = append(slice, low)
	}
	return slice
}

func main() {
	sum := 0
	for _, v := range fibonacci(4000000) {
		if v%2 == 0 {
			sum += v
		}
	}
	fmt.Println(sum)
}
