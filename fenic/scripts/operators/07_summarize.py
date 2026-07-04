from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_summarize")

df = session.create_dataframe(
    [
        {
            "id": 1,
            "text": (
                "A finance manager at a regional retailer is preparing for the quarterly "
                "business review and needs to export revenue, refund, and discount data from "
                "the analytics dashboard. The export job starts normally and shows progress "
                "for several minutes, but it fails with a timeout after processing roughly "
                "eighty percent of the rows. The customer has tried the export in Chrome and "
                "Edge, reduced the date range from a full quarter to one month, and removed "
                "several optional columns, but the job still fails. Smaller exports for a "
                "single store work correctly, which suggests the issue is related to data "
                "volume rather than permissions or browser settings. The customer needs the "
                "CSV before an executive meeting tomorrow morning and is currently copying "
                "figures by hand from dashboard cards into a spreadsheet. They are asking for "
                "either a workaround, a backend export, or confirmation that engineering can "
                "increase the timeout for large report downloads."
            ),
        }
    ]
)

result = df.select("id", fc.semantic.summarize("text").alias("summary"))

result.show()
