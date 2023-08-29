import requests
from configuration import Configuration


class TradeInfo(Configuration):
    @staticmethod
    def get_info() -> dict:
        """
        Information about all current pairs
        :return: dict
        """
        response = requests.get(
            url="https://yobit.net/api/3/info"
        )
        return response.text

    def get_ticker(self) -> dict:
        """
        Information about a pair or pairs in the last 24 hours
        :return: dict
        """
        response = requests.get(
            url=f"https://yobit.net/api/3/ticker/{self.coin_pair()}?ignore_invalid=1"
        )
        return response.text

    @staticmethod
    def get_depth(coin_one="eth", coin_two="usd", limit=150) -> str:
        """
        asks - dictionary with orders for sale [price, number of coins ready to sell]
        bids - dictionary with orders to buy [price, number of coins ready to buy]
        :param coin_one: eth
        :param coin_two: usd
        :param limit: int
        :return: str
        """
        response = requests.get(
            url=f"https://yobit.net/api/3/depth/{coin_one}_{coin_two}?limit={limit}&ignore_invalid=1"
        )
        bids = response.json()[f"{coin_one}_usd"]["bids"]
        total_bids_amount = 0
        for i in bids:
            price = i[0]
            coin_amount = i[1]
            total_bids_amount += price * coin_amount

        return f"Total bids: {total_bids_amount} $"  # общая сумма выставленных на закуп последних 150 ордеров

    @staticmethod
    def get_trades(coin_one="eth", coin_two="usd", limit=150) -> str:
        """
        Allows you to retrieve already completed buy and sell transactions
        Returns the total amount of coins bought and sold
        :param coin_one: eth
        :param coin_two: usd
        :param limit: int
        :return: str
        """
        response = requests.get(
            url=f"https://yobit.net/api/3/trades/{coin_one}_{coin_two}?limit={limit}&ignore_invalid=1"
        )

        total_trade_ask = 0  # общая сумма продажи
        total_trade_bid = 0  # общая сумма покупки

        for i in response.json()[f"{coin_one}_{coin_two}"]:
            if i["type"] == "ask":
                total_trade_ask += i["price"] * i["amount"]
            if i["type"] == "bid":
                total_trade_bid += i["price"] * i["amount"]

        info = (
            f"TOTAL {coin_one} SELL: {round(total_trade_ask, 4)} $\n"
            f"TOTAL {coin_one} BUY: {round(total_trade_bid, 4)} $"
        )
        return info
