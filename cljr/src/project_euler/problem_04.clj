(ns project-euler.problem-04
  (:require [project-euler.common :as common]
            [clojure.string :as s])
  (:gen-class))

(defn- find-solution
  [solution]
  (let [result (time (eval solution))]
    (clojure.pprint/pprint (str ("Result: " result)))))

(defn- palindromic?
  [number]
  (let [reversed (-> (str number) reverse s/join)
        number-s (-> number str)]
    (if (= reversed number-s) true false)))

(defn- find-largest-palindromic-product
  [lower-range upper-range s-pallindrome l-pallindrome]
  (let [palindromes (filter palindromic? (range s-pallindrome l-pallindrome))
        biggest-divisor upper-range
        results (for [palindrome palindromes
                      x (range lower-range upper-range)
                      :when (and
                              (= (mod palindrome x) 0)
                              (> upper-range (/ palindrome x)))]
                  palindrome)]
    (apply max results)))

(defn problem-04-solve
  "
  problem 04... takes no arguments
  Palindromes...
  "
  []
  (let [blurb-text (str "A palindromic number reads the same both ways.\n"
                        "The largest palindrome made from the product of "
                        "two 2-digit numbers is 9009 = 91 × 99.\n"
                        "Find the largest palindrome made from the product of "
                        "two 3-digit numbers.")
        number-of-digits 3
        upper-range (if (= number-of-digits 2) 100 1000)
        lower-range (if (= number-of-digits 2) 10 100)
        smallest-palindrome (if (= number-of-digits 2) 100 10000)
        biggest-palindrome (if (= number-of-digits 2) 9801 998001)
        ]
  (common/blurb blurb-text)
  (newline)
  (->> (find-largest-palindromic-product lower-range upper-range
                                         smallest-palindrome biggest-palindrome)
       time clojure.pprint/pprint)))
