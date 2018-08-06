#!/usr/bin/env node

function printBlurb() {
    var blurb = `
    blurb
    `
    console.log(blurb)
}

function problem_xxx(x) {
    return x
}

printBlurb()
console.time('Completed in')
result = problem_xxx(1)
console.log(`Result: ${result}`)
console.timeEnd('Completed in')
