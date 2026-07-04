from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_analyze_sentiment")

df = session.create_dataframe(
    [
        {"id": 1, "text": "The new dashboard is beautiful and very fast."},
        {"id": 2, "text": "The export job failed again and blocked my report."},
        {"id": 3, "text": "I opened the account settings page."},
    ]
)

result = df.select(
    "id",
    "text",
    fc.semantic.analyze_sentiment("text").alias("sentiment"),
)

result.show()
