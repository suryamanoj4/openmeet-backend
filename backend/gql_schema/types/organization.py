import uuid
from datetime import datetime
from typing import Optional

import strawberry
from strawberry.scalars import JSON


@strawberry.type
class OrganizationType:
    id: uuid.UUID
    name: str
    slug: str
    description: Optional[str]
    logo_url: Optional[str]
    website_url: Optional[str]
    social_links: Optional[JSON]
    settings: Optional[JSON]
    is_verified: bool
    created_at: datetime
    updated_at: datetime
