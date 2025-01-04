from underthesea import chunk

class Underthesea_tokenize:

  def __init__(self):
    pass
  def tokenize(self,text):
    output = []
    ners = chunk(text)
    for item in ners:
      output.append([item[0],item[1],item[3]])
    return output

  def info(self):
    return('Underthesea')

  def close(self):
    pass
