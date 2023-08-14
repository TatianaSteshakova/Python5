word = input("Введите слово: ")
word = word.lower()
word_set = set(word)
vowels = set("aeiou")

a_count = word.count('a')
e_count = word.count('e')
i_count = word.count('i')
o_count = word.count('o')
u_count = word.count('u')

consonants_cnt = len(word_set.difference(vowels))

if (a_count + e_count + i_count + o_count + u_count == 0):
    print("False")
else:
    print("Согласных: ", consonants_cnt)
    print ("Гласных:")
    print ("a = ", a_count)
    print ("e = ", e_count)
    print ("i = ", i_count)
    print ("o = ", o_count)
    print ("u = ", u_count)
