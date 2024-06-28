import random

class Account: 
    def __init__(self, name, email, password):
        self.name = name 
        self.email = email
        self.password = password
        self.balance = random.randint(500, 10000)  
    
    def withdrawalAccount(self, withdrawal):
        if withdrawal <= self.balance:
            self.balance -= withdrawal
            return self.balance
        else:
            print('Insufficient balance!')
            return self.balance
    
    def depositAccount(self, deposit):
        self.balance += deposit
        return self.balance

    def showAccount(self):
        hidden_password = '******'
        print('='*40)
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print(f'Password: {hidden_password}')
        print(f'Balance: ${self.balance}')
        print('='*40)
