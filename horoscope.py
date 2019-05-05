import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми","неожиданного праздника", "приятных перемен"]

def generated_prophecies(total_num = 5, num_sentanses = 3):
    prophecies = []
    i = 0
    while i < total_num:
        q = 0
        gorlk = ""

        while q < num_sentanses:
            
            a = random.choice(times)
            b = random.choice(advices)
            d = random.choice(promises)
            full_sentense = a.title() + " " + b + " " + d + "."
            if q != num_sentanses - 1:
                full_sentense = full_sentense + " "
            gorlk = gorlk + full_sentense
            q = q + 1
        prophecies.append(gorlk)   
        i = i + 1
    return prophecies


start = generated_prophecies()
print(start)
     