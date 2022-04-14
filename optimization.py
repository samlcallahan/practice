# my original solution - best for usable variable names
def getUniqueCharacter0(s):
    is_unique = {}
    for char in s:
        if char not in is_unique:
            is_unique[char] = True
        elif is_unique[char]:
            is_unique[char] = False
    for char in is_unique:
        if is_unique[char]:
            return s.find(char) + 1
    return -1

# supposedly optimal solution (takes about 4x as long as other solutions)
def getUniqueCharacter1(s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq.update({i:1})
    for i in range(0, len(s)):
        if freq[s[i]] == 1:
            return i + 1
    return -1

# 
def getUniqueCharacter2(s):
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = True
        elif freq[i]:
            freq[i] = False
    for i in freq:
        if freq[i]:
            return s.find(i) + 1
    return -1

# 
def getUniqueCharacter3(s):
    freq= {}
    for i in s:
        if i in freq:
            freq[i] = False
        else:
            freq[i] = True
    for i in freq:
        if freq[i]:
            return s.find(i) + 1
    return -1 

#
def getUniqueCharacter4(s):
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = True
        else:
            freq[i] = False
    for i in freq:
        if freq[i]:
            return s.find(i) + 1
    return -1

def getUniqueCharacter5(s):
    freq = {}
    for i in s:
        if freq.get(i):
            freq[i] = False
        elif i not in freq:
            freq[i] = True
    for i in freq:
        if freq[i]:
            return s.find(i) + 1
    return -1 
        

# benchmark comparisons: https://docs.google.com/spreadsheets/d/1InbgWDroQV2J-3u-Fy5CutP6NQuE4zquMeLUXi41Qh4/edit?usp=sharing

test_strings = ['a', 'falafal', 'hackthegame', 'abcdefghijklmnopqrstuvwxyz', 'a' * 9999 + 'z', 'abcdefghijklmnopqrstuvwxy' * 399 + 'abcdefghijklmnopqrstuvwxz', 'a' * 26]

def getUniqueCharacter6(s):
    freq = {}
    for i in s:
        if i in freq:
            if freq[i]:
                freq[i] = False
        else:
            freq[i] = True
    for i in freq:
        if freq[i]:
            return s.find(i) + 1
    return -1 

def funWithAnagrams0(text):
    unique_char_counts = []
    not_anagrams = []
    for word in text:
        char_counts = {}
        for char in word:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        if char_counts not in unique_char_counts:
            not_anagrams.append(word)
            unique_char_counts.append(char_counts)
    return sorted(not_anagrams)

def funWithAnagrams1(text):
    cs = set()
    ans = []
    for t in text:
        tt = tuple(sorted(list(t)))
        if tt not in cs:
            ans.append(t)
            cs.add(tt)
    return sorted(ans)

def funWithAnagrams2(text):
    cs = set()
    ans = []
    for t in text:
        cc = {}
        for c in t:
            if c in cc:
                cc[c] += 1
            else:
                cc[c] = 1
        cc = frozenset(cc.items())
        if cc not in cs:
            ans.append(t)
            cs.add(cc)
    return sorted(ans)

text_tests = [["code","aaagmnrs","anagrams","doce"], ["poke","pkoe","okpe","ekop"]]
anagram_funcs = [funWithAnagrams0, funWithAnagrams1, funWithAnagrams2]

import string
import random

letters = string.ascii_lowercase

new_test = []
for k in range(10):
    text = []
    for i in range(random.randrange(1,1001)):
        word_length = random.randrange(1,1001)
        word = ''
        for j in range(word_length):
            word += random.choice(letters)
        text.append(word)
    new_test.append(text)

for i in anagram_funcs:
    print(i)
    for x, j in enumerate(new_test):
        print(x)
        for k in range(10):
            %timeit i(j)

largest = []
for i in range(1000):
    word = ''
    for j in range(1000):
        word += random.choice(letters)
    largest.append(word)