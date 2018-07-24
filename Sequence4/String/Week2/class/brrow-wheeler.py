def rotation(text):
  n = len(text)
  _text = text * 2
  # print('text', _text)
  result = [_text[i:i + n] for i in range(n)]
  # print('result', result)
  return result

def bwm(text):
  rotated = rotation(text)
  # print(rotated)
  return sorted(rotated)

def bwt_arr(text):
  n = len(text)
  burrow_wheeler_matrix = bwm(text)
  # print(burrow_wheeler_matrix)
  return ''.join([burrow_wheeler_matrix[i][n - 1] for i in range(n)])

if __name__ == '__main__':
  text = 'panamabananas$'
  print(bwt_arr(text))