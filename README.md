# sp24-lab3
Lab 3, which includes (a) "Duplicate Files" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson (b) command line integration example with sys.argv, (c) and example of how to use the simpleaudio package to play a .wav file in Python.

_January 30, 2024_

Organization:
* SDX-Ch3: The code files for the _SDX Ch.3_ activity (as downloaded directly from the book website, unmodified) 
* TeamActivities: Has the code files for the command line activity (cli_example.py), the simpleaudio activity (simpleaudio_test.py), and two sample .wav audio files in the sounds subfolder.

## Team Members
Luke Samuels (done late, 2/2/23)

## Team Roles
Who will start out as
* DRIVER: Driver's name
* NAVIGATOR: Navigator's name

You will switch halfway through the _SDX Ch. 3_ activity.

## SDX Ch. 3 documentation

Write your answers to the questions below.

* What were the main ideas from each chapter?
* What questions did you have about the material in the chapters? What did you find confusing?

After you've modified/remixed the code, write a summary of what you did and why below:

I took out the .out files and stuck them in a directory. Then I made a _SCHEMA.txt file to keep
track of how the different files interactied with each other... turns out they don't, at all.
Instead, I included a brief summary of what each file did (not all files were included but you
can get the idea). Finally, I went through and added some much-needed comments to the files. If
this were an actual project, I would have added a standardized comment scheme including dates,
inputs/outputs, and so on, but in the interest of this not taking all day I just put in a few.

After you've worked on the exercises, write a summary of what you did and why below:

Exercise 1 response:
It seems like hashing audio files works just fine. Running dup.py with the
argument ../sounds/* presented that coffee.wav and coffee-slurp-6.wav were identical.

Exercise 2 response:
I managed to get the repo-wide duplicate checker working (it's in a new folder called duplicate-checker).
In real life this thing would get slow without some sort of data structure underlying the known_hashes
file, plus the known_hashes file is prone to getting deleted. Otherwise though, it totally worked out!


