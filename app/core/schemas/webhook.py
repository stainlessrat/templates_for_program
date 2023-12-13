from .base import BaseSchema


class Webhook(BaseSchema):
    test: str
    value: str
