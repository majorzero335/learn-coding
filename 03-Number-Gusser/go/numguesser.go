const maxtries = 5;
var attempts = 0;
var name = prompt("What is your name?");
print("Hello " + name + "!");
print("Welcome to the number guessing game!");
var number = Math.floor(Math.random() * 10) + 1;
print("I am thinking of a number between 1 and 10. Can you guess it?");
print("You have " + maxtries + " tries to guess the number.");
while (attempts < maxtries) {
	var guess = prompt("Enter your guess:");
	attempts = attempts + 1;
	if (guess == number) {
		print("Congratulations " + name + "! You guessed the number!");
		break;
	}
	else if (guess < number) {
		print("Your guess is too low. Try again.");
	}
	else if (guess > number) {
		print("Your guess is too high. Try again.");
	}
	if (attempts == maxtries) {
		print("Sorry " + name + ", you have used all your tries. The number was " + number + ".");
	}
}	
