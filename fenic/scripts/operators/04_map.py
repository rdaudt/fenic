from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_map")

df = session.create_dataframe(
    [
        {
            "id": 1,
            "text": (
                "I am trying to import a CSV with about 15,000 customer rows. "
                "The upload finishes, but then the import button disappears and the page never "
                "shows whether the import succeeded or failed. I have retried three times and "
                "now I am worried we may have created duplicate records."
            ),
        },
        {
            "id": 2,
            "text": (
                "Our finance team exports invoices from the billing page every Friday. "
                "The PDF includes the invoice number and customer name, but it does not include "
                "the purchase order number that our accounting system requires. We have to add "
                "that number by hand before sending invoices to customers."
            ),
        },
    ]
)

result = df.select(
    "id",
    fc.semantic.map(
        "Rewrite this customer note as a concise support ticket title: {{ text }}",
        text=fc.col("text"),
    ).alias("ticket_title"),
)

result.show()
