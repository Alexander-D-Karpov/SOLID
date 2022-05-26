from abc import ABC


class FX:
    def get_rate(self):
        return 1.2


class FX_Alpha:
    def get_rate(self):
        return 1.23549845339485737495839


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        converter = FX_Alpha()
        print(f'{amount} {from_currency} = {amount * converter.get_rate()} {to_currency}')
        return amount * converter.get_rate()


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        converter = FX()
        print(f'{amount} {from_currency} = {amount * converter.get_rate()} {to_currency}')
        return amount * converter.get_rate()


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def change_converter(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


converter = FXConverter()
converter2 = AlphaConverter()

app = App(converter)
app.start()

app.change_converter(converter2)
app.start()
