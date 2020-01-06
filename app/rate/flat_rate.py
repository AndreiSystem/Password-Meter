from app.rate.rate import Rate


class FlatRate(Rate):
    def __init__(self, weight: int):
        super().__init__(weight)