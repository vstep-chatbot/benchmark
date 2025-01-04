from vncorenlp import VnCoreNLP

class VncoreNLP_tokenize:

  # To perform word segmentation, POS tagging, NER and then dependency parsing
  # annotator = VnCoreNLP("VnCoreNLP-1.1.1.jar", annotators="wseg,pos,ner,parse", max_heap_size='-Xmx2g')
  def __init__(self):
    self.annotator = VnCoreNLP("tokenizers/VnCoreNLP-1.2.jar", annotators="wseg,pos,ner,parse", max_heap_size='-Xmx2g')

  def tokenize(self,text):
    output = []
    annotated_text = self.annotator.annotate(text)
    for sent in annotated_text['sentences']:
        for item in sent:
          output.append([item['form'].replace('_',' '),item['posTag'],item['nerLabel']])
    return output

  def close(self):
    self.annotator.close()
  def info(self):
    return('VnCoreNLP')
