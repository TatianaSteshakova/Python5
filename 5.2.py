word = input("Введите слово: ")
vowels = set("aeiou")
word_set = set(word.lower())

vowels_cnt = len(word_set.intersection(vowels))
consonants_cnt = len(word_set.difference(vowels))

if (vowels_cnt == 0):
    print("False")
else:
    print("Гласных:", vowels_cnt, "Согласных: ", consonants_cnt)
