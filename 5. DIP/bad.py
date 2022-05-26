class FX:
    def get_rate(self):
        return 1.2


class Converter:
    def convert(self, from_currency, to_currency, amount):
        converter = FX()
        print(f'{amount} {from_currency} = {amount * converter.get_rate()} {to_currency}')
        return amount * converter.get_rate()


class App:
    def start(self):
        converter = Converter()
        converter.convert('EUR', 'USD', 100)  # bad, cause if FX class will be updated the code would brake


app = App()
app.start()
