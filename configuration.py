from ast import literal_eval
from datetime import datetime


class Configuration:
    def __init__(self):
        super().__init__()
        self.date = f'{datetime.now():%d}.{datetime.now():%m}.{datetime.now():%Y}'
        self.time = f'{datetime.now():%H}:{datetime.now():%M}'
        self.coin_first = 0
        self.coin_second = 1
        self.buy = 0
        self.sell = 1

    @staticmethod
    def make_coin_pair_file() -> None:
        """
        The function creates a file with the currency pair name
        :return: None
        """
        with open("coin_pair.spec", "w") as coin_pair:
            coin_pair.write("['" + f'{input("Введите валютную пару: ")}' + "']")

    def verify_coin_pair_file(self) -> None:
        """
        The function checks the presence and correctness of the data of the coin_pair.spec file
        :return: None
        """
        try:
            with open("coin_pair.spec") as coin_pair_verify:
                try:
                    verify = literal_eval(coin_pair_verify.read())[0]
                except (SyntaxError, IndexError):
                    self.make_coin_pair_file()
        except FileNotFoundError:
            self.make_coin_pair_file()

    @staticmethod
    def coin_pair() -> str:
        """
        The function returns the currency pair name
        :return: str
        """
        with open("coin_pair.spec") as pair:
            coin_pair = literal_eval(pair.read())[0]
        return coin_pair

    def get_coin_name(self, coin) -> str:
        """
        The function takes a currency pair name and returns one of two currency pairs
        :param coin: 0 or 1
        :return: str
        """
        return (''.join(self.coin_pair())).split("_")[coin]
