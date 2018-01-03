from nltk.tag import DefaultTagger
from nltk.corpus import brown
from nltk.tag import RegexpTagger
from nltk.tag import UnigramTagger

default_tagger = DefaultTagger("NN")
print(list(default_tagger.tag('This is a test'.split())))

regexp_tagger = RegexpTagger(
     [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
      (r'(The|the|A|a|An|an)$', 'AT'),   # articles
      (r'.*able$', 'JJ'),                # adjectives
      (r'.*ness$', 'NN'),                # nouns formed from adjectives
      (r'.*ly$', 'RB'),                  # adverbs
      (r'.*s$', 'NNS'),                  # plural nouns
      (r'.*ing$', 'VBG'),                # gerunds
      (r'(.*ed|said)$', 'VBD'),                 # past tense verbs
      (r'.*', 'NN')                      # nouns (default)
])
print(regexp_tagger)
test_sent = brown.sents(categories='news')[0]
print(test_sent)
print(regexp_tagger.tag(test_sent))

unigram_tagger = UnigramTagger(brown.tagged_sents(categories='news')[:500])
for tok, tag in unigram_tagger.tag(test_sent):
    print("(%s, %s), " % (tok, tag))