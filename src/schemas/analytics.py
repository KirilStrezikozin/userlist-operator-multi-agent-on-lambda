from .base import Base
from .user import UserDataFetchResult


class FinalAnalyticsCount(Base):
    unfiltered: int
    filtered: int


class FinalAnalyticsResult(UserDataFetchResult):
    count: FinalAnalyticsCount
