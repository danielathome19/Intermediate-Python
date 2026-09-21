""" Description:
Maintains a checkbook register and reports a summary of the current months transactions.

An external file provides the following information:
 * The first number in the file is the beginning balance of the account. 
 * The beginning balance is followed by sets of transactions (character-number). 
 * The valid characters are C(check), D(deposit) and S(service charge). 
 * The character E represents the end of data and should not be processed.

- Deposits are automatically added to the account balance.
- Checks are subtracted from the balance if there is enough money in the 
    account to cover the check, otherwise the check is not processed but 
    the account is charged $10.00 for "insufficient funds". 
- Service charges are automatically subtracted from the account. 
- Any other transaction code is output as an "illegal transaction code" 
    and the balance is unaffected.

In addition to maintaining the running balance of the account, 
a summary report of the Deposits and Withdrawals (checks, insufficient funds, 
and service charges) is to be maintained and printed.

Sample output:
                    Qty     Amount
====================================
Starting Balance            $20.05
Deposits            1       $100.00
Withdrawals         3       $30.00
Ending Balance              $90.05
=========================================================
"""

from dataclasses import dataclass


@dataclass
class Transaction:
    type: str
    amount: float


class Bank:
    def __init__(self, balance: float):
        self._balance = balance
        self._transactions: list[Transaction] = []
    
    def process(self, tx: Transaction):
        if tx.type == 'C':
            if self._balance >= tx.amount:
                self._balance -= tx.amount
            else:
                self._balance -= 10.0  # Insufficient funds
                self._transactions.append(Transaction('I', 10.00))
                return
        elif tx.type == 'D':
            self._balance += tx.amount
        elif tx.type == 'S':
            self._balance -= tx.amount
        else:
            print(f"Invalid transaction type: {tx.type}")
            return
        self._transactions.append(tx)


def main():
    account: Bank = None

    try:
        with open('lecture5/checkout.txt', 'r') as f:
            lines = f.readlines()
            init_balance = float(lines[0].strip())
            account = Bank(init_balance)
            for line in lines[1:]:
                line = line.strip()
                if line[0] in ['C', 'D', 'S']:
                    tx_type = line[0]
                    tx_amt = float(line[1:])
                    txn = Transaction(tx_type, tx_amt)
                    account.process(txn)
                elif line.startswith('E'):
                    break
    except FileNotFoundError:
        print("File not found")
        return

    deposit_sum = 0.0
    withdrawal_sum = 0.0
    deposit_count = 0
    withdrawal_count = 0

    for tx in account._transactions:
        if tx.type == 'D':
            deposit_sum += tx.amount
            deposit_count += 1
        else:
            withdrawal_sum += tx.amount
            withdrawal_count += 1

    print(f"Beginning Balance: ${init_balance:.2f}")
    print(f"Deposits ({deposit_count}): ${deposit_sum:.2f}")
    print(f"Withdrawals ({withdrawal_count}): ${withdrawal_sum:.2f}")
    print(f"Final Balance: ${account._balance:.2f}")
    pass


if __name__ == "__main__":
    main()
