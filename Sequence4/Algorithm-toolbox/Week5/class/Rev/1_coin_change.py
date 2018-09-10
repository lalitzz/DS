import sys 


"""
All combination of coins
"""
def get_change_rec(n):
  if n == 0:
    return n
  min_coins = float('inf')
  changes = [1, 3, 4]
  for c in changes:
    if n >= c:
      num_coins = get_change_rec(n - c) 
    if num_coins + 1 < min_coins:
      min_coins = num_coins + 1
  return min_coins

def get_change_memo(n):
  if n == 0:
    return 0
  changes = [1, 3, 4]
  cols = m + 1
  rows = len(changes)
  memo = [[0 if j == 0 else float('inf') for j in range(cols)] for i in range(rows)]
  for i in range(rows):
    for j in range(cols):
      if changes[i] > j:
        memo[i][j] = memo[i - 1][j]
      else:
        memo[i][j] = min(memo[i-1][j], 1 + memo[i][j - changes[i]])
  print(memo)
  return memo[rows-1][cols-1]


def get_change(m):
  changes = [1, 3, 4]
  d = []
  all_changes = []
  _get_changes(m, changes, 0, d, all_changes)
  print(all_changes)
  
def _get_changes(m, changes, n, d, all_changes):
  if m == 0:
    for coin in d:
      print(coin, end = " ")
    all_changes.append(d[:])
    print("")
  
  for i in range(n, len(changes)):
    if m >= changes[i]:
      d.append(changes[i])
      _get_changes(m - changes[i], changes, i, d, all_changes)
      d.pop()

def get_all_change(m):
  changes = [1, 3, 4]
  cols = m + 1
  rows = len(changes)
  memo = [[0 if j == 0 else float('inf') for j in range(cols)] for i in range(rows)]
  for i in range(rows):
    for j in range(1, cols):
      if changes[i] > j:
        memo[i][j] = memo[i - 1][j]
      else:
        memo[i][j] = min(memo[i - 1][j], 1 + memo[i][j - changes[i]])
  print(memo)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change_memo(m))