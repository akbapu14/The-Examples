(define (make-fact-stream)
    (define (factorial x size)
      (if (= 0 x)
          size
      (factorial (- x 1) (* x (- x 1)))))

    (define (helper x)
    (cons-stream (factorial x 0) (helper (- x 1))))
    (cons-stream 1 (helper 1))
)




scm> (stream-to-list (make-fact-stream 4))
(1 1 2 6)
