from .tools import user_data_fetch


def self_test() -> None:
    import asyncio

    res = asyncio.run(user_data_fetch())
    print(res)


if __name__ == "__main__":
    self_test()
