import random

class BetLog:
    def __init__(self):
        self.log = list()
        self.record = dict()
        self.time = 1
        self.refresh()

    def refresh(self):
        self.record = {
            "time": 0,
            "capital": 0,
            "bet": 0,
            "result": False,
            "balance": 0,
            "capital_after": 0,
            "all_in": False
        }

    def push_preset(self, capital, bet):
        self.record["time"] = self.time
        self.record["capital"] = capital
        self.record["bet"] = bet
        if self.record["capital"] == self.record["bet"]:
            self.record["all_in"] = True

    def push_result(self, result, balance):
        self.record["result"] = result
        self.record["balance"] = balance
        self.record["capital_after"] = self.record["capital"] + balance

    def submit(self):
        self.log.append(self.record)
        self.refresh()
        self.time += 1

    def output(self, page = 0):
        output = ""
        if page:
            output = "{} try #{}: capital: {}, bet: {} [{}] balance: {}, capital_after:{}".format(
                "[ALL-IN]" if self.log[page - 1]["all_in"] else "",
                self.log[page - 1]["time"],
                self.log[page - 1]["capital"],
                self.log[page - 1]["bet"],
                "WON" if self.log[page - 1]["result"] else "LOST",
                self.log[page - 1]["balance"],
                self.log[page - 1]["capital_after"]
            )
        else:
            for line in self.log:
                output += "{} try #{}: capital: {}, bet: {} [{}] balance: {}, capital_after:{}\n".format(
                    "[ALL-IN]" if line["all_in"] else "",
                    line["time"],
                    line["capital"],
                    line["bet"],
                    "WON" if line["result"] else "LOST",
                    line["balance"],
                    line["capital_after"]
                )
        print(output)

capital = 100000
times = 0
win_rate = 0.5
power = 2
origin_bet = 100
bet = origin_bet
last_won = True

betlog = BetLog()
while times < 100 and capital > 0:
    # get in new round
    times += 1

    # calculate bet this time
    if last_won:
        bet = origin_bet
    else:
        bet *= 2
        # if not enough for doubling, all-in
        if capital - bet <= 0:
            bet = capital
    betlog.push_preset(capital, bet)

    # gambling section
    capital -= bet
    balance = 0
    if random.random() < win_rate:
        # won
        balance = bet * power
        capital += balance
        last_won = True
    else:
        # lost
        balance = - bet
        last_won = False
    betlog.push_result(last_won, balance)
    betlog.submit()
betlog.output()

