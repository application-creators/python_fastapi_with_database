from typing import Dict, List

from database import Base, Session
from database.utils import build_list_query, build_paginated_list_query
from fastapi import HTTPException, status
from serialization.base_models import PaginatedListField


def paginate_list(
    session: Session,
    model: Base,
    offset: int,
    limit: int,
    order_by: List = None,
    filters: List = None,
) -> Dict:
    list_query = build_list_query(session, model, filters)

    paginated_list_query = build_paginated_list_query(
        list_query,
        order_by,
        offset,
        limit,
    )

    total_count = list_query.count()

    results = paginated_list_query.all()

    return {
        PaginatedListField.TOTAL_COUNT: total_count,
        PaginatedListField.COUNT: len(results),
        PaginatedListField.LIMIT: limit,
        PaginatedListField.OFFSET: offset,
        PaginatedListField.RESULTS: results,
    }


def get_or_raise(session: Session, model: Base, **kwargs) -> Base:
    instance = session.query(model).filter_by(**kwargs).one_or_none()

    if not instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{model.__name__} not found: {kwargs}",
        )

    return instance
