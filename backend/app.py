"""FastAPI application with GraphQL."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.ext.asyncio import AsyncSession

from database import AsyncSessionLocal, async_engine
from gql_schema import schema


async def get_db_context() -> dict:
    async with AsyncSessionLocal() as session:
        try:
            yield {"db": session}
        finally:
            await session.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await async_engine.dispose()


graphql_router = GraphQLRouter(
    schema,
    context_getter=get_db_context,
    allow_queries_via_get=True,
)

app = FastAPI(
    title="OpenMeets API",
    description="GraphQL API for OpenMeets event management platform",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(graphql_router, prefix="/graphql")


@app.get("/")
async def root():
    return {"message": "Welcome to OpenMeets GraphQL API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
