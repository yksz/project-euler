// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

object Main {

  def fibonacci(max: Int): List[Int] = {
    def loop(low: Int, high: Int, list: List[Int]): List[Int] = {
      if (high > max)
        return list
      else
        return loop(high, low + high, high :: list)
    }
    return loop(1, 1, List())
  }

  def sum(list: List[Int]): Int = {
    return list.foldLeft(0)((x, y) => x + y)
  }

  def sumOfEven(list: List[Int]): Int = {
    return sum(list.filter(x => x % 2 == 0))
  }

  def main(args: Array[String]) {
    println(sumOfEven(fibonacci(4000000)))
  }

}
