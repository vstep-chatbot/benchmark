# Format for data [sentence, [[word, entity], [word, entity],...]]
from tokenizers.spacy import Spacy_tokenize
from tokenizers.underthesea import Underthesea_tokenize
from tokenizers.vncorenlp import VncoreNLP_tokenize
from time import time as timer

from conllu import parse

with open ('UD_Vietnamese-VTB/vi_vtb-ud-test.conllu', 'r', encoding='utf-8') as f:
  text = f.read()

sentences = parse(text)

text = ''
sents : list[str] = []
groundtruth = []
for tokenlist in sentences:
  tagged = []
  sent = tokenlist.metadata['text']
  for item in tokenlist:
    #print(item['form'],item['xpos'])
    tagged.append([item['form'],item['xpos'],' '])
  text += sent + ' '
  groundtruth.append(tagged)
  sents.append(sent)

for t in [Underthesea_tokenize]:
  t = t()
  count = 0
  wordcount = 0
  poscount = 0
  sercount = 0


  time = 0
  index = 0

  for sent in sents:
    start = timer()
    predict = t.tokenize(sent)
    time += timer() - start
    count += len(groundtruth[index])

    # 'Predict: ',predict,'Ground-truth: ', groundtruth[index]
    if len(predict) == len(groundtruth[index]):
        for item,gt in zip(predict,groundtruth[index]):  # item = [word, pos, entity]
          if item[0] == gt[0]:
            wordcount += 1
          if item[1] == gt[1]:
            poscount += 1
          if item[2] == gt[2]:
            sercount += 1
    index += 1

  # Corrected segmented word and entity / total word count
  wordsegacc = wordcount/count
  posacc = poscount/count
  seracc = sercount/count

  print()
  print(t.info())
  print('Tagging time: ',time,' Accuracy: Word segmentation ',wordsegacc,' Pos tag ',posacc,' Entity recognition ',seracc)


  t.close()
