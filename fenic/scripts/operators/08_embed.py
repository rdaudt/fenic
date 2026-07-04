from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_embed")

df = session.create_dataframe(
    [
        {"id": 1, "text": "Reset a forgotten password."},
        {"id": 2, "text": "Export dashboard data as CSV."},
    ]
)

result = df.select("id", "text", fc.semantic.embed("text").alias("embedding"))

result.show()
