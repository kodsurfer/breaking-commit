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

def is_broken(commit_number):
  return commit_number == 5

n = 10
res = find_break(n, is_broken)
print(f"first breaking commit: {res}")
