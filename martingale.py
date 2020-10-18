import random

capital = 100000
times = 0
win_rate = 0.5
power = 2
origin_bet = 100
bet = origin_bet
last_won = True
log_dict = {
    "time": 0,
    "capital": 0,
    "bet": 0,
    "capital_before": 0,
    "result": "",
    "balance": 0,
    "capital_after": 0
}

while times < 100 and capital > 0:
    # get in new round
    times += 1
    log_dict["time"] = times

    # calculate bet this time
    if last_won:
        bet = origin_bet
    else:
        bet *= 2
        # if not enough for doubling, all-in
        if capital - bet < 0:
            bet = capital
    log_dict["capital"] = capital
    log_dict["bet"] = bet

    # gambling section
    capital -= bet
    log_dict["capital_before"] = capital
    balance = 0
    if random.random() < win_rate:
        # won
        balance = bet * power
        capital += balance
        log_dict["result"] = "win"
        last_won = True
    else:
        # lost
        balance = - bet
        log_dict["result"] = "lost"
        last_won = False
    log_dict["balance"] = balance
    log_dict["capital_after"] = capital

    # log output
    log_str = ""
    for key, value in log_dict.items():
        log_str += key + ":" + str(value) + ", "
    print(log_str)



