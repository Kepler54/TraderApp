from data_analysis import DataAnalysis

trade = DataAnalysis()


def main() -> None:
    """Entry point"""
    trade.verify_pair_file()
    trade.add_db_value()
    print(trade.get_full_info())


if __name__ == '__main__':
    main()
