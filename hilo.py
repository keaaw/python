from math import log2

lo = None
hi = None
ready_to_play = False

def get_game_extent(str):
    while True:
        input_str = input(f"{str}: ")
        try:
            input_num = int(input_str)
        except:
            print(f"{str} must be an integer")
            continue
        if input_num < 0:
            print(f"{str} must be non-negative")
            continue
        return input_num

msg = "both low and high must be non-negative integers, low <= high"

while True:
    print("Enter the low and high range of the game")
    lo = get_game_extent("lo")
    hi = get_game_extent("hi")
    if (lo > hi):
        print("low must be less than or equal to high")
        continue
    break

def underline(str):
    return "\033[4m" + str + "\033[0m"

n_guesses = 0
print(f"I should be able to guess the number in about {int(log2((hi - lo + 1)))} guesses")

prompt = "Guess #{num_guesses}: {guess}? ("
prompt += underline('h') + "igher, "
prompt += underline('l') + "ower, "
prompt += underline('c') + "orrect): "

got_it = False

while lo <= hi and not got_it:
    n_guesses += 1
    g = (lo + hi) // 2
    good_response = False
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
