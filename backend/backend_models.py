import asyncio

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count


class Runner:
    def __init__(self):
        self.counter = Counter()
        self.kill = False

    async def run_main(self):
        while not self.kill:
            await asyncio.sleep(5)




class Tenant:
    users: dict[str, Runner] = {}
