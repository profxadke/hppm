#!/usr/bin/env python3

import os
from subprocess import Popen, PIPE
from httpx import AsyncClient


async def main():
    async with AsyncClient() as client:
        response = await client.get('http://repo.zeenoverse.io/index.json')
        resp = response.json()
        print(resp)


if __name__ == '__main__':
    __import__('uvloop').run(main())