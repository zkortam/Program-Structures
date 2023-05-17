; Zakaria Kortam - COMSC 78 - Professor Estrada
; 4 May, 2023
; 1. Create a procedure that finds the cube of a number.
; 2. Create a procedure that sums all the numbers from a base to a ceiling.
; 3. Create a procedure that finds the pi sum of a value.
; 4. Create a procedure called sum-function that takes all of the other procedures and passes them within it.
; 5. Print and format all of the results.


(display ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
(newline)
(display ">>>>>>>>> Zakaria Kortam - COMSC 78 >>>>>>>>> ")
(newline)
(display ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
(newline)
(newline)

(define (cube x)
    (* x x x ))

(define (sum bottom top)
    (if (> bottom top)
        0
        (+ a (sum (+ a 1) b)))
)

(define (sum-cubes a b)
(if (> a b)
    0
    (+ (cube a) (sum-cubes (+ a 1) b))))

(define (pi-sum n)
(define (term k)
  (/ 8.0 (* (- (* 4 k) 3) (- (* 4 k) 1))))
(define (pi-sum-iter total k)
  (if (> k n)
      total
      (pi-sum-iter (+ total (term k)) (+ k 1))))
(* 4 (pi-sum-iter 0 1)))

(define (sum-function f a b)
(if (> a b)
    0
    (+ (f a) (sum-function f (+ a 1) b))))

(define result1 (sum-function identity 1 10))
(define result2 (sum-function cube 1 10))
(define result3 (sum-function (lambda (k) (/ 8.0 (* (- (* 4 k) 3) (- (* 4 k) 1)))) 0 1000)) 

(display "Result 1: ")
(display result1)
(newline)
(display "Result 2: ")
(display result2)
(newline)
(display "Result 3: ")
(display result3)
(newline)


