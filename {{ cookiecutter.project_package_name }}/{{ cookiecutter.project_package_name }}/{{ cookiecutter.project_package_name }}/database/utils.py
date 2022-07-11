from typing import List

from database import Base, Session


def exists(session: Session, model: Base, **kwargs) -> bool:
    return session.query(session.query(model).filter_by(**kwargs).exists()).scalar()


def build_list_query(
    session: Session,
    model: Base,
    filters: List,
):
    query = session.query(model)
    if filters:
        query = query.filter(*filters)
    return query


def build_paginated_list_query(
    list_query,
    order_by: List,
    offset: int,
    limit: int,
):
    if order_by:
        list_query = list_query.order_by(*order_by)
    return list_query.offset(offset).limit(limit)
