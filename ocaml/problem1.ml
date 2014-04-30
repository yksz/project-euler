(*
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 *)

let rec range a b =
    if a >= b then []
    else a :: range (a+1) b
;;

let lis = List.filter (fun x -> x mod 3 = 0 || x mod 5 = 0) (range 0 1000);;
let sum = List.fold_left (+) 0 lis;;
Printf.printf "%d\n" sum;;
