

T = int(raw_input())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def clean(value):
    if value < 0:
        return value + 26
    return value


def decipher(word):
    if len(word) == 2:
        return word[1] + word[0]
    elif len(word) == 3:
        return "AMBIGUOUS"

    n = len(word)
    result = [-1] * n

    # We will always know these two letters
    result[1] = alphabet.index(word[0])
    result[-2] = alphabet.index(word[-1])
    decrypted_count = 2

    still_possible = True
    while decrypted_count < n and still_possible:
        still_possible = False
        for i in xrange(1, n-1):
            if result[i-1] > -1 and result[i+1] > -1:  # We know both values already
                continue
            elif result[i-1] == -1 and result[i+1] == -1:  # We don't know either so can't do much
                continue
            else:  # Now we have something to work with
                still_possible = True
                decrypted_count += 1
                value = alphabet.index(word[i])
                if result[i - 1] == -1:
                    result[i - 1] = clean(value - result[i + 1])
                else:
                    result[i + 1] = clean(value - result[i - 1])
            if decrypted_count == n:
                break
        if not still_possible:
            return "AMBIGUOUS"
    original = ""
    for i in result:
        if i == -1:
            original += " "
        else:
            original += alphabet[i]
    return original


for case in xrange(1, T + 1):
    print "Case #{}: {}".format(case, decipher(raw_input()))