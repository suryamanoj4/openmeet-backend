from typing import List, Optional
from uuid import UUID

import strawberry
from strawberry import Info

from gql_schema.types import (
    UserType,
    OrganizationType,
    EventType,
    MemberType,
    TicketType,
    OrderType,
    AttendeeType,
    FollowerType,
    EventStaffType,
    PaymentType,
    OrderItemType,
)
from gql_schema.services import UserService, OrganizationService, EventService
from models import User, Organization, Event, Ticket, Member, Order, Attendee


@strawberry.type
class Query:
    @strawberry.field
    async def users(
        self,
        info: Info,
        skip: int = 0,
        limit: int = 100,
    ) -> List[UserType]:
        service = UserService(info)
        users = await service.get_all(skip=skip, limit=limit)
        return [
            UserType(
                id=user.id,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                phone=user.phone,
                avatar_url=user.avatar_url,
                is_email_verified=user.is_email_verified,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users
        ]

    @strawberry.field
    async def user(
        self,
        info: Info,
        id: UUID,
    ) -> Optional[UserType]:
        service = UserService(info)
        user = await service.get_by_id(id)
        if not user:
            return None
        return UserType(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            phone=user.phone,
            avatar_url=user.avatar_url,
            is_email_verified=user.is_email_verified,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @strawberry.field
    async def organizations(
        self,
        info: Info,
        skip: int = 0,
        limit: int = 100,
    ) -> List[OrganizationType]:
        service = OrganizationService(info)
        orgs = await service.get_all(skip=skip, limit=limit)
        return [
            OrganizationType(
                id=org.id,
                name=org.name,
                slug=org.slug,
                description=org.description,
                logo_url=org.logo_url,
                website_url=org.website_url,
                social_links=org.social_links,
                settings=org.settings,
                is_verified=org.is_verified,
                created_at=org.created_at,
                updated_at=org.updated_at,
            )
            for org in orgs
        ]

    @strawberry.field
    async def organization(
        self,
        info: Info,
        id: UUID,
    ) -> Optional[OrganizationType]:
        service = OrganizationService(info)
        org = await service.get_by_id(id)
        if not org:
            return None
        return OrganizationType(
            id=org.id,
            name=org.name,
            slug=org.slug,
            description=org.description,
            logo_url=org.logo_url,
            website_url=org.website_url,
            social_links=org.social_links,
            settings=org.settings,
            is_verified=org.is_verified,
            created_at=org.created_at,
            updated_at=org.updated_at,
        )

    @strawberry.field
    async def events(
        self,
        info: Info,
        organization_id: Optional[UUID] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> List[EventType]:
        service = EventService(info)
        events = await service.get_all(
            skip=skip,
            limit=limit,
            organization_id=organization_id,
        )
        return [
            EventType(
                id=event.id,
                organization_id=event.organization_id,
                name=event.name,
                slug=event.slug,
                description=event.description,
                event_type=event.event_type,
                status=event.status,
                visibility=event.visibility,
                start_date=event.start_date,
                end_date=event.end_date,
                timezone=event.timezone,
                venue_name=event.venue_name,
                venue_address=event.venue_address,
                venue_city=event.venue_city,
                venue_country=event.venue_country,
                is_online=event.is_online,
                online_url=event.online_url,
                max_attendees=event.max_attendees,
                min_tickets_per_order=event.min_tickets_per_order,
                max_tickets_per_order=event.max_tickets_per_order,
                registration_start=event.registration_start,
                registration_end=event.registration_end,
                cover_image_url=event.cover_image_url,
                banner_image_url=event.banner_image_url,
                settings=event.settings,
                created_at=event.created_at,
                updated_at=event.updated_at,
            )
            for event in events
        ]

    @strawberry.field
    async def event(
        self,
        info: Info,
        id: UUID,
    ) -> Optional[EventType]:
        service = EventService(info)
        event = await service.get_by_id(id)
        if not event:
            return None
        return EventType(
            id=event.id,
            organization_id=event.organization_id,
            name=event.name,
            slug=event.slug,
            description=event.description,
            event_type=event.event_type,
            status=event.status,
            visibility=event.visibility,
            start_date=event.start_date,
            end_date=event.end_date,
            timezone=event.timezone,
            venue_name=event.venue_name,
            venue_address=event.venue_address,
            venue_city=event.venue_city,
            venue_country=event.venue_country,
            is_online=event.is_online,
            online_url=event.online_url,
            max_attendees=event.max_attendees,
            min_tickets_per_order=event.min_tickets_per_order,
            max_tickets_per_order=event.max_tickets_per_order,
            registration_start=event.registration_start,
            registration_end=event.registration_end,
            cover_image_url=event.cover_image_url,
            banner_image_url=event.banner_image_url,
            settings=event.settings,
            created_at=event.created_at,
            updated_at=event.updated_at,
        )
