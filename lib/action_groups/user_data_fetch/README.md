# UserDataFetch Action Group

## Generate OpenAPI schema

```sh
cd lib/action_groups/user_data_fetch # if in project's root
uv run -m scripts.generate_schema | jq > openapi.json
```

## Docker

Make sure you run the `docker` commands below from the project's root directory.

1. Build an Arm container:

```sh
echo "Building for Arm..."
docker buildx build \
    --platform linux/arm64 \
    --provenance=false \
    -t user_data_fetch_function:latest-arm \
    --file lib/action_groups/user_data_fetch/Dockerfile \
    --build-arg PLATFORM_TAG=-arm64 \
    --load \
    .
```

2. Or build an Intel/AMD container:

```sh
echo "Building for x86_64..."
docker buildx build \
    --platform linux/amd64 \
    --provenance=false \
    -t user_data_fetch_function:latest-x86_64 \
    --file lib/action_groups/user_data_fetch/Dockerfile \
    --build-arg PLATFORM_TAG=-x86_64 \
    --load \
    .
```

## Testing

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
