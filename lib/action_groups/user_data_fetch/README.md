# UserDataFetch Action Group

# Docker

Build an ARM container:

```sh
docker buildx build --platform linux/arm64 --provenance=false -t user_data_fetch_function:latest-arm --file lib/action_groups/user_data_fetch/Dockerfile . --load
```

Build an x86_64 container:

```sh
docker buildx build --platform linux/amd64 --provenance=false -t user_data_fetch_function:latest-x86_64 --file lib/action_groups/user_data_fetch/Dockerfile . --build-arg ARM= --load
```

# Testing

Example response:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "age": 24,
      "city": "Berlin"
    },
    {
      "id": 3,
      "name": "Charlie",
      "age": 29,
      "city": "Warsaw"
    },
    {
      "id": 2,
      "name": "Bob",
      "age": 31,
      "city": "Kyiv"
    }
  ],
  "summary": "Fetched a list of 3 users."
}
```
