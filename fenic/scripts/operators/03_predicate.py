from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_predicate")

df = session.create_dataframe(
    [
        {"id": 1, "text": "The app crashes when I upload a 200 MB PDF."},
        {"id": 2, "text": "I love the cleaner billing page."},
        {"id": 3, "text": "Dark mode would be nice on mobile."},
    ]
)

result = df.filter(
    fc.semantic.predicate(
        "{{ text }} describes a product defect or broken behavior.",
        text=fc.col("text"),
    )
)

result.show()
