from account import Account

var_name = input('Enter your name: ')
var_email = input('Enter your email: ')
var_password = input('Enter your password: ')

account_1 = Account(var_name, var_email, var_password)

def accountUX():
    while True:
        var_choice = input('Do you want to withdraw, deposit, or show account [1/2/3] [To exit, enter any number besides these]: ')

        if var_choice == '1':
            var_withdraw = int(input('Enter how much you want to withdraw: '))
            print(f'Your balance is ${account_1.withdrawalAccount(var_withdraw)}')
        elif var_choice == '2':
            var_deposit = int(input('Enter how much you want to deposit: '))
            print(f'Your balance is ${account_1.depositAccount(var_deposit)}')
        elif var_choice == '3':
            account_1.showAccount()
        else:
            break

if __name__ == '__main__':
    accountUX()
