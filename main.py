#!/usr/bin/env python3

import os, typer
from subprocess import Popen, PIPE
from anyio import create_task_group
from httpx import AsyncClient


app = typer.Typer()


async def fetch_data(url: str) -> None:
    async with AsyncClient() as client:
        print(f"[*] Fetching: {url}")
        response = await client.get(url)
        print(f"[+] Response from {url}: {response.status_code}\t{response.json()}")
        return response.json()  # Returning the response as JSON


async def fetch_repos() -> None:
    repos = [
        'http://repo.zeenoverse.io/index.json'
    ]

    async with create_task_group() as tg:
        # Start each fetch_data task concurrently using task group
        for url in repos:
            tg.start_soon(fetch_data, url)

    print('[X] All tasks finished!')


@app.command()
def main():
    __import__('anyio').run(fetch_repos, backend='trio')


if __name__ == '__main__':
    app()