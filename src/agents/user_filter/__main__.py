from .tools import user_filter


def self_test() -> None:
    import asyncio

    from agents.user_provider import user_data_fetch_action

    users = asyncio.run(user_data_fetch_action())
    criteria = "only age > 30"

    res = user_filter(users, criteria)
    print(res.model_dump_json())


if __name__ == "__main__":
    self_test()
