import re
from typing import List


def get_pagination_urls(url: str) -> List[str]:

    x = re.findall(r"(\[[0-9]+\-[0-9]+\])", url)

    nums = re.findall(r"[0-9]+", x[0])
    nums = list(range(int(nums[0]), int(nums[1]) + 1))
    nums = [str(n) for n in nums]

    return [url.replace(x[0], num) for num in nums]
