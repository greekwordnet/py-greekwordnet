Greek WordNet 2.0 API
=====================

This module provides a light-weight wrapper for the Greek WordNet 2.0 API.

Basic Usage
-----------

```
>>> from greekwordnet import GreekWordNet
>>> LWN = GreekWordNet()
>>> for lemma in LWN.index():
...     print(lemma['lemma'], lemma['pos'], lemma['morpho'])
>>> uirtus = LWN.lemmas(lemma='uirtus', pos='n').get()
[{'lemma': 'uirtus', 'pos': 'n', 'morpho': 'n-s---fn3-', 'uri': '28157', 'pronunciation': '[ˈwɪr.tuːs]', 'principal_parts': 'uirtut', 'irregular_forms': '', 'alternative_forms': ''}]
>>> dicere = LWN.lemmas(lemma='dico', pos='v', morpho='v1spia--3-').get()
>>> synsets = LWN.lemmas(lemma='dico', morpho='v1spia--1-').synsets
>>> LWN.lemmas(lemma='femina', pos='n').relations)[0]['relations']
{'related-to': [{'lemma': 'femellarius', 'morpho': 'n-s---mn2-', 'uri': 'f0342'}, {'lemma': 'femella', 'morpho': 'n-s---fn1-', 'uri': 'f0341'}, {'lemma': 'femino', 'morpho': 'v1spia--1-', 'uri': 'f0348'}, {'lemma': 'feminatus', 'morpho': 'aps---mn1-', 'uri': '110520'}, {'lemma': 'femineus', 'morpho': 'aps---mn1-', 'uri': 'f0345'}, {'lemma': 'femininus', 'morpho': 'aps---mn1-', 'uri': 'f0346'}, {'lemma': 'feminine', 'morpho': 'rp--------', 'uri': '110522'}]}
>>> LWN.synsets(pos='n', offset='03316977').get()
{'pos': 'n', 'offset': '03316977', 'gloss': 'a protective structure or device (usually metal)', 'semfield': []}
>>> LWN.synsets(pos='n', offset='03316977').lemmas
[{'lemma': 'aegis', 'morpho': 'n-s---fn3-', 'uri': 'a0870'}, {'lemma': 'integumentum', 'morpho': 'n-s---nn2-', 'uri': 'i2222'}, {'lemma': 'scutum', 'morpho': 'n-s---nn2-', 'uri': 's0833'}, {'lemma': 'clipeus', 'morpho': 'n-s---mn2-', 'uri': 'c2123'} . . . ]
>>> for lemmed in LWN.lemmatize('virtutem'):
...     print(lemmed)
{'lemma': {'lemma': 'uirtus', 'morpho': 'n-s---fn3-', 'uri': '28157'}, 'morpho': ['n-s---fa3-']}
>>> for translated in LWN.translate('en', 'dagger', 'n'):
...     print(translated)
[{"lemma": "pugio", "morpho": "n-s---mn3-", "prosody": "pugio", "uri": "p4420"}, {"lemma": "sicula", "morpho": "n-s---fn1-", "prosody": "sicula", "uri": "s1585"}, {"lemma": "gladiolus", "morpho": "n-s---mn2-", "prosody": "gladiolus", "uri": "g0330"}]
```
