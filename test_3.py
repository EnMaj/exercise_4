sentence = input()
sentence_mass = list(sentence.split())
for i in range(len(sentence_mass)):
    if ("," in sentence_mass[i]) or ("." in sentence_mass[i]):
        sentence_mass[i] = sentence_mass[i].replace(",","")
        sentence_mass[i] = sentence_mass[i].replace(".","")
print(sentence_mass)

sentence = input()
sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
sentence_mass = list(sentence.split())
print(sentence_mass)

