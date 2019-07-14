(ns project-euler.problem-05
  (:require [project-euler.common :as common]
            [clojure.string :as s])
  (:gen-class))

(defn- divisible?
  [number]
  (let [test-against-range (map #(mod number %) (range 11 21))]
    (every? zero? test-against-range)))

(defn- find-solution [] (loop [number 100]
                          (if (divisible? number) number (recur (+ number 20)))))


(defn solve-problem
  "
  problem 05... takes no arguments
  test if numbers are divisible against a range
  takes ~18 seconds to run which is too long!
  "
  []
  (let [blurb-text (str "2520 is the smallest number that can be divided by "
                        "each of the numbers from 1 to 10 without any "
                        "remainder.\n"
                        "What is the smallest positive number that is evenly "
                        "divisible by all of the numbers from 1 to 20?\n")]
  (common/blurb blurb-text)
  (newline)
  (->> (find-solution)
       time clojure.pprint/pprint)))
