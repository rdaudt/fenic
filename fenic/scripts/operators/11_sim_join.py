from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_sim_join")

queries = session.create_dataframe(
    [
        {"query_id": 1, "query": "How do I reset my password?"},
        {"query_id": 2, "query": "Can I download report data as CSV?"},
    ]
)

docs = session.create_dataframe(
    [
        {"doc_id": "auth", "title": "Account access and password recovery"},
        {"doc_id": "reports", "title": "Exporting analytics reports"},
    ]
)

result = queries.semantic.sim_join(
    docs,
    left_on=fc.semantic.embed("query"),
    right_on=fc.semantic.embed("title"),
    k=1,
    similarity_score_column="score",
)

result.show()
