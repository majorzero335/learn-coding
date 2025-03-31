var attempts = 0;
const maxtries = 5;
var name = prompt("What is your name?");
alert("Hello, " + name + "!");
alert("Welcome to the number guessing game!");
var str = Math.floor(Math.random() * 10) + 1;
alert("I am guessing a number from 1-10. Can you guess the number?");
alert("You can only get " + maxtries + " tries");
while (attempts < maxtries) {
    var guess = prompt("Please Guess a number");
    guess = parseInt(guess);
    attempts += 1;
    if (guess > str) {
        alert("Guess is too high, try a smaller number");
    } else if (guess < str) {
        alert("Guess is too low, try a higher number");
    } else if (guess == str) {
        alert("Correct- you win in " + attempts + " guesses");
        break;
    } else {
        alert("You failed to guess in time. The correct number was " + str + ". Better luck next time!"); // This line will execute if the user fails to guess correctly within the allowed attempts
    }
}
