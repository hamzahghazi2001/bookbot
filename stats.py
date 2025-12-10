def word_count(content):
  my_list = content.split()
  count =0 
  for i in my_list:
    count = count + 1
  print(f"Found {count} total words ")

def char_count(content):
    char_counts = {}

    for ch in content.lower():   # LOOP DIRECTLY OVER CHARACTERS
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1
    return char_counts

def sort_on(items):
    return items["num"]

# def formating(items):
#     for i in items:
#         print(f"{i}:{items[i]}\n")