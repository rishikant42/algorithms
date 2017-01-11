(define (front-ptr stack) (car stack))

(define (rear-ptr stack) (cdr stack))

(define (set-front-ptr! stack item) (set-car! stack item))

(define (set-rear-ptr! stack item) (set-cdr! stack item))

(define (make-stack) (cons '() '()))

(define (empty-stack? stack)
  (null? (front-ptr stack)))

(define (top-item stack)
  (if (empty-stack? stack)
    (error "TOP-ITEM called with an empty stack" stack)
    (car (front-ptr stack))))

(define (bottom-item stack)
  (if (empty-stack? stack)
    (error "BOTTOM-ITEM called with an empty stack" stack)
    (car (rear-ptr stack))))

(define (push! stack item)
  (let ((new-pair (cons item '())))
    (if (empty-stack? stack)
      (begin (set-front-ptr! stack new-pair)
             (set-rear-ptr! stack new-pair)
             stack)
      (begin (set-cdr! new-pair (front-ptr stack))
             (set-front-ptr! stack new-pair)
             stack))))

(define (pop! stack)
  (if (empty-stack? stack)
    (error "POP is called with an empty stack" stack)
    (begin (set-front-ptr! stack (cdr (front-ptr stack)))
           stack)))

;; TEST

;; 1 ]=> (define s (make-stack))
;; 
;; ;Value: s
;; 
;; 1 ]=> s
;; 
;; ;Value 11: (())
;; 
;; 1 ]=> (push! s 'a)
;; 
;; ;Value 11: ((a) a)
;; 
;; 1 ]=> (push! s 'b)
;; 
;; ;Value 11: ((b a) a)
;; 
;; 1 ]=> (push! s 'c)
;; 
;; ;Value 11: ((c b a) a)
;; 
;; 1 ]=> (top-item s)
;; 
;; ;Value: c
;; 
;; 1 ]=> (bottom-item s)
;; 
;; ;Value: a
;; 
;; 1 ]=> (pop! s)
;; 
;; ;Value 11: ((b a) a)
;; 
;; 1 ]=> (pop! s)
;; 
;; ;Value 11: ((a) a)
;; 
;; 1 ]=> (top-item s)
;; 
;; ;Value: a
