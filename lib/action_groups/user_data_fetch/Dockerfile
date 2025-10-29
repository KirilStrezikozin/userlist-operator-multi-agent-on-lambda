ARG ARM=true
ARG BASE_IMAGE=public.ecr.aws/lambda/python:3.12${ARM:+-arm64} AS builder

FROM ghcr.io/astral-sh/uv:0.9.5 AS uv

FROM ${BASE_IMAGE} AS builder

ENV UV_COMPILE_BYTECODE=1
ENV UV_NO_INSTALLER_METADATA=1
ENV UV_LINK_MODE=copy

RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv export --frozen --no-emit-workspace --no-dev --no-editable -o requirements.txt && \
    uv pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

FROM ${BASE_IMAGE}

ENV POWERTOOLS_SERVICE_NAME="user_data_fetch_function"
ENV POWERTOOLS_METRICS_NAMESPACE="UserDataFetch"
ENV POWERTOOLS_LOG_LEVEL="INFO"

COPY --from=builder ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

COPY ./lib/action_groups/user_data_fetch/app ${LAMBDA_TASK_ROOT}/app

CMD ["app.handler.lambda_handler"]
