# Bayan target architecture

```text
Citizen text over HTTP
        |
        v
Validation -> versioned preprocessing
                    |
          +---------+---------+
          |         |         |
          v         v         v
   topic/sentiment  NER   embeddings -> FAISS -> re-rank
          |         |                 |
          +---- case fields       similar cases
```

Offline training/evaluation produces versioned artifacts consumed by serving. Training, evaluation,
and serving must import the same preprocessing contract.
