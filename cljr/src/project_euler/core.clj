(ns project-euler.core
  (:require [clojure.tools.cli :refer :all]
            [project-euler.core :refer :all]
            [project-euler.problem-01 :as problem-01]
            [project-euler.problem-02 :as problem-02]
            [project-euler.problem-03 :as problem-03])
  (:gen-class))

(defn -main
  "
  A stub method to import the problem files above to allow you to import the
  project euler solutions
  "
  [& args]
  (println "Hello, World!"))
