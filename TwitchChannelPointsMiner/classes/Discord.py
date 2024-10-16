from textwrap import dedent

import requests

from TwitchChannelPointsMiner.classes.Settings import Events


class Discord(object):
    __slots__ = ["webhook_api", "events"]

    def __init__(self, webhook_api: str, events: list):
        self.webhook_api = webhook_api
        self.events = [str(e) for e in events]

    def send(self, message: str, event: Events) -> None:
        if str(event) in self.events:
            requests.post(
                url=self.webhook_api,
                data={
                    "content": dedent(message),
                    "username": "Rushymusy",
                    "avatar_url": "https://static.wikia.nocookie.net/doors-game/images/2/2b/Rush_Moving.gif/revision/latest/scale-to-width-down/250?cb=20221002084139",
                },
            )
