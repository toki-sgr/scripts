import random
from statistics import *


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
        return output

class HardGambler:
    def __init__(self, win_rate = 0.5, power = 2, origin_capital = 100000, origin_bet = 100, time_limit = 100):
        self.win_rate = win_rate
        self.power = power
        self.origin_capital = origin_capital
        self.origin_bet = origin_bet
        self.time_limit = time_limit

        self.betlogs = list()
        self.explogs = list()
        self.exp_result = dict()

    def _gamble(self):
        # initializing
        betlog = BetLog()
        times = 0
        last_won = True
        bet = self.origin_bet
        capital = self.origin_capital

        while times < self.time_limit and capital > 0:
            # get in new round
            times += 1

            # calculate bet this time
            if last_won:
                bet = self.origin_bet
            else:
                bet *= 2
                # if not enough for doubling, all-in
                if capital - bet <= 0:
                    bet = capital
            betlog.push_preset(capital, bet)

            # gambling section
            capital -= bet
            balance = 0
            if random.random() < self.win_rate:
                # won
                balance = bet * self.power
                capital += balance
                last_won = True
            else:
                # lost
                balance = - bet
                last_won = False
            betlog.push_result(last_won, balance)
            betlog.submit()
        
        # record result
        self.betlogs.append(betlog.output())
        self.explogs.append({
            "times": times,
            "final_capital": capital
        })

    def execute_experiment(self, exp_times = 1):
        for i in range(exp_times):
            self._gamble()

        self.exp_result["exp_times"] = exp_times
        self.exp_result["failed_times"] = 0
        self.exp_result["total_balance"] = 0

        times = list()
        final_capitals = list()

        for explog in self.explogs:
            times.append(explog["times"])
            final_capitals.append(explog["final_capital"])
            if explog["final_capital"] == 0:
                self.exp_result["failed_times"] += 1
            self.exp_result["total_balance"] += explog["final_capital"] - self.origin_capital
        self.exp_result["times_mean"] = mean(times)
        self.exp_result["times_min"] = min(times)
        self.exp_result["capital_mean"] = mean(final_capitals)
        self.exp_result["capital_max"] = max(final_capitals)
        self.exp_result["capital_stdev"] = int(stdev(final_capitals))
        self.exp_result["capital_variance"] = int(variance(final_capitals))
        


    def output(self):
        return self.betlogs, self.explogs, self.exp_result

if __name__ == "__main__":
    hg = HardGambler(win_rate = 0.5, power = 2, origin_capital = 100000, origin_bet = 100, time_limit = 100)
    hg.execute_experiment(100)
    betlogs, explogs, exp_result = hg.output()
    
    # if len(explogs) == 1:
    #     print(betlogs[0])
    # else:
    #     for explog in explogs:
    #         print(explog)
    print(exp_result)