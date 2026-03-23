import uuid
from datetime import datetime
from typing import Optional

import strawberry


@strawberry.type
class OrderType:
    id: uuid.UUID
    event_id: uuid.UUID
    order_number: str
    status: str
    customer_email: str
    customer_first_name: Optional[str]
    customer_last_name: Optional[str]
    customer_phone: Optional[str]
    subtotal: float
    tax_amount: float
    discount_amount: float
    total: float
    currency: str
    payment_status: str
    notes: Optional[str]
    created_at: datetime
    updated_at: datetime
