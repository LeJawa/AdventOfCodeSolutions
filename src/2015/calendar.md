# Advent of Code 2015

## [Day 1: Not Quite Lisp](https://adventofcode.com/2015/day/1)

### Part One

Starting from floor 0, we simply add 1 for each `(` and subtract 1 for each `)`. The final floor is the answer.

### Part Two

Part 2 is similar, except we keep track of the indices of the instructions. When the floor hits -1, the index of the last instruction  is the answer.

## [Day 2: I Was Told There Would Be No Math](https://adventofcode.com/2015/day/2)

### Part One

For each L x W x H, we add `2 * (LW + LH + WH)` plus the minimum between LW, LH and WH to the total. 

Final formula: `2LW + 2LH + 2WH + min(LW, LH, WH)`.

### Part Two

For part 2, we need to add the volume (i.e. `LWH`) as well as the smallest perimeter of any one face. 

Instead of finding the smallest perimeter (which amounts to finding the smallest two values between L, W and H), we can add all the perimeters (i.e. `2L + 2W + 2H`) and subtract the largest side twice. 

Final formula: `LWH + 2(L + W + H) - 2(max(L, W, H))`.

## [Day 3: Perfectly Spherical Houses in a Vacuum](https://adventofcode.com/2015/day/3)

### Part One

For this challenge I have created a `UniqueLocations` class that keeps track of the unique locations visited. 

Internally it is a dictionary of dictionaries, which makes it very efficient (O(1)) to check if a location has been visited before.

After that, it is just a matter of looping through the instructions and adding each location to the `UniqueLocations` object.

The `total` property of `UniqueLocations` returns the number of unique locations visited.

### Part Two

Part 2 is very similar, except that we have two sets of positions that we alternate between instructions.

## [Day 4: The Ideal Stocking Stuffer](https://adventofcode.com/2015/day/4)

### Part One

I solved this challenge by brute force alone. Simply increment the number until the md5 hash starts with 5 zeros.
I currently used the md5 algorithm from the `hashlib` library, but I might try to implement it myself later.

To speed the computation up, I used the `multiprocessing` library to run the md5 algorithm in parallel.

### Part Two

Part 2 uses the exact same code from Part 1, but for 6 zeros, so it takes longer.

## [Day 5: Doesn't He Have Intern-Elves For This?](https://adventofcode.com/2015/day/5)

### Part One

I used regex to find the patterns in the strings. The only difficulty was matching the repeating letters. But the re library allows to match any previously found group with the `\1` syntax. To avoid any lookahead or lookbehind, I simply used three separate patterns.

### Part Two

For Part 2 I again made use of the `\1` syntax for the two patterns necessary. 

## [Day 6: Probably a Fire Hazard](https://adventofcode.com/2015/day/6)

### Part One

My first implementation is very naive. I crate a 1000x1000 grid of True/False and I loop through the instructions, toggling the lights on or off. The parsing of the instructions is done with regex.

### Part Two

I copied the code from Part 1 and replaced the True/False with integers while making sure to not go below zero.

## [Day 7: Some Assembly Required](https://adventofcode.com/2015/day/7)

### Part One

### Part Two

## [Day 8: Matchsticks](https://adventofcode.com/2015/day/8)

### Part One

### Part Two

## [Day 9: All in a Single Night](https://adventofcode.com/2015/day/9)

### Part One

### Part Two

## [Day 10: Elves Look, Elves Say](https://adventofcode.com/2015/day/10)

### Part One

### Part Two