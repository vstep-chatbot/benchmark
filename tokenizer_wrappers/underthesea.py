from underthesea import chunk


class Underthesea_tokenize:

  def tokenize(self, text):
    output = []
    ners = chunk(text)
    for item in ners:
      output.append([item[0], item[1], ""])
    return output

  def info(self):
    return "Underthesea"
