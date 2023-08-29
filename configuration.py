from ast import literal_eval


class Configuration:
    @staticmethod
    def make_pair_file() -> None:
        """
        The function creates a file with the currency pair name
        :return: None
        """
        with open("coin_pair.spec", "w") as pair:
            pair.write("['" + f'{input("Введите валютную пару: ")}' + "']")

    def verify_pair_file(self) -> None:
        """
        The function checks the presence and correctness of the data of the coin_pair.spec file
        :return: None
        """
        try:
            with open("coin_pair.spec") as pair_verify:
                try:
                    verify = literal_eval(pair_verify.read())[0]
                except (SyntaxError, IndexError):
                    self.make_pair_file()
        except FileNotFoundError:
            self.make_pair_file()

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
