(use srfi.13 )

(define (main args)
  (print (reduce + 0 (map check (read-lines "./input.txt"))))
0)

(define (read-lines filename)
  (call-with-input-file filename port->string-list))

(define (check line)
  (define ID (string->number (rxmatch->string #/[0-9]+/ line)))
  (let loop ((sets (string-split (substring line (+ 1 (string-index line #\:)) (string-length line)) #[,;]))
             (ok #t))
    (if (null? sets)
      (if ok ID 0)
      (let* ((ball-color (string-split (string-trim (car sets)) " "))
             (ball (string->number (car ball-color)))
             (color (cadr ball-color)))
        (cond ((and (equal? color "red")   (<= ball 12)) (loop (cdr sets) #t))
              ((and (equal? color "green") (<= ball 13)) (loop (cdr sets) #t))
              ((and (equal? color "blue")  (<= ball 14)) (loop (cdr sets) #t))
              (else (loop '() #f)))))))