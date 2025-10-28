def self_test() -> None:
    from .agent import orchestrator_agent

    prompt = 'Filtering criteria:\n"only age > 30"'
    res = orchestrator_agent(prompt)
    print(res)


if __name__ == "__main__":
    self_test()
