const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';
const WORDS = [
  'strawberry', 'orange', 'apple', 'banana', 'pineapple', 'kiwi',
  'peach', 'pecan', 'eggplant', 'durian', 'peanut', 'chocolate'
];


let numWrong = 0;


/** Loop over the chars in `word` and create divs. */
const createDivsForChars = (word) => {
  // Loops through letters of guess word to make a div for each letter

  for (letter of word) {
    $('#word-container').append(`<div class="letter-box ${letter}"></div>`);
  }
};


/** Loop over each letter in `ALPHABET` and generate buttons. */
const generateLetterButtons = () => {
  // Creates a button for each letter in the alphabet to guess

  for (letter of ALPHABET) {
    $('#letter-buttons').append(`<button>${letter}</button>`);
  }
};


/** Set the `disabled` property of `buttonEl` to `true.
 *
 * `buttonEl` is an `HTMLElement` object.
 */
const disableLetterButton = (buttonEl) => {
  // Disables a button after clicking (guessing) the letter from alphabet

  const jQueryEl = $(buttonEl);
  jQueryEl.attr('disabled','true')

};


/** Return `true` if `letter` is in the word. */
const isLetterInWord = (letter) => {
  // Checks is a guessed letter is in the word they are gessing against

  return ($('div').hasClass(`letter-box ${letter}`))
};


/** Called when `letter` is in word. Update contents of divs with `letter`. */
const handleCorrectGuess = (letter) => {
  // Replaces div contents of matching letters with correctly guessed letter

  const letterBoxes = $('div.letter-box')
  for (box of letterBoxes) {
    if ($('div.letter-box').hasClass(`${letter}`)) {
      $(`div.letter-box.${letter}`).html(`${letter}`)
    }
  }
};


/** Called when `letter` is not in word.
 *
 * If the shark gets the person, disable all buttons and show the "play again"
 * message. Otherwise, increment `numWrong` and update the shark image.
 */
const handleWrongGuess = () => {
  // Checks number of wrong guesses and either increases wrong guesses or resets the game
  numWrong += 1;
  $('img').attr('src', `images/guess${numWrong}.png`);
  if (numWrong === 5) {
    $('button').attr('disabled','true');
    $('#play-again').css('display', 'inline');
    }
  };


/** Reset game state. Called before restarting the game. */
const resetGame = () => {
  // Rests game to beginning which play again link is clicked

  numWrong = 0;
  $('img').attr('src', 'images/guess0.png')
  $('#play-again').css('display', 'none');
  $('#word-container').empty();
  $('#letter-buttons').empty();
};



/** This is like if __name__ == '__main__' in Python */

(function startGame() {
  // For now, we'll hardcode the word that the user has to guess.
  const wordIndex = Math.floor(Math.random() * WORDS.length);
  const word = WORDS[wordIndex];

  createDivsForChars(word);
  generateLetterButtons();

  $('button').on('click', (evt) => {
    const clickedBtn = $(evt.target);
    disableLetterButton(clickedBtn);

    const letter = clickedBtn.html();

    if (isLetterInWord(letter)) {
      handleCorrectGuess(letter);
    } else {
      handleWrongGuess(letter);
    }
  });

  $('#play-again').on('click', () => {
    resetGame();
    startGame();
  });
})();
