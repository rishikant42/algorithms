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

(define (search ll data)
  (define (helper items)
    (cond ((null? items) #f)
          ((eq? (car items) data) #t)
          (else (helper (cdr items)))))
  (helper (head-ptr ll)))


(define (front-delete ll data)
  (cond ((empty-ll? ll) (error "DELETE called with an empty linkde list" ll))
        ((not (search ll data)) (error "Item is not present in list" ll))
        ((eq? (first-item ll) data) (set-head-ptr! ll (cdr (head-ptr ll)))
                                    ll)
        (else (display "Given item must be at front of list"))))
