import uuid
from datetime import datetime
from typing import Optional

import strawberry
from strawberry.scalars import JSON


@strawberry.type
class AttendeeType:
    id: uuid.UUID
    order_item_id: uuid.UUID
    ticket_id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    custom_data: Optional[JSON]
    check_in_status: bool
    checked_in_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
