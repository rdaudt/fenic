from __future__ import annotations

import fenic as fc


def get_session(app_name: str) -> fc.Session:
    config = fc.SessionConfig(
        app_name=app_name,
        semantic=fc.SemanticConfig(
            language_models={
                "mini": fc.OpenAILanguageModel(
                    model_name="gpt-5.5",
                    rpm=100,
                    tpm=100_000,
                )
            },
            default_language_model="mini",
            embedding_models={
                "small": fc.OpenAIEmbeddingModel(
                    model_name="text-embedding-3-small",
                    rpm=100,
                    tpm=100_000,
                )
            },
            default_embedding_model="small",
        ),
    )
    return fc.Session.get_or_create(config)
