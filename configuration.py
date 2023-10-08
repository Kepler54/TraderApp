from ast import literal_eval


class Descriptor:
    def __set_name__(self, owner, name) -> None:
        self.name = f"_{name}"

    def __get__(self, instance, owner) -> int:
        return getattr(instance, self.name)


class Configuration:
    buy = Descriptor()
    sell = Descriptor()
    coin_first = Descriptor()
    coin_second = Descriptor()

    @classmethod
    def verify_instance(cls, instance) -> None:
        if type(instance) != float:
            raise TypeError

    def __init__(self, buy=0, sell=1, coin_first=0, coin_second=1, percent=0.2):
        self._buy = buy
        self._sell = sell
        self._coin_first = coin_first
        self._coin_second = coin_second
        self._percent = percent

    @property
    def percent(self) -> float:
        return self._percent

    @percent.setter
    def percent(self, instance):
        self.verify_instance(instance)
        self._percent = instance

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
                    literal_eval(coin_pair_verify.read())[0]
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
