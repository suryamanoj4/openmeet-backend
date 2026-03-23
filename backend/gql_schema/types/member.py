import uuid
from datetime import datetime

import strawberry


@strawberry.type
class MemberType:
    id: uuid.UUID
    user_id: uuid.UUID
    organization_id: uuid.UUID
    role: str
    joined_at: datetime
    created_at: datetime
