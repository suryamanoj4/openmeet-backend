import uuid
from datetime import datetime
from typing import Optional

import strawberry
from strawberry import input


@input
class CreateUserInput:
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None


@input
class UpdateUserInput:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None


@strawberry.type
class UserMutationResult:
    user: Optional["UserType"]
    error: Optional[str]
