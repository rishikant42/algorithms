(defn merged
  [left right]
  (cond (nil? left) right
        (nil? right) left
        :else
          (let [[l & *left] left
                [r & *right] right]
            (if (<= l r) 
              (cons l (merged *left right))
              (cons r (merged left *right))))))

(defn msort
  [list]
  (if (< (count list) 2)
    list
    (let [mid (/ (count list) 2)
         [left right] (split-at mid list)]
     (merged (msort left) (msort right))))) 

(println (msort '(3 5 7 1 2 3 4 6 5 4 1)))

;; OUTPUT
;; 
;; $ clojure msort1.clj 
;; (1 1 2 3 3 4 4 5 5 6 7)
