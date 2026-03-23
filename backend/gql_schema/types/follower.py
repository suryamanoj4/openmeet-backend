import uuid
from datetime import datetime

import strawberry


@strawberry.type
class FollowerType:
    id: uuid.UUID
    user_id: uuid.UUID
    organization_id: uuid.UUID
    created_at: datetime
    is_active: bool
