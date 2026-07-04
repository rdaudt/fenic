from __future__ import annotations

import fenic as fc
from common import get_session


session = get_session("fenic_operator_semantic_join")

tickets = session.create_dataframe(
    [
        {"ticket_id": 1, "text": "I cannot log in after the SSO redirect."},
        {"ticket_id": 2, "text": "The CSV export for reports is timing out."},
    ]
)

teams = session.create_dataframe(
    [
        {"team": "Identity", "responsibility": "Authentication, SSO, login, and account access."},
        {"team": "Analytics", "responsibility": "Reports, dashboards, exports, and metrics."},
    ]
)

result = tickets.semantic.join(
    teams,
    predicate="{{ left_on }} should be handled by the team responsible for {{ right_on }}",
    left_on=fc.col("text"),
    right_on=fc.col("responsibility"),
)

result.show()
