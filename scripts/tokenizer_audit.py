"""Lab 1 starter: tokenizer audit."""
from pathlib import Path
import pandas as pd
from transformers import AutoTokenizer

CANDIDATES = {
    "bert-base-multilingual-cased": "mBERT (WordPiece, 104 langs)",
    "xlm-roberta-base": "XLM-R (SentencePiece, 100 langs)",
    "CAMeL-Lab/bert-base-arabic-camelbert-mix": "CAMeLBERT (Arabic-centric)",
    "distilbert-base-uncased": "DistilBERT (English-only — the trap)",
}


def fertility(tokenizer, texts):
    # TODO(Lab 1): total subword pieces / total whitespace words.
    raise NotImplementedError


def main():
    corpus = pd.read_csv(Path("data/raw/bayan_feedback.csv"))
    print(f"Loaded {len(corpus):,} Bayan rows")
    # TODO: audit candidates by language and record evidence in BENCHMARKS.md / DECISIONS.md.


if __name__ == "__main__":
    main()
