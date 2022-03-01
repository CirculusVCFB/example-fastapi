import pytest
from app.calculations import add, BankAccount

@pytest.mark.parametrize("num1, num2, expected", [

	(3,2,5),
	(7,1,8),
	(12,4,16)
	
	])
def test_add(num1, num2, expected):
	print("testing add function")
	assert add(num1, num2) == expected 

def test_bank_set_initial_amount():
	bank_account = BankAccount(50)
	assert bank_account.balance == 50

def test_bank_default_amount():
	bank_account = BankAccount()
	assert bank_account.balance == 0

def test_withdraw():
	bank_account = BankAccount(50)
	bank_account.withdraw(20)
	assert bank_account.balance == 30

def test_deposit():
	bank_account = BankAccount(50)
	bank_account.deposit(30)
	assert bank_account.balance ==  80

def test_collect_interest():
	bank_account = BankAccount(50)
	bank_account.collect_interest()
	assert round(bank_account.balance, 4) == 55



