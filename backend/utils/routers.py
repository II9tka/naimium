from typing import Type, Tuple, Union, Iterable

from rest_framework_nested import routers
from rest_framework.viewsets import GenericViewSet

from inflection import tableize, singularize


def lazy_router(
        view_sets: Tuple[Type[GenericViewSet], ...],
        router: Union[routers.DefaultRouter, routers.SimpleRouter] = routers.DefaultRouter(),
):
    for view_set in view_sets:
        model_name = view_set.serializer_class.Meta.model.__name__
        tableized_model_name = tableize(model_name)

        router.register(fr'{tableized_model_name}', view_set, basename=model_name)

    return router


def lazy_nested_router(
        url: str,
        view_sets: Union[Tuple[Type[GenericViewSet], ...], Type[GenericViewSet]],
        router: Union[routers.DefaultRouter, routers.SimpleRouter],
        nested_router: Union[routers.NestedDefaultRouter, routers.NestedSimpleRouter] = routers.NestedDefaultRouter
):
    if not isinstance(view_sets, tuple):
        view_sets = view_sets,

    router = nested_router(router, fr'{url}', lookup=singularize(url))
    return lazy_router(view_sets, router=router)
