def parse_input(lines):
  """
  Each line of input is a sequence of space-separated ints.
  Returns a list of lists, with each inner list containing one line of input, stripped and cast to ints
  """
  parsed = []
  for line in lines:
    ints = [int(x) for x in line.split()]
    parsed.append(ints)
  # print(parsed[:50])
  return parsed

def is_safe(report) -> bool:
  """
  Returns whether a given report is 'safe'
  To be safe a report must satisfy both:
  - Be strongly monotone - either always increasing or always decreasing, but never contstant and never mixed
  - Have a consecutive pairwise difference between 1 and 3, inclusive
  """

  # Calculate the signed difference between each consecutive pair
  diffs = []
  for i in range(1, len(report)):
    diffs.append(report[i] - report[i-1])
  
  # All greater than 0 (increasing) or less than 0 (decreasing)
  is_monotone = all(n > 0 for n in diffs) or all(n < 0 for n in diffs)
  # All (absolute) differences between 1 and 3
  is_gradual = all(1 <= abs(n) <= 3 for n in diffs)

  # Safe only if both conditions satisfied
  return is_monotone and is_gradual

def main():
  in_file = "data.txt"
  with open(in_file, 'r') as f:
    lines = f.readlines()
  
  reports = parse_input(lines)

  safe_reports = [r for r in reports if is_safe(r)]
  score = len(safe_reports)

  print(f"Score: {score}")

if __name__ == "__main__":
  main()