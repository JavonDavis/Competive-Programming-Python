
vowel_set = ['a', 'e', 'i', 'o', 'u', 'y']

w = raw_input().strip()
is_beautiful = "Yes"
for i in xrange(len(w) - 1):
    if w[i] == w[i+1]:
        is_beautiful = "No"
        break
    elif w[i] in vowel_set and w[i+1] in vowel_set:
        is_beautiful = "No"
        break
print is_beautiful.strip()
