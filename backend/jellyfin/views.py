from ninja import Router
from ninja.responses import JsonResponse

from base.utils.authentication import async_django_auth
from jellyfin.models import JellyfinServer
from jellyfin.schemas import JellyfinServerResponseSchema

router = Router()


@router.get("server/", auth=async_django_auth, response=JellyfinServerResponseSchema)
async def get_server(request):
    server = await JellyfinServer.objects.afirst()
    if not server:
        return JsonResponse({"error": "No Jellyfin server configured"}, status=404)
    return server
