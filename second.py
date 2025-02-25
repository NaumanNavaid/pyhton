sentence=(input("Enter a sentence:"))
word_count=len(sentence.split())
reversed_sentence = " ".join(sentence.split()[::-1])
print(f"The number of words in the sentence is: {word_count}")
print(f"The reversed sentence is: {reversed_sentence}")

