import uuid
from datetime import datetime

import strawberry


@strawberry.type
class OrderItemType:
    id: uuid.UUID
    order_id: uuid.UUID
    ticket_id: uuid.UUID
    quantity: int
    unit_price: float
    total_price: float
    created_at: datetime
    is_active: bool
