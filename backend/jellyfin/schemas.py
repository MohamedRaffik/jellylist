from ninja import ModelSchema

from jellyfin.models import JellyfinServer


class JellyfinServerResponseSchema(ModelSchema):
    class Meta:
        model = JellyfinServer
        fields = ["name", "url"]
