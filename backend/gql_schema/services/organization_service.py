from typing import Optional, List
from uuid import UUID

from sqlmodel import select
from strawberry import Info

from gql_schema.services.base import BaseService
from models import Organization, Member, Event, Follower


class OrganizationService(BaseService[Organization]):
    async def get_by_slug(self, slug: str) -> Optional[Organization]:
        result = await self.session.exec(
            select(Organization).where(Organization.slug == slug)
        )
        return result.first()

    async def get_by_id(self, id: UUID) -> Optional[Organization]:
        result = await self.session.exec(
            select(Organization).where(Organization.id == id)
        )
        return result.first()

    async def get_members(self, organization_id: UUID) -> List[Member]:
        result = await self.session.exec(
            select(Member)
            .where(Member.organization_id == organization_id)
            .where(Member.is_active == True)
        )
        return list(result.all())

    async def get_events(self, organization_id: UUID) -> List[Event]:
        result = await self.session.exec(
            select(Event)
            .where(Event.organization_id == organization_id)
            .where(Event.is_active == True)
        )
        return list(result.all())

    async def get_followers(self, organization_id: UUID) -> List[Follower]:
        result = await self.session.exec(
            select(Follower)
            .where(Follower.organization_id == organization_id)
            .where(Follower.is_active == True)
        )
        return list(result.all())

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Organization]:
        result = await self.session.exec(select(Organization).offset(skip).limit(limit))
        return list(result.all())
