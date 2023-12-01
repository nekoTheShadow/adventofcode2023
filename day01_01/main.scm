(define (main args)
  (print (reduce + 0 (map calibration-value (read-lines "./input.txt"))))
0)

(define (read-lines filename)
  (call-with-input-file filename port->string-list))

(define (calibration-value line)
  (define integers (map digit->integer (filter char-numeric? (string->list line))))
  (+ (* 10 (list-ref integers 0)) (list-ref integers (- (length integers) 1))))