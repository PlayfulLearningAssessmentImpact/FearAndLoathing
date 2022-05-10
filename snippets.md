TODO do this, but for multiple codes at a time. we want to 1000ish rows we code through prodigy to help us toward each code, and not to have to go through this process like 12 times

This downloads a pretrained spacy model:

```sh
python3 -m spacy download en_core_web_lg
```

Alternatively, you can use `blank:en` in the command line commands below. But, maybe that isn't a good idea. I don't actually know.

Starter keywords go in `patterns.jsonl`, and `python preprocess.py` will split the dataset up for us for base rate inflation.

This uses active machine learning to show you smart things to annotate. This does not train a model, just collects annotations, which it then sends to prodi.gy's local database. We'll use the `en_core_web_lg` model as the starting point, since it has the tokenizer, lemmatizer, etc. that we want. We'll use the `shuf-ai.csv` (or whatever) for the dataset, since it has been base rate inflated.

```sh
python3 -m prodigy textcat.teach textcat_ai_2 en_core_web_lg shuf-ai.csv --label AI --patterns patterns.jsonl
```

To export that:

```py
from prodigy.components.db import connect
from json import dumps

db = connect()
with open("hand_coded/ai_export.json", "w") as f:
    data = db.get_dataset("textcat_ai_2")
    f.write(dumps(data))
```

To import that:

```sh
python3 -m prodigy db-in textcat_ai_2 hand_coded/ai_export.json
```

Then this trains a model, using the annotations already in the database. This is fully automated.

```sh
python3 -m prodigy train model_ai_2 --base-model en_core_web_lg --textcat-multilabel textcat_ai_2
```

If it looks like we need to do another round of annotations, we can use the model we just made (`model_ai_2` or whatever) and the full shuffled dataset (`shuf.csv`).

```sh
python3 -m prodigy textcat.teach textcat_ai_2 model_ai_2/model-best shuf.csv --label AI --patterns patterns.jsonl
```

Then we train it some more.

```sh
python3 -m prodigy train model_ai_2 --base-model model_ai_2/model-best --textcat-multilabel textcat_ai_2
```

Once we're happy with it, we run `python3 postprocess.py` to automate coding on the original dataset