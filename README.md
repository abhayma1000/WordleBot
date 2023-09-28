# WordleBot

### Overview

This is a bot to help people solve the wordle

It takes in input from the user based off results of wordle

Uses a dictionary to calculate all possible words and returns for the user to try

Then, the user updates the data and re-calculates. The cycle continues until word is correct
(or used up all tries)

### Instructions

* Run the python script and follow instructions from the output
* Update banned characters, specific placements, and somewhere
  * Banned characters are all characters that are nowhere in word
  * Specific placements are green characters that you know placement of
  * Somewhere are yellow words that you know are in the word, but don't know where
  * There is a specific way to input all this data, so follow carefully
* Can then generate possible words or print data (to ensure it is correct) to the screen
* Press 0 to exit once done

### Development

* Written in python and contained within a virtual environment
* Code contained in a main.py file