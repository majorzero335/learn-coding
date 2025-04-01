var attempts = 0;
const maxtries = 5;
var n = prompt("What is your name?");
alert("Hello, " + n + "!");
alert("Welcome to the number guessing game!");
var number = Math.floor(Math.random() * 10) + 1;
alert("I am guessing a number from 1-10. Can you guess the number?");
alert("You can only get " + maxtries + " tries");
while (attempts < maxtries) {
    var guess = prompt("Please Guess a number");
    guess = parseInt(guess);
    attempts += 1;
    if (guess > number) {
        alert("Guess is too high, try a smaller number");
    } else if (guess < number) {
        alert("Guess is too low, try a higher number");
    } else if (guess == number) {
        alert("Correct- you win in " + attempts + " guesses");
        break;
    } else {
        alert("You failed to guess in time. The correct number was " + number + ". Better luck next time!");
    }
}
