"""
TODO:

You're writing a web backend.
Annotate a function `execute_query` which runs SQL, but also can prevent SQL injection attacks.

NOTE: You don't need to implement `execute_query`
"""

from typing import Iterable, LiteralString


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...):
    pass


# def query_user(user_id: str):
#     query = f"SELECT * FROM data WHERE user_id = {user_id}"
#     mypy ignored that case (https://github.com/python/mypy/issues/12554, https://github.com/python/mypy/issues/16169)
#     execute_query(sql=query) expect-type-error


def query_data(user_id: str, limit: bool) -> None:
    query = """
        SELECT
            user.name,
            user.age
        FROM data
        WHERE user_id = ?
    """

    if limit:
        query += " LIMIT 1"

    execute_query(query, (user_id,))
