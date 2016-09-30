(ns binary-search.core
  (:gen-class))

(defn bsearch1
  [k list]
  (if (= (count list) 1)
    (do (if (= (first list) k)
          (println "Element" k "is present in list")
          (println "Element" k "isn't present in list")))
    (let [mid (/ (count list) 2)
          current (nth list mid)
          split-list (split-at mid list)
          left (first split-list)
          right (last split-list)]
      (cond (= k current) (println "Element" k "is present in list")
            (< k current) (bsearch1 k left)
            :else (bsearch1 k right)))))

(defn bsearch2
  [k list]
  (loop [new-list list]
    (if (= (count new-list) 1)
      (do (if (= (first new-list) k)
            (println "Element" k "is present in list")
            (println "Element" k "isn't present in list")))
      (let [size (count new-list)
            mid (/ size 2)
            current (nth new-list mid)
            split-list (split-at mid new-list)
            left (first split-list)
            right (last split-list)]
        (cond (= k current) (println "Element" k "is present in list")
              (< k current) (recur left)
              :else (recur right))))))

(bsearch1 4 '(1 2 3 4 5 6 7 8 9 10))
(bsearch2 4 '(1 2 3 4 5 6 7 8 9 10))
