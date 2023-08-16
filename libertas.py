import json

import requests
from pydantic import BaseModel


class MintResponse(BaseModel):
    success: bool
    message: str


def get_response(address: str) -> MintResponse:
    url = f"https://qr-mint.g7p.io/api/checkWhitelist?wallet={address}"
    response = requests.get(url=url)
    return MintResponse.parse_obj(json.loads(response.content))


if __name__ == '__main__':
    with open('address.txt') as file:
        lines = [line for line in file.read().splitlines() if line]

    for num, address in enumerate(lines):
        if address:
            try:
                response = get_response(address=address)
                print(f'#{num + 1} | {address} | {response.success}, {response.message}')
            except Exception as e:
                print(e.args)

