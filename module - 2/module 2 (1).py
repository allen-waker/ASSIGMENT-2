def myfun():
  l1 = ['a','i','o','u','e']

  ch = input("Enter character : ").lower()
  if ch in l1:
    print("vowel")
  else:
    print("invalid vowel")
    myfun()