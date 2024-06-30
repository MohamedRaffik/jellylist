from ninja.security import SessionAuth

from users.models import User


class AsyncDjangoAuth(SessionAuth):
    async def authenticate(self, request, token):
        user: User = await request.auser()
        if user.is_authenticated:
            return user
        return None

    async def get_current_user(self, request) -> User:
        user = await request.auser()
        if not user:
            raise Exception(
                "No user found. Ensure endpoint is protected with `auth` parameter."
            )
        return await request.auser()


class AsyncDjangoAuthSuperUser(AsyncDjangoAuth):
    async def authenticate(self, request, token):
        user: User = await request.auser()
        if user.is_authenticated and user.is_superuser:
            return user
        return None


async_django_auth = AsyncDjangoAuth()
async_django_auth_superuser = AsyncDjangoAuthSuperUser()