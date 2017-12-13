def count_words(string):
  word_counts = {}
  for word in string.split(' '):
    if word not in word_counts:
      word_counts[word] = 0
    word_counts[word] += 1
  return word_counts