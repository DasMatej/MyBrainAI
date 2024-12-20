import time
from logger import setup_logger

logger = setup_logger('rate_limiter')

class RateLimiter:
    # max_requests: max number of requests allowed in a period
    def __init__(self, max_requests, period):
        self.max_requests = max_requests
        self.period = period
        self.users = {}

    async def check_limit(self, user_id):
        # If user_id is not in the dictionary, add it
        if user_id not in self.users:
            # Return True because this is the first request
            self.users[user_id] = []

        # If the user has made requests before, check if the last request was made within the period
        timestamps = self.users[user_id]

        # Remove timestamps that are older than the period
        now = time.time()
        while timestamps and now - timestamps[0] > self.period:
            #logger.info(f'User {user_id} has made {len(timestamps)} requests in the last {self.period} seconds')
            timestamps.pop(0)

        # If the number of remaining timestamps is greater than the max_requests, return False
        if len(timestamps) >= self.max_requests:
            logger.warning(f'User {user_id} has exceeded the rate limit because they have made {len(timestamps)+1} requests in the last {self.period} seconds. Next avaliable text in {self.period - (now - timestamps[0])} seconds')
            return False

        # If the number of remaining timestamps is less than the max_requests, add the current timestamp to the list and return True
        logger.info(f'User {user_id} has made {len(timestamps)+1} requests in the last {self.period} seconds (Max requests: {self.max_requests})')
        timestamps.append(now)
        return True
