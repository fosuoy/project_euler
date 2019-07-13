(ns project-euler.problem-01
  (:require [project-euler.common :as common])
  (:gen-class))

(defn problem-01-solve
  "
  problem 01... takes no arguments
  sum the multiples of 3 and 5 below 1000
  "
  []
  (let [blurb-text (str "If we list all the natural numbers below 10 that are \n"
                        "multiples of 3 or 5, we get 3, 5, 6 and 9.\n"
                        "The sum of these multiples is 23.\n"
                        "Find the sum of all the multiples of 3 or 5 below 1000.\n")
        upper-limit 999
        find-solution (fn fs [upper-limit & [result]]
                        (let [multiple? (or
                                          (zero? (mod upper-limit 3))
                                          (zero? (mod upper-limit 5)))
                              new-upper-limit (dec upper-limit)
                              result (or result 0)]
                          (if (zero? new-upper-limit)
                            result
                            (if multiple?
                              (fs new-upper-limit (+ result upper-limit))
                              (fs new-upper-limit result)))))]
  (common/blurb blurb-text)
  (newline)
  (-> (find-solution upper-limit) time clojure.pprint/pprint)))
