from statsforecast.models import AutoARIMA


class ARIMA:

    def __init__(self):
        self.logger = None

    def train(self. data):
        self.model = auto_arima(
            data,
            start_p=0,
            start_q=0,
            max_p=3,
            max_q=3,
            m=1,
            seasonal=False,
            trace=True,
            error_action="ignore",
            suppress_warnings=True,
        )

    def forecast(self):
        pass
