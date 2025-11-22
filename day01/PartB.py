from partA import parse_input


def build_counts(nums):
  """
  Build a dictionary mapping each number in the given list its frequency within the list.
  Ex. [1, 2, 3, 3, 2, 5] becomes {1: 1, 2: 2, 3: 2, 5: 1}
  """
  counts_dict = {}
  for n in nums:
    if n in counts_dict:
      counts_dict[n] += 1
    else:
      counts_dict[n] = 1
  return counts_dict

def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    lines = f.readlines()
  
  list_a, list_b = parse_input(lines)

  counts_a = build_counts(list_a)
  counts_b = build_counts(list_b)

  # Each number in the first list adds its value multiplied by its frequency in the second list to the score
  # Since it does this each time it occurs in the first list, we multiply this by its frequency in the first list too and only add once
  score = 0
  for num, freq_a in counts_a.items():
    score += num * freq_a * counts_b.get(num, 0)
  
  print(f"Score: {score}")


if __name__ == "__main__":
  main()