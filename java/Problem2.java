// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import java.util.LinkedList;
import java.util.List;

public class Problem2 {

    private static List<Integer> fibonacci(int max) {
        List<Integer> list = new LinkedList<Integer>();
        int low = 1;
        int high = 1;
        while (high < max) {
            int tmp = low;
            low = high;
            high = tmp + high;
            list.add(low);
        }
        return list;
    }

    public static void main(String[] args) {
        int sum = 0;
        for (int i : fibonacci(4000000))
            if (i % 2 == 0)
                sum += i;
        System.out.println(sum);
    }

}