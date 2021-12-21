import json
from pprint import pprint

from statement import Statement


def main() -> None:
    statement_obj = Statement()
    result = statement_obj.statement(
        json.load(open('invoices.json'))[0],
        json.load(open('plays.json')),
    )
    pprint(result)


if __name__ == '__main__':
    main()
