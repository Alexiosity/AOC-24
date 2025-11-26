
from collections import defaultdict

def parse_input(lines):
  order_rules = defaultdict(set)
  sep_line_num = -1
  for i, line in enumerate(lines):
    if len(line) < 3:
      sep_line_num = i
      break
    else:
      pre, post = line.strip().split('|')
      pre = int(pre)
      post = int(post)
      order_rules[pre].add(post)
  
  if sep_line_num == -1: raise ValueError("I don't know where to start looking for page lists")
  
  manuals = []
  for i in range(sep_line_num+1, len(lines)):
    manuals.append(tuple(int(n) for n in lines[i].strip().split(',')))
  
  return order_rules, manuals

def is_valid_manual(rules, manual):
  """
  Return whether the given pages follow the rules about relative order
  """

  for i, page in enumerate(manual):
    if any(manual[j] in rules[page] for j in range(i)): return False
  return True

def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    lines = f.readlines()
  order_rules, manuals = parse_input(lines)

  correct_manuals = [manual for manual in manuals if is_valid_manual(order_rules, manual)]
  middle_pages = [manual[len(manual)//2] for manual in correct_manuals]
  
  score = sum(middle_pages)
  print(f"Score: {score}")


if __name__ == "__main__":
  main()