from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_classify")

df = session.create_dataframe(
    [
        {"id": 1, "text": "Password reset fails after I enter the SMS code."},
        {"id": 2, "text": "Please add CSV export to the analytics dashboard."},
        {"id": 3, "text": "The checkout page returns a 500 error."},
    ]
)

result = df.select(
    "id",
    "text",
    fc.semantic.classify("text", ["bug", "feature_request", "account_help"]).alias("category"),
)

result.show()
