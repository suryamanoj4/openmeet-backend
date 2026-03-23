from typing import Optional

import strawberry
from strawberry import input
from strawberry.scalars import JSON


@input
class CreateOrganizationInput:
    name: str
    slug: str
    description: Optional[str] = None
    logo_url: Optional[str] = None
    website_url: Optional[str] = None
    social_links: Optional[JSON] = None
    settings: Optional[JSON] = None


@input
class UpdateOrganizationInput:
    name: Optional[str] = None
    description: Optional[str] = None
    logo_url: Optional[str] = None
    website_url: Optional[str] = None
    social_links: Optional[JSON] = None
    settings: Optional[JSON] = None


@strawberry.type
class OrganizationMutationResult:
    organization: Optional["OrganizationType"]
    error: Optional[str]
