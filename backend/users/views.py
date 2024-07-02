from django.contrib.auth import alogin, aauthenticate
from django.http import HttpRequest
from ninja import Router
from ninja.responses import JsonResponse

from base.utils.authentication import async_django_auth, async_django_auth_superuser
from users.models import user_manager
from users.schemas import UserResponseSchema, UserRequestSchema


router = Router()


@router.get("session/", auth=async_django_auth, response=UserResponseSchema)
async def get_session_user(request: HttpRequest):
    user = await async_django_auth.get_current_user(request)
    return user


@router.post("create/", auth=async_django_auth_superuser, response=UserResponseSchema)
async def create_user(request: HttpRequest, data: UserRequestSchema):
    new_user = await user_manager.acreate_user(**data.dict())
    return new_user


@router.post("login/", response=UserResponseSchema)
async def login(request: HttpRequest, data: UserRequestSchema):
    user = await aauthenticate(request, email=data.email, password=data.password)
    if not user:
        return JsonResponse({"detail": "Invalid credentials"}, status=401)
    await alogin(request, user)
    return user
