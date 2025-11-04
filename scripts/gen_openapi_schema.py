import importlib
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <module_name>")
        print(
            "Example: uv run -m scripts.gen_openapi_schema lib.action_groups.user_filter.app > openapi.json"
        )
        sys.exit(1)

    module_name = sys.argv[1]

    module = importlib.import_module(module_name)
    app = module.app

    print(app.get_openapi_json_schema())

    return None


if __name__ == "__main__":
    main()
