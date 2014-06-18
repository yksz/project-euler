;; If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
;; Find the sum of all the multiples of 3 or 5 below 1000.

(use srfi-1)

(define lis (map
                (lambda (x)
                    (if (or (= (modulo x 3) 0) (= (modulo x 5) 0))
                        x
                        0))
                (iota 1000)))

(define (sum)
    (fold + 0 lis))

(print (sum))
