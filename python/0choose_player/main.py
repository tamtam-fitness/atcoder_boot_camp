import random
import time
import datetime
import pytz
from typing import List

def read_pre_not_player() -> str:
    with open("./0choose_player/tmp.txt", mode="r") as f :
        pre_not_player = f.read()
        return pre_not_player

def write_current_not_player(current_not_player: str) -> None:
    with open("./0choose_player/tmp.txt", mode="w") as f :
        f.write(current_not_player)


def choose_player_and_current_not_player(pre_not_player: str, players: List[str]) -> tuple:

    #前回の人をからなずplayerとする
    players.append(pre_not_player)
    #ランダムでplayerを選ぶ際に除外
    persons.remove(pre_not_player)

    #余ったpersonから一人playerとして選出
    person = random.choice(persons)
    players.append(person)
    #personsから除外
    persons.remove(person)

    #あまったpersonが今回答えない人
    current_not_player = persons[0]

    return players, current_not_player


def print_questions_num_and_player(players: List[str]) -> None:
    ques_list = [1, 2]
    for idx in range(len(players)) :
        ques = random.choice(ques_list)
        ques_list.remove(ques)
        print(players[idx], ques)


def read_datetime():
    with open("./0choose_player/date.txt", "r") as f:
        str_date = f.read()
        return str_date

def write_datetime(str_today: str) -> None:
    with open("./0choose_player/date.txt", "w") as f:
        f.write(str_today)


if __name__ == "__main__":
    str_date = read_datetime()
    # today = datetime.date.today()
    JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    #GOOD, タイムゾーンを指定している．早い
    today = datetime.datetime.now(JST)
    str_today = today.strftime("%Y-%m-%d")
    
    if str_date == str_today :
        print(f"{str_today}でのプレイヤーの選定は終了しました。")
    else:
        print("選定を開始します")
        time.sleep(1)

        太田 = "太田"
        梶村 = "梶村"
        田村 = "田村"
        persons = [太田, 梶村, 田村]
        players = []
        
        pre_not_player = read_pre_not_player()
        #今回のplayerとnot_playerを選出
        players, current_not_player = choose_player_and_current_not_player(pre_not_player, players)
        #次回playerとして選出するために記憶
        write_current_not_player(current_not_player)
        print_questions_num_and_player(players)

        #出力した日付を選択
        write_datetime(str_today) 
        print(f"選定日を更新しました：{str_today}")

 











