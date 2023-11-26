import asyncio
from asyncio import create_subprocess_shell
from asyncio.subprocess import PIPE, STDOUT
import sys

async def main():
    # create a subprocess in asyncio and connect its stdout to the stdin of another subprocess


    p1 = await create_subprocess_shell("python myfile.py",
                                       stdout=PIPE, stderr=STDOUT)
    while True:
        if p1.stdout.at_eof():
            break
        stdout = (await p1.stdout.readline()).decode()
        if stdout:
            print(f'[stdout] {stdout}')
    await p1.wait()
