(defn qsort [[pivot & xs]]
  (when pivot
    (let [smaller #(< % pivot)]
      (lazy-cat (qsort (filter smaller xs))
                [pivot]
                (qsort (remove smaller xs))))))

(println (qsort '(3 8 6 4 7 5 0 2 1 11 10 12)))
