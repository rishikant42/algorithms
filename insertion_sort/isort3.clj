(defn insert
  [l k]
  (concat
    (filter #(>= % k) l)
    [k]
    (filter #(< % k) l)))

(defn isort
  [list]
  (loop [sorted-list []
        unsorted-list list]
   (if (empty? unsorted-list) 
     sorted-list
     (recur (insert sorted-list (first unsorted-list))
            (rest unsorted-list)))))

(println (isort '(3 5 2 4 1 7 3 2 6 4 5)))

;; OUTPUT
;; 
;; $ clojure isort3.clj 
;; (7 6 5 5 4 4 3 3 2 2 1)
