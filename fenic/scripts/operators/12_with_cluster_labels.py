from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_with_cluster_labels")

df = session.create_dataframe(
    [
        {"id": 1, "text": "Password reset email never arrived."},
        {"id": 2, "text": "SSO login redirects forever."},
        {"id": 3, "text": "CSV export from dashboard is slow."},
        {"id": 4, "text": "Report download times out."},
    ]
)

result = df.semantic.with_cluster_labels(
    by=fc.semantic.embed("text"),
    num_clusters=2,
    label_column="cluster",
)

result.order_by(["cluster", "id"]).show()
