def longest_consec(strarr, k):
  current_longest = ""
  for x in range(0, len(strarr) - k + 1):
    possible_str = ""
    for y in range(x, x+k):
      possible_str += strarr[y]

    if len(possible_str) > len(current_longest):
      current_longest = possible_str
  return current_longest
