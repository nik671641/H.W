###################### DICTIONARY ######################
# Я выбррал структуру dict потому что есть ключи и значения, так легче сохранять данные, а потом выводить в консоль по ключам


def calculateTax(amount_money,amount_percentage, amount_assignment):
    tax =  (amount_percentage / 100) * amount_money
    ###################### DICTIONARY ######################
    # Я выбррал структуру dict потому что есть ключи и значения, так легче сохранять данные, а потом выводить в консоль по ключам

    data_amount_money = {'amount_money : ': str(amount_money),
                         'amount_percentage : ': str(amount_percentage),
                         'amount_assignment : ': str(amount_assignment),
                         'amount_tax : ': str(tax)}
    df = data_amount_money.items()
    def convertsion(df):
        for i in df:
            print(''.join(i))
    convertsion(df)
######################## PYTHON DOCSTRINGS #############################
# функция вызывается в app.py получает арументы
# арументы
# далее благодаря арументам вычисляется налог из суммы и упаковывает все значения в dict
# после все выводится в консоль
######################## PYTHON DOCSTRINGS #############################
