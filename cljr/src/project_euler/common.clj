(ns project-euler.common
  (:gen-class))

(defn blurb
  "
  Print out question blurb
  "
  [blurb]
  (let [lines (clojure.string/split-lines blurb)]
    (doseq [line lines]
      (clojure.pprint/pprint line))))
