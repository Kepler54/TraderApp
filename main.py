from data_analysis import DataAnalysis

trade = DataAnalysis()


def main() -> None:
    """Entry point"""
    try:
        trade.verify_pair_file()
        trade.add_db_value()
        print(trade.get_full_info())
    except ValueError:
        print("В базе данных осутствуют необходимые значения!")
    except SyntaxError:
        print("В файле coin_pair осутствуют необходимые значения!")
    except KeyboardInterrupt:
        print("Вы ничего не ответили!")


if __name__ == '__main__':
    main()
