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

I was stumped for the longest time on this problem. In the end, I just failed to see that there were two inputs given ('b' and 'c') instead of just one.

The gates are modelized as a list with 4 values: input1, input2, operator and output. The inputs are either a value or a wire identifier. The output is the wire it is connected to.
If a wire is connected directly to another wire, the operator in None.

I create a list with all the gates and a list with the gates whose value can already be calculated (i.e. all the inputs are values). This last list is called next_gates and will be looped over continuously until it is empty or the output wire has been calculated.

I also create a dictionary with the wires as keys and an array of gates they are connected to as values.

For each gate in next_gates, I first check if the gate output can be calculated (i.e. all the inputs are values). If not, I drop the gate from the list and go to the next one.

If the output can be calculated, I loop through the gates that are connected to the output wire and replace the wire identifier with the value of the output. I then add the connected gates to next_gates.

### Part Two

Part 2 is the same as Part 1, but ran twice. For the second run the value of wire 'b' is changed to the value of the wire 'a' from the first run.

## [Day 8: Matchsticks](https://adventofcode.com/2015/day/8)

### Part One
For each line, code length is simply the length of the line with the newline character removed.

For the code value, I first remove the first and last characters (the quotes). I then loop through all the characters. If the character is a backslash, I check the next character. If it is a backslash or a quote, I add 1 to the code value. If it is an 'x', I add 3 to the code value and skip the next three characters.
### Part Two

Part two is easier. The encoded length is the code length plus one per backslash or quote and plus 2 for the quotes.

## [Day 9: All in a Single Night](https://adventofcode.com/2015/day/9)

### Part One
This problem is a traveling salesman problem without return to the first city. To solve it I implemented the Bellman–Held–Karp algorithm. 

My input is a dictionary with the cities as keys and a dictionary with the distances to the other cities as values.

The BHK algorithm is a recursive algorithm which returns the shortest distance from the source city to the target city, while ensuring going through all the cities in a given set. If the answer is not trivial (i.e. the set is not empty), the algorithm will loop through all the cities in the set and return the minimum of the distance from the source to the current city plus the distance from the current city to the target. It does so by recursively calling itself with the current city removed from the set.

The final answer is found by looping through all the cities and all the potential final targets and finding the lowest value.

### Part Two

Part 2 is the same as part 1 but maximizing the distance instead of minimizing it. With my implementation, I simply changed the `min` function to `max`.

## [Day 10: Elves Look, Elves Say](https://adventofcode.com/2015/day/10)

### Part One

To generate the next number in the sequence, I loop through the string. If the next character is identical to the current one, I increment a counter. If the next character is different, I add the counter and the current character to the new string and reset the counter. I do this 40 times.

### Part Two

Part 2 is the same as part 1 but ran 50 times instead of 40.

## [Day 11: Corporate Policy](https://adventofcode.com/2015/day/11)

### Part One

I separated this problem into two functions. The first one gets me the next password and the second one checks if the password is valid.

Getting the next password is done by looping through the string in reverse order and incrementing the character by one. If the character is 'z', I change it to 'a' and continue to the next character. If the character is not 'z', I stop incrementing and return the current character until the end (start) of the string.

The validity check has three conditions found by looping through the password:
1. If the current character is 'i', 'o' or 'l', I return False immediately.
1. If the current character is equal to the previous character, I check if the one pair flag is True. If yes, I set the two pair flag to True. If not, I set the one pair flag to True.
1. If the current character is equal to the previous character plus one and the ongoing straight flag is True, I set the three straight flag to True. If not, I set the ongoing straight flag to True.

Extra caution needs to be taken to avoid overlapping pairs and reset the ongoing straight flag when a straight is lost.

In the end, I return True if both the two pair and three straight flags are True.

### Part Two

Part 2 is the same as part 1, but I keep generating passwords until I find the second valid one.

## [Day 12: JSAbacusFramework.io](https://adventofcode.com/2015/day/12)

### Part One

I looped through the string and every time I found either a digit or a negative sign, I appended the character to a string. When I found a non-digit, I converted the string to an integer and added it to the total.

### Part Two

I couldn't solve part 2 the same way as part 1. I had to use the `json` library to parse the string and recursevily return the sum of all the numbers.

To do that I had three functions: one to return the value of a list, one to return the value of a dictionary and one to return the value of an element. This last function checks if the element is a list or a dictionary and calls the first two functions accordingly. If the element is a number, it simply returns the number. If it is a string, it returns 0.

This solution is the implementation to the part 1 problem. To solve part 2, I simply added a check to the dictionary function to return 0 if the dictionary contains a `red` element.

## [Day 13: Knights of the Dinner Table](https://adventofcode.com/2015/day/13)

### Part One

### Part Two

## [Day 14: Reindeer Olympics](https://adventofcode.com/2015/day/14)

### Part One

### Part Two

## [Day 15: Science for Hungry People](https://adventofcode.com/2015/day/15)

### Part One

### Part Two

## [Day 16: Aunt Sue](https://adventofcode.com/2015/day/16)

### Part One

### Part Two

## [Day 17: No Such Thing as Too Much](https://adventofcode.com/2015/day/17)

### Part One

### Part Two

## [Day 18: Like a GIF For Your Yard](https://adventofcode.com/2015/day/18)

### Part One

### Part Two

## [Day 19: Medicine for Rudolph](https://adventofcode.com/2015/day/19)

### Part One

### Part Two

## [Day 20: Infinite Elves and Infinite Houses](https://adventofcode.com/2015/day/20)

### Part One

### Part Two

## [Day 21: RPG Simulator 20XX](https://adventofcode.com/2015/day/21)

### Part One

### Part Two

## [Day 22: Wizard Simulator 20XX](https://adventofcode.com/2015/day/22)

### Part One

### Part Two

## [Day 23: Opening the Turing Lock](https://adventofcode.com/2015/day/23)

### Part One

### Part Two

## [Day 24: It Hangs in the Balance](https://adventofcode.com/2015/day/24)

### Part One

### Part Two

## [Day 25: Let It Snow](https://adventofcode.com/2015/day/25)

### Part One

### Part Two


