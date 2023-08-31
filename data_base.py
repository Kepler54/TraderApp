import sqlite3
from ast import literal_eval
from trade_info import TradeInfo


class DataBase(TradeInfo):
    def add_db_value(self) -> None:
        """
        The function creates a database
        :return: None
        """
        with sqlite3.connect(f"{self.coin_pair()}_trades.db") as db:
            cur = db.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS trades
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                date TEXT, time TEXT, coin_pair TEXT, buy TEXT, sell TEXT, amount TEXT, percent TEXT
                )
                """
            )
            cur.execute(
                "INSERT INTO trades VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)",
                (
                    self.date, self.time, self.coin_pair(),
                    literal_eval(self.get_ticker())[self.coin_pair()]["buy"],
                    literal_eval(self.get_ticker())[self.coin_pair()]["sell"],
                    self.entry_value("Введите сумму входа на рынок: "),
                    self.entry_value("Введите процент: ")
                )
            )

    def get_value_list(self, select) -> list:
        """
        The function accepts a query to the database and returns a list of data
        :param select: str
        :return: list
        """
        with sqlite3.connect(f"{self.coin_pair()}_trades.db") as db:
            cur = db.cursor()
            cur.execute(select)
            return cur.fetchall()

    def entry_value(self, request) -> float:
        """
        The function takes the market entry amount, commission in percent and returns a float value
        :param request: str
        :return: float
        """
        try:
            try:
                if self.get_value_list(
                        "SELECT date, time, coin_pair, buy, sell, amount, percent FROM trades"
                )[0][0]:
                    pass
            except IndexError:
                return float(input(request))
        except KeyboardInterrupt:
            pass
