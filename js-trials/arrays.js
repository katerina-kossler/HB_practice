"use strict";


/** 1. printIndices */
function printIndices(items) {
	// Replace this with your code
  // The output should look like this:
  //       apple 0
  //       berry 1
  //       cherry 2

  //   Arguments:
  //       items (list)

  //   Returns:
  //       None

  for (const i in items) {
    console.log(`${items[i]} ${i}`)
  }
}

printIndices(['apple', 'berry', 'cherry']);


/** 2. everyOtherItem */
function everyOtherItem(items) {
  // Print a list of every other item in `items`

  //   Start with index 0.

  //   Arguments:
  //       items (list)
  
  let result = [];

  for (const i in items) {
    if (i % 2 === 0) {
      result.push(items[i]);
    }
	}
  console.log(result);

}

everyOtherItem(['apple', 'berry', 'cherry']);


/** 3. smallestNItems */
function smallestNItems(items, n) {
	// Print a list of the `n` smallest integers in `items`.

    // Order the integers in descending order.

    // You can assume that `n` will be less than the length of the list.

    // Arguments:
    //     items (list[int]): A list of integers
    //     n (int): Desired length for the resulting list
  
  let sorted_items = items.sort((a, b) => b - a);

  let start = (sorted_items.length - n);
  let stop = sorted_items.length;
  console.log(sorted_items.slice(start, stop));
}

smallestNItems([1,5,10,200,5000,7,6,4,2,3],5);