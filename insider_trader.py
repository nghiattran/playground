from collections import namedtuple

def findPotentialInsiderTraders(datafeed):
    Transaction = namedtuple('Transaction', ['date', 'name', 'type', 'amount', 'price'])
    transactions = []
    date, price = datafeed[0].split('|')

    flagged_trader = set()
    flags = []

    for entry in datafeed[1:]:
        info = entry.split('|')
        if len(info) == 2:
            date, price = [int(num) for num in info]

            

            for i, transaction in enumerate(transactions):
                if date - transaction.date > 3:
                    continue

                diff = abs(price - transaction.price) * transaction.amount
                print(transaction.name, diff, price - transaction.price, transaction.amount)
                if diff > 500000 and transaction.name not in flagged_trader:
                    flags.append((transaction.date, transaction.name))
                    flagged_trader.add(transaction.name)

        elif len(info) == 4:
            date, name, type, amount = info
            transactions.insert(0, Transaction(
                date=int(date),
                name=name,
                type=type,
                amount=int(amount),
                price=float(price)
            ))
            print(info, transactions[0].amount)

    return ['%d|%s' % pair for pair in sorted(flags)]


# Testing
feed1 = """0|1000
0|Shilpa|BUY|30000
0|Will|BUY|50000
0|Tom|BUY|40000
0|Kristi|BUY|15000
1|Kristi|BUY|11000
1|Tom|BUY|1000
1|Will|BUY|19000
1|Shilpa|BUY|25000
2|1500
2|Will|SELL|7000
2|Shilpa|SELL|8000
2|Kristi|SELL|6000
2|Tom|SELL|9000
3|500
38|1000
78|Shilpa|BUY|30000
79|Kristi|BUY|60000
80|1100
81|1200"""

datafeed1 = feed1.split("\n")

print(findPotentialInsiderTraders(datafeed1))

feed2 = """0|20
0|Kristi|SELL|3000
0|Will|BUY|5000
0|Tom|BUY|50000
0|Shilpa|BUY|1500
1|Tom|BUY|1500000
3|25
5|Shilpa|SELL|1500
8|Kristi|SELL|600000
9|Shilpa|BUY|500
10|15
11|5
14|Will|BUY|100000
15|Will|BUY|100000
16|Will|BUY|100000
17|25"""

datafeed2 = feed2.split("\n")

print(findPotentialInsiderTraders(datafeed2))
