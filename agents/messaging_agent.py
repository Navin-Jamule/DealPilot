import os
import requests
from openai import OpenAI
from agents.deals import Opportunity
from agents.agent import Agent

pushover_url = "https://api.pushover.net/1/messages.json"


class MessagingAgent(Agent):
    name = "Messaging Agent"
    color = Agent.WHITE
    MODEL = "gpt-5-mini"

    def __init__(self):
        self.log("Messaging Agent is initializing")

        self.pushover_user = os.getenv("PUSHOVER_USER", "your-pushover-user-if-not-using-env")
        self.pushover_token = os.getenv("PUSHOVER_TOKEN", "your-pushover-token-if-not-using-env")
        self.openai = OpenAI()
        self.log("Messaging Agent has initialized Pushover and OpenAI")

    def push(self, text):
        self.log("Messaging Agent is sending a push notification")
        payload = {
            "user": self.pushover_user,
            "token": self.pushover_token,
            "message": text,
            "sound": "cashregister",
        }

        requests.post(pushover_url, data=payload)

    def craft_message(self, description: str, deal_price: float, estimated_true_value: float) -> str:
        try:
            user_prompt = (
                "Summarize this deal in 2-3 exciting sentences for a push notification.\n"
                f"Item: {description}\n"
                f"Price: {deal_price}\n"
                f"Estimated Value: {estimated_true_value}\n"
                "Make it engaging but not spammy."
            )

            response = self.openai.chat.completions.create(
                model=self.MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a marketing assistant creating short, exciting deal notifications."
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
                # temperature=0.3
            )

            return response.choices[0].message.content if response.choices else ""

        except Exception as e:
            self.log(f"Error in craft_message: {e}")
            return ""

    def notify(self, description: str, deal_price: float, estimated_true_value: float, url: str):
        self.log("Messaging Agent is using OpenAI to craft the message")

        text = self.craft_message(description, deal_price, estimated_true_value)

        if not text:
            text = "Great deal available! Check it out"
        short_text = text[:200].rsplit(" ", 1)[0]

        self.push(f"{short_text}... {url}")

        self.log("Messaging Agent has completed")

    def alert(self, opportunity: Opportunity):
        text = (
            f"Deal Alert! Price=${opportunity.deal.price:.2f}, "
            f"Estimate=${opportunity.estimate:.2f}, "
            f"Discount=${opportunity.discount:.2f}: "
            f"{opportunity.deal.product_description[:50]}... "
            f"{opportunity.deal.url}"
        )

        self.push(text)
        self.log("Messaging Agent has completed")