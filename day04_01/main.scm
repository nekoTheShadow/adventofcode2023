(use srfi.13)

(define (main args)
  (define lines (call-with-input-file "./input.txt" port->string-list))
  (define sum 0)
  (dolist (line lines)
    (define cards1 (map string->number (string-split (substring line (+ 2 (string-index line #\:)) (- (string-index line #\|) 1)) #/\s+/)))
    (define cards2 (map string->number (string-split (substring line (+ 2 (string-index line #\|)) (string-length line)) #/\s+/)))
    (define c (count (lambda (card1) (contains cards2 card1)) cards1))
    (if (> c 0) (set! sum (+ sum (expt 2 (- c 1)))))
  )
  (print sum)
0)

(define (contains lst v)
  (find (lambda (u) (equal? u v)) lst)
)

