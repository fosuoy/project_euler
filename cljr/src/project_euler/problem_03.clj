(ns project-euler.problem-03
  (:require [project-euler.common :as common])
  (:gen-class))

(defn find-solution
  [solution]
  (let [result (time (eval solution))]
    (clojure.pprint/pprint (str ("Result: " result)))))

(defn problem-03-solve
  "
  problem 03... takes no arguments
  Prime factors...
  "
  []
  (let [blurb-text (str "The prime factors of 13195 are 5, 7, 13 and 29.\n"
                        "What is the largest prime factor of the number "
                        "600851475143?\n")
        main-prime-factor-of 600851475143
        find-prime-factors (fn fpf [& [prime-factor-of factor-to-test]]
                             (let [factor-to-test (or factor-to-test 1)
                                   prime-factor-of (or prime-factor-of main-prime-factor-of)
                                   new-factor-to-test (inc factor-to-test)
                                   squared-ftt (* factor-to-test factor-to-test)
                                   sftt-gt-pf? (> squared-ftt prime-factor-of)
                                   is-prime-factor? (zero? (mod prime-factor-of factor-to-test))
                                   new-prime-factor-of (if is-prime-factor?
                                                         (/ prime-factor-of factor-to-test)
                                                         prime-factor-of)
                                   ]
                               (if sftt-gt-pf?
                                 prime-factor-of
                                 (fpf new-prime-factor-of new-factor-to-test))))]
  (common/blurb blurb-text)
  (newline)
  (->> (find-prime-factors) time clojure.pprint/pprint)))
