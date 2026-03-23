from typing import Optional
from uuid import UUID

import strawberry
from strawberry import Info
from passlib.hash import bcrypt

from gql_schema.types import (
    UserType,
    OrganizationType,
    EventType,
    TicketType,
)
from gql_schema.inputs import (
    CreateUserInput,
    UpdateUserInput,
    CreateOrganizationInput,
    UpdateOrganizationInput,
    CreateEventInput,
    UpdateEventInput,
    CreateTicketInput,
    UpdateTicketInput,
)
from gql_schema.services import UserService, OrganizationService, EventService
from models import User, Organization, Event, Ticket


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(
        self,
        info: Info,
        input: CreateUserInput,
    ) -> UserType:
        service = UserService(info)
        user = await service.create(
            User,
            email=input.email,
            password_hash=bcrypt.hash(input.password),
            first_name=input.first_name,
            last_name=input.last_name,
            phone=input.phone,
            avatar_url=input.avatar_url,
        )
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

    @strawberry.mutation
    async def update_user(
        self,
        info: Info,
        id: UUID,
        input: UpdateUserInput,
    ) -> Optional[UserType]:
        service = UserService(info)
        user = await service.get_by_id(id)
        if not user:
            return None

        update_data = {}
        if input.first_name is not None:
            update_data["first_name"] = input.first_name
        if input.last_name is not None:
            update_data["last_name"] = input.last_name
        if input.phone is not None:
            update_data["phone"] = input.phone
        if input.avatar_url is not None:
            update_data["avatar_url"] = input.avatar_url

        user = await service.update(user, **update_data)
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

    @strawberry.mutation
    async def delete_user(
        self,
        info: Info,
        id: UUID,
    ) -> bool:
        service = UserService(info)
        user = await service.get_by_id(id)
        if not user:
            return False
        await service.delete(user)
        return True

    @strawberry.mutation
    async def create_organization(
        self,
        info: Info,
        input: CreateOrganizationInput,
    ) -> OrganizationType:
        service = OrganizationService(info)
        org = await service.create(
            Organization,
            name=input.name,
            slug=input.slug,
            description=input.description,
            logo_url=input.logo_url,
            website_url=input.website_url,
            social_links=input.social_links,
            settings=input.settings,
        )
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

    @strawberry.mutation
    async def update_organization(
        self,
        info: Info,
        id: UUID,
        input: UpdateOrganizationInput,
    ) -> Optional[OrganizationType]:
        service = OrganizationService(info)
        org = await service.get_by_id(id)
        if not org:
            return None

        update_data = {}
        if input.name is not None:
            update_data["name"] = input.name
        if input.description is not None:
            update_data["description"] = input.description
        if input.logo_url is not None:
            update_data["logo_url"] = input.logo_url
        if input.website_url is not None:
            update_data["website_url"] = input.website_url
        if input.social_links is not None:
            update_data["social_links"] = input.social_links
        if input.settings is not None:
            update_data["settings"] = input.settings

        org = await service.update(org, **update_data)
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

    @strawberry.mutation
    async def delete_organization(
        self,
        info: Info,
        id: UUID,
    ) -> bool:
        service = OrganizationService(info)
        org = await service.get_by_id(id)
        if not org:
            return False
        await service.delete(org)
        return True

    @strawberry.mutation
    async def create_event(
        self,
        info: Info,
        input: CreateEventInput,
    ) -> EventType:
        service = EventService(info)
        event = await service.create(
            Event,
            organization_id=input.organization_id,
            name=input.name,
            slug=input.slug,
            description=input.description,
            event_type=input.event_type,
            status=input.status,
            visibility=input.visibility,
            start_date=input.start_date,
            end_date=input.end_date,
            timezone=input.timezone,
            venue_name=input.venue_name,
            venue_address=input.venue_address,
            venue_city=input.venue_city,
            venue_country=input.venue_country,
            is_online=input.is_online,
            online_url=input.online_url,
            max_attendees=input.max_attendees,
            min_tickets_per_order=input.min_tickets_per_order,
            max_tickets_per_order=input.max_tickets_per_order,
            registration_start=input.registration_start,
            registration_end=input.registration_end,
            cover_image_url=input.cover_image_url,
            banner_image_url=input.banner_image_url,
            settings=input.settings,
        )
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

    @strawberry.mutation
    async def update_event(
        self,
        info: Info,
        id: UUID,
        input: UpdateEventInput,
    ) -> Optional[EventType]:
        service = EventService(info)
        event = await service.get_by_id(id)
        if not event:
            return None

        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        event = await service.update(event, **update_data)

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

    @strawberry.mutation
    async def delete_event(
        self,
        info: Info,
        id: UUID,
    ) -> bool:
        service = EventService(info)
        event = await service.get_by_id(id)
        if not event:
            return False
        await service.delete(event)
        return True
