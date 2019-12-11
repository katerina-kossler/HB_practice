"use strict";


/** 1. countWords */
function countWords(phrase) {
	// Return a dictionary of each word and the no. of times they appear.

  //    You can assume that `phrase` does not contain any punctuation and that
  //    each word is separated with a space.

  //    Arguments:
  //        phrase (str): A string of space-separated words

  //    Returns:
  //        dict: {word: # of times word appears in `phrase`}
  let wordCounts = {};
  let words = phrase.split(' ');

  for (const word of words) {
    if (!wordCounts[word]) {
      wordCounts[word] = 1;
    }
    else {
      wordCounts[word] += 1
    } 
  }
  return wordCounts;
}

console.log(countWords('bananas are good for bananas are good for bananas'))

/** 2. getMelonsAtPrice */
function getMelonsAtPrice(price) {
	// Replace this with your code
}
