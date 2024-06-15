from datetime import datetime

class mainMenuNetWorth():

    def __init__(self) -> None:
        now= datetime.now()
        self.month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        self.year = now.strftime("%Y")
        self.netWorth = [0,0,0,0,0,0,0,0,0,0,0,0]
        