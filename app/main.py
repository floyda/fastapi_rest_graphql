"""
main.py
"""
# from ariadne.asgi import GraphQL
# from api.graphql.api import schema
import asyncio
from ariadne import SubscriptionType, make_executable_schema
from ariadne.asgi import GraphQL

type_def = """
    type Query {
        _unused: Boolean
    }

    type Subscription {
        counter: Int
    }
"""

subscription = SubscriptionType()

# @subscription.source("counter")
async def counter_generator(obj, info):
    yield 1
    # for i in range(5):
    #     await asyncio.sleep(1)
    #     yield i


# @subscription.field("counter")
def counter_resolver(count, info):
    return info


subscription.set_field("counter", counter_resolver)
subscription.set_source("counter", counter_generator)
schema = make_executable_schema(type_def, subscription)

from fastapi import FastAPI
from routers import locations, login

app = FastAPI()

app.include_router(login.router)
app.include_router(locations.router)
app.mount("/graphql", GraphQL(schema, debug=True))

    