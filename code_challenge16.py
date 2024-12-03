

def create_accout (name, initial_deposit = 0):
    Acc_n = name
    balance=initial_deposit
    print(f"BANK ACCOUNT CREATED FOR {Acc_n} WITH INITIAL DEPOSIT OD {balance}")

def get_deno(amount):
    libo = amount // 1000
    libo_sukli = amount % 1000

    five_h = libo_sukli // 500
    fh_sukli = libo_sukli % 500

    two_h = fh_sukli // 200
    twh_sukli = fh_sukli // 200

    one_h = twh_sukli // 100
    onh_sukli = twh_sukli % 100

    fifty = onh_sukli // 50
    fifty_sukli = twh_sukli % 50

    twenty = fifty_sukli // 20
    twe_sukli = fifty_sukli % 20

    ten = twe_sukli // 10
    ten_sukli = twe_sukli % 10

    five = ten_sukli // 5
    five_sukli = ten_sukli % 5

    one = five_sukli // 1
    one_sukli = five_sukli % 1


    print(f" The breakdown based on the [hilippine denomiation for the  amount of {amount}")
    print(f"libo - 1000")
    
    