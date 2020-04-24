import asyncio
from ariadne import SubscriptionType, make_executable_schema
from ariadne.asgi import GraphQL

from ariadne import SchemaDirectiveVisitor
from graphql import default_field_resolver
from core.security import get_current_user, oauth2_scheme


class IsAuthenticated(SchemaDirectiveVisitor):
    def visit_field_definition(self, field, object_type):
        original_resolver = field.resolve
        async def resolve_authentication(obj, info, **kwargs):
            param = await oauth2_scheme(info.context['request'])
            if await get_current_user(param):
                return original_resolver(obj, info, **kwargs)
            return None

        field.resolve = resolve_authentication
        return field

type_def = """
    directive @isAuthenticated on FIELD_DEFINITION

    type Query{
        _unused: Boolean
    }

    type Subscription {
        counter: Int! @isAuthenticated
    }
"""

subscription = SubscriptionType()

@subscription.source("counter")
async def counter_generator(obj, info):
    for i in range(5):
        await asyncio.sleep(1)
        yield i


@subscription.field("counter")
def counter_resolver(count, info):
    return count + 1


schema = make_executable_schema(type_def, subscription, directives={"isAuthenticated": IsAuthenticated})
