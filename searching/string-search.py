import timeit

# yo check this out, you can use rolling hashes to make this way faster:
# https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

def string_search(substr, str):
  sub_len = len(substr)

  idx = 0
  lp = 0
  substart = None # first char in substring

  len_str = len(str)
  while idx < len_str - (sub_len - lp):
    if str[idx] == substr[lp]:
      if lp == sub_len - 1:
        return idx - lp
      if lp > 0 and substr[0] == str[idx]:
        substart = idx
      lp += 1
    else:
      if substart is not None:
        idx = substart - 1
        substart = None
      #   in_substr = False
      lp = 0
    idx += 1

  return -1

def indexOf(needle, haystack):
  for h_idx in range(len(haystack) - len(needle)):
    for n_idx in range(len(needle)):
      if haystack[h_idx + n_idx] != needle[n_idx]:
        break
      if n_idx + 1 == len(needle):
        return h_idx

  return -1

start = timeit.default_timer()
print(string_search('or', 'hello world'), 'should equal 7') # should return 7
print(string_search('hello world', 'or'), 'should equal -1') # should return -1
print(string_search('howdy', 'hello world'), 'should equal -1') # should return -1
print(string_search('oox', 'ooboxoooxo'), 'should equal 6') # should return 6)
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
print(indexOf('or', 'hello world'), 'should equal 7') # should return 7
print(indexOf('hello world', 'or'), 'should equal -1') # should return -1
print(indexOf('howdy', 'hello world'), 'should equal -1') # should return -1
print(indexOf('oox', 'ooboxoooxo'), 'should equal 6') # should return 6)
stop = timeit.default_timer()
print('Time: ', stop - start)
