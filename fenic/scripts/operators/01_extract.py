from __future__ import annotations

from pydantic import BaseModel, Field

import fenic as fc
from common import get_session


class Ticket(BaseModel):
    product: str = Field(description="Product or feature area mentioned by the user")
    sentiment: str = Field(description="positive, neutral, or negative")
    issue: str = Field(description="Short description of the issue or praise")


session = get_session("fenic_operator_extract")

df = session.create_dataframe(
    [
        {"id": 1, "text": "The CSV export in Reports times out every morning."},
        {"id": 2, "text": "The new dashboard is fast and much easier to read."},
    ]
)

result = df.select("id", fc.semantic.extract("text", Ticket).alias("ticket")).unnest("ticket")

result.show()
