(defn isort
  [arg]
  (loop [sorted-list []
         unsorted-list arg]
    (if (empty? unsorted-list)
      sorted-list
      (recur (cons (apply min unsorted-list) sorted-list)
             (remove (fn [x] (= x (apply min unsorted-list))) unsorted-list)))))

(println (isort '(8 3 1 5 6 2 7 4 )))

;; => (remove (fn[x] (= x 3)) '(1 2 3 4 5))
;; (1 2 4 5)
