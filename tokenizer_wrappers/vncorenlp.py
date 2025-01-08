from py_vncorenlp import VnCoreNLP, download_model


class VncoreNLP_tokenize:
  # To perform word segmentation, POS tagging, NER and then dependency parsing
  # annotator = VnCoreNLP("VnCoreNLP-1.1.1.jar", annotators="wseg,pos,ner,parse", max_heap_size='-Xmx2g')
  def __init__(self):
    download_model()
    self.annotator = VnCoreNLP(annotators=["wseg", "pos", "parse"])

  def tokenize(self, text):
    output = []
    annotated_text = self.annotator.annotate_text(text)
    for token in annotated_text[0]:
      output.append([token["wordForm"].replace("_", " "), token["posTag"], ""])
    return output

  def close(self):
    pass

  def info(self):
    return "VnCoreNLP"
