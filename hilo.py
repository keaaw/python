# HILO, a simple number guessing game where the computer is doing the guessing
#

from math import log2

lo = None
hi = None
ready_to_play = False


# get either the low or high extent of the guessing range
# str is the name of the extent, either "hi" or "lo"
# enforces the game rules of the extent must be a non-negative integer (numeric) value
#
def get_game_extent(s):
    while True:
        input_str = input(f"{s}: ")
        try:
            input_num = int(input_str)
        except ValueError:
            print(f"{s} must be an integer")
            continue
        if input_num < 0:
            print(f"{s} must be non-negative")
            continue
        return input_num


# get the extents of the game from the user, keep asking
# until we get good answers for both
# enforces the rule that low <= high
#
while True:
    print("Enter the low and high range of the game")
    lo = get_game_extent("lo")
    hi = get_game_extent("hi")
    if lo > hi:
        print("low must be less than or equal to high")
        continue
    break


# given an input string, returns a new string with added terminal escape codes that
# when printed, displays the intput string underlined
#
def underline(s):
    return "\033[4m" + s + "\033[0m"


n_guesses = 0
print(f"I should be able to guess the number in about {int(log2(hi - lo + 1))} guesses")

# string format template for the main game loop's prompt
prompt = "Guess #{num_guesses}: {guess}? ("
prompt += underline('h') + "igher, "
prompt += underline('l') + "ower, "
prompt += underline('c') + "orrect): "

got_it = False

# main game loop: keep going until either the user indicates that
# the computer has guessed correctly, or until the computer determines
# that the user is cheating and has not answered correctly!
#
while lo <= hi and not got_it:
    n_guesses += 1
    g = (lo + hi) // 2
    good_response = False
    ans = None
    while not good_response:
        ans = input(prompt.format(num_guesses=n_guesses, guess=g))
        good_response = ans[0] in ['h', 'l', 'c']
        if not good_response:
            print("I didn't understand that answer")
    if ans[0] == 'c':
        got_it = True
    elif ans[0] == 'l':
        hi = g - 1
    else:
        lo = g + 1
if got_it:
    print("yay!")
else:
    print("I quit, you're cheating!")
