class Spacy_tokenize:
  def __init__(self):
    import spacy
    self.nlp = spacy.load('vi_core_news_lg')

  def tokenize(self, text):
    output = []
    doc = self.nlp(text)
    for token in doc:
      output.append([token.text, token.tag_, ''])
      #print(token.text, token.lemma_, token.tag_, token.pos_, token.dep_,
      #        token.shape_, token.is_alpha, token.is_stop)
    return output

  def info(self):
    return 'PyVi'

  def close(self):
    pass
