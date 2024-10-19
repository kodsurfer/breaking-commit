def find_break(n, is_broken):
  le = 1
  ri = n

  while le<ri:
    mi = (le+ri)//2
    if is_broken(mi):
      le = mi + 1
    else:
      ri = mi
  return le

def is_broken():
  pass
