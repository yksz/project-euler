<?php
// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

function fibonacci($max) {
    $array = array();
    $low = 1;
    $high = 1;
    while ($high < $max) {
        $tmp = $low;
        $low = $high;
        $high = $tmp + $high;
        $array[] = $low;
    }
    return $array;
}

$sum = 0;
$array = fibonacci(4000000);
foreach($array as $i)
    if ($i % 2 === 0)
        $sum += $i;
echo $sum, PHP_EOL;
