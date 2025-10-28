from .tools import user_filter


def self_test() -> None:
    import asyncio

    from agents.user_provider import user_data_fetch

    users = asyncio.run(user_data_fetch())
    criteria = "only age > 30"

    res = user_filter(users, criteria)
    print(res)


if __name__ == "__main__":
    self_test()
