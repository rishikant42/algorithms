(define (head-ptr ll) (car ll))

(define (rear-ptr ll) (cdr ll))

(define (set-head-ptr! ll item) (set-car! ll item))

(define (set-rear-ptr! ll item) (set-cdr! ll item))

(define (make-ll) (cons '() '()))

(define (empty-ll? ll)
  (null? (head-ptr ll)))

(define (first-item ll)
  (if (empty-ll? ll)
    (error "FIRST-ITEM is called with empty linked list" ll)
    (car (head-ptr ll))))

(define (last-item ll)
  (if (empty-ll? ll)
    (error "LAST-ITEM is called with empty linked list" ll)
    (car (rear-ptr ll))))

(define (addfirst ll data)
  (let ((new-pair (cons data '())))
    (if (empty-ll? ll)
      (begin (set-head-ptr! ll new-pair)
             (set-rear-ptr! ll new-pair)
             ll)
      (begin (set-cdr! new-pair (head-ptr ll))
             (set-head-ptr! ll new-pair)
             ll))))

(define (addlast ll data)
  (let ((new-pair (cons data '())))
    (if (empty-ll? ll)
      (begin (set-head-ptr! ll new-pair)
             (set-rear-ptr! ll new-pair)
             ll)
      (begin (set-cdr! (rear-ptr ll) new-pair)
             (set-rear-ptr! ll new-pair)
             ll))))
