import strawberry
from strawberry.fastapi import GraphQLRouter

from gql_schema.queries import Query
from gql_schema.mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_router = GraphQLRouter(schema)
