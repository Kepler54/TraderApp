from os import remove
# from interface import Interface
from data_analysis import DataAnalysis

trade = DataAnalysis()


# app = Interface(trade.get_full_info())


def main() -> None:
    """Entry point"""
    try:
        trade.verify_coin_pair_file()
        trade.add_db_value()
        print(trade.get_full_info())
        # app.mainloop()
    except ValueError:
        print("В базе данных осутствуют необходимые значения!")
    except SyntaxError:
        print('В файле "coin_pair" осутствуют необходимые значения!')
        remove("coin_pair.spec")
        remove("_trades.db")
    except (KeyError, FileNotFoundError):
        print('Ошибка названия валютной пары в файле "coin_pair"!')
        remove(f'{trade.coin_pair()}_trades.db')
        remove("coin_pair.spec")
    except KeyboardInterrupt:
        print("Вы ничего не ответили!")

    return None


if __name__ == '__main__':
    main()
