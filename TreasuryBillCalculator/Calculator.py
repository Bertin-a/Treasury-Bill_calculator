ratesDownload = __import__('ratesDownload').ratesDownload


class Calculator:
    def __init__(self, face_value, duration):
        self.rates = ratesDownload()
        self.face_value = face_value
        self.duration = duration
        self.maturityDays = int(self.duration)
        self.durationRates = self.getRates()
        self.discount_price = float(self.durationRates['discount'])
        self.interest_rate = float(self.durationRates['interest'])
        self.days = self.durationRates['duration']
        self.price = self.calculate_purchase_price()


    def getRates(self):
        self.rates_data = self.rates[self.duration]
        return self.rates_data

    def calculate_purchase_price(self):
        self.purchase_price = int(self.face_value) * (1 - (self.discount_price * self.maturityDays / 365))
        return self.purchase_price

    def effective_annual_yield(self):
        self.annual_yeild = (self.face_value / self.purchase_price) ** (365 / self.maturityDays) - 1
        return self.annual_yeild

    def interest_earned(self):
        self.interest = self.face_value - self.purchase_price
        return self.interest





cal = Calculator(1000, '91')
duration_rates = cal.interest_earned()
print(duration_rates)