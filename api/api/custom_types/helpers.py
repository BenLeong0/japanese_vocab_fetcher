from copy import deepcopy
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, create_model
from pydantic.fields import FieldInfo


class MyBaseModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


def partial_model(model: type[MyBaseModel]):
    def make_field_optional(
        field: FieldInfo, default: Any = None
    ) -> tuple[Any, FieldInfo]:
        new = deepcopy(field)
        new.default = default
        new.annotation = Optional[field.annotation]  # type: ignore
        return new.annotation, new

    return create_model(
        f"Partial{model.__name__}",
        __base__=model,
        __module__=model.__module__,
        **{  # type: ignore
            field_name: make_field_optional(field_info)
            for field_name, field_info in model.model_fields.items()
        },
    )
