from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        @staticmethod
        def to_camel(string: str) -> str:
            camel = ''.join(item.capitalize() for item in string.split('_'))
            return camel[0].lower() + camel[1:]

        # https://pydantic-docs.helpmanual.io/usage/model_config/#options
        allow_population_by_field_name = True
        alias_generator = to_camel
