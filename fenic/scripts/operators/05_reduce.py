from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_reduce")

df = session.create_dataframe(
    [
        {"area": "billing", "note": "Invoice download is slow for enterprise accounts."},
        {"area": "billing", "note": "Customers want purchase order numbers on invoices."},
        {"area": "auth", "note": "SSO login fails on the mobile browser."},
        {"area": "auth", "note": "Password reset emails sometimes arrive late."},
    ]
)

result = df.group_by("area").agg(
    fc.semantic.reduce(
        "Summarize the common customer theme in one sentence.",
        column=fc.col("note"),
    ).alias("theme")
)

result.show()
