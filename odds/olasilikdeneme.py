import math
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
import json


url = "https://www.soccerstats.com/homeaway.asp?league=england"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

satirlar = soup.find_all("tr", class_="odd")

EvdeMatches = []
AwayMatches = []

for i, row in enumerate(satirlar):
    fontlar = row.find_all("font", color="green")
    
    for font in fontlar:
        data = font.text.strip()
        data = float(data)
        data = int(data)
        if i < 20:
            EvdeMatches.append(data)
        elif 20 <= i < 40:
            AwayMatches.append(data)
            

home_table = soup.find("div", id="h2h-team1")
away_table = soup.find("div", id="h2h-team2")

home_takim_siralamasi = []
away_takim_siralamasi = []

if home_table:
    satirlar_home = home_table.find_all("tr", class_="odd")
    for satir in satirlar_home:
        takim_isimi = satir.find("td", style="padding-left:4px;").text.strip()
        home_takim_siralamasi.append(takim_isimi)

if away_table:
    satirlar_away = away_table.find_all("tr", class_="odd")
    for satir in satirlar_away:
        takim_isimi = satir.find("td", style="padding-left:4px;").text.strip()
        away_takim_siralamasi.append(takim_isimi)


birlestirilmis_evdeki_maclar = []
birlestirilmis_away_maclar = []

for i in range(len(EvdeMatches)):
    birlestirilmis_evdeki_maclar.append((home_takim_siralamasi[i], EvdeMatches[i]))

for i in range(len(AwayMatches)):
    birlestirilmis_away_maclar.append((away_takim_siralamasi[i], AwayMatches[i]))

evdeki_maclar_sirali = sorted(birlestirilmis_evdeki_maclar)
away_maclar_sirali = sorted(birlestirilmis_away_maclar)

awayhomelist = []
for evdeki, awaydeki in zip(evdeki_maclar_sirali, away_maclar_sirali):
    awayhomelist.append((evdeki[0], evdeki[1], awaydeki[1]))


GoalsF1 = []
GoalsF2 = []

for i, yenixd in enumerate(satirlar):
    fontlar = yenixd.find_all("font", color="blue")
    
    for font in fontlar:
        data = font.text.strip()
        data = float(data)
        data = int(data)
        if i < 20:
            GoalsF1.append(data)
        elif 20 <= i < 40:
            GoalsF2.append(data)
            


evdeki_goller = []
for takim, gol_evde in zip(home_takim_siralamasi, GoalsF1):
    evdeki_goller.append((takim, gol_evde))

deplasmandaki_goller = []
for takim, gol_deplasman in zip(away_takim_siralamasi, GoalsF2):
    deplasmandaki_goller.append((takim, gol_deplasman))

evdeki_goller_sirali = sorted(evdeki_goller, key=lambda x: x[0])
deplasmandaki_goller_sirali = sorted(deplasmandaki_goller, key=lambda x: x[0])

birlesmis_goller = []
for evdeki, deplasmandaki in zip(evdeki_goller_sirali, deplasmandaki_goller_sirali):
    birlesmis_goller.append((evdeki[0], evdeki[1], deplasmandaki[1]))



finalList1 = []

for home_team, home_games, away_games in awayhomelist:
    for team, home_atilan, away_atilan in birlesmis_goller:
        if home_team == team:
            finalList1.append((home_team, home_games, away_games, home_atilan, away_atilan))
            break


GoalsA1_yenilen = []
GoalsA2_yenilen = []

for i, row in enumerate(satirlar):
    fontlar = row.find_all("font", color="#C70039")
    
    for font in fontlar:
        data = font.text.strip()
        data = float(data)
        data = int(data)
        if i < 20:
            GoalsA1_yenilen.append(data)
        elif 20 <= i < 40:
            GoalsA2_yenilen.append(data)


evdeki_goller_yenilen = []
for takim, gol_evde_yenilen in zip(home_takim_siralamasi, GoalsA1_yenilen):
    evdeki_goller_yenilen.append((takim, gol_evde_yenilen))

deplasmandaki_goller_yenilen = []
for takim, gol_deplasman_yenilen in zip(away_takim_siralamasi, GoalsA2_yenilen):
    deplasmandaki_goller_yenilen.append((takim, gol_deplasman_yenilen))

evdeki_goller_sirali_yenilen = sorted(evdeki_goller_yenilen, key=lambda x: x[0])
deplasmandaki_goller_sirali_yenilen = sorted(deplasmandaki_goller_yenilen, key=lambda x: x[0])

birlesmis_goller_yenilen = []
for evdeki, deplasmandaki in zip(evdeki_goller_sirali_yenilen, deplasmandaki_goller_sirali_yenilen):
    birlesmis_goller_yenilen.append((evdeki[0], evdeki[1], deplasmandaki[1]))



finalList2 = []

for home_team, home_games, away_games, home_scored, away_scored in finalList1:
    for team, home_conceded, away_conceded in birlesmis_goller_yenilen:
        if home_team == team:
            finalList2.append((home_team, home_games, away_games, home_scored, away_scored, home_conceded, away_conceded))
            break





home_table_wins = soup.find("div", id="h2h-team1")
away_table_wins = soup.find("div", id="h2h-team2")

home_takim_wins = []
away_takim_wins = []

if home_table_wins:
    satirlar_home_wins = home_table_wins.find_all("tr", class_="odd")
    for satirlar_win in satirlar_home_wins:
        win_sayilari = satirlar_win.find_all("td")[3]
        for win_sayisi in win_sayilari:
            home_takim_wins.append(win_sayisi.text.strip())

if away_table_wins:
    satirlar_away_wins = away_table_wins.find_all("tr", class_="odd")
    for satirlar_win in satirlar_away_wins:
        win_sayilari = satirlar_win.find_all("td")[3]
        for win_sayisi in win_sayilari:
            away_takim_wins.append(win_sayisi.text.strip())

birlestirilmis_evdeki_kazanma_sayilari = []
for i in range(len(home_takim_wins)):
    birlestirilmis_evdeki_kazanma_sayilari.append((home_takim_siralamasi[i], home_takim_wins[i]))

birlestirilmis_away_kazanma_sayilari = []
for i in range(len(away_takim_wins)):
    birlestirilmis_away_kazanma_sayilari.append((away_takim_siralamasi[i], away_takim_wins[i]))

evdeki_kazanma_sayilari_sirali = sorted(birlestirilmis_evdeki_kazanma_sayilari, key=lambda x: x[0])
away_kazanma_sayilari_sirali = sorted(birlestirilmis_away_kazanma_sayilari, key=lambda x: x[0])

awayhome_kazanma_listesi = []
for evdeki, deplasmandaki in zip(evdeki_kazanma_sayilari_sirali, away_kazanma_sayilari_sirali):
    awayhome_kazanma_listesi.append((evdeki[0], evdeki[1], deplasmandaki[1]))





home_table_draws = soup.find("div", id="h2h-team1")
away_table_draws = soup.find("div", id="h2h-team2")

home_takim_draws = []
away_takim_draws = []

if home_table_draws:
    satirlar_home_draws = home_table_draws.find_all("tr", class_="odd")
    for satirlar_draw in satirlar_home_draws:
        draw_sayilari = satirlar_draw.find_all("td")[4].text.strip()  
        home_takim_draws.append(draw_sayilari) 

if away_table_draws:
    satirlar_away_draws = away_table_draws.find_all("tr", class_="odd")
    for satirlar_draw in satirlar_away_draws:
        draw_sayilari = satirlar_draw.find_all("td")[4].text.strip()  
        away_takim_draws.append(draw_sayilari)  



birlestirilmis_evdeki_beraberlik_sayilari = []
for i in range(len(home_takim_draws)):
    birlestirilmis_evdeki_beraberlik_sayilari.append((home_takim_siralamasi[i], home_takim_draws[i]))

birlestirilmis_away_beraberlik_sayilari = []
for i in range(len(away_takim_draws)):
    birlestirilmis_away_beraberlik_sayilari.append((away_takim_siralamasi[i], away_takim_draws[i]))

evdeki_beraberlik_sayilari_sirali = sorted(birlestirilmis_evdeki_beraberlik_sayilari, key=lambda x: x[0])
away_beraberlik_sayilari_sirali = sorted(birlestirilmis_away_beraberlik_sayilari, key=lambda x: x[0])

awayhome_beraberlik_listesi = []
for evdeki, deplasmandaki in zip(evdeki_beraberlik_sayilari_sirali, away_beraberlik_sayilari_sirali):
    awayhome_beraberlik_listesi.append((evdeki[0], evdeki[1], deplasmandaki[1]))





home_table_loses = soup.find("div", id="h2h-team1")
away_table_loses = soup.find("div", id="h2h-team2")

home_takim_loses = []
away_takim_loses = []

if home_table_loses:
    satirlar_home_loses = home_table_loses.find_all("tr", class_="odd")
    for satirlar_lose in satirlar_home_loses:
        lose_sayilari = satirlar_lose.find_all("td")[5]
        for lose_sayisi in lose_sayilari:
            home_takim_loses.append(lose_sayisi.text.strip())

if away_table_loses:
    satirlar_away_loses = away_table_loses.find_all("tr", class_="odd")
    for satirlar_lose in satirlar_away_loses:
        lose_sayilari = satirlar_lose.find_all("td")[5]
        for lose_sayisi in lose_sayilari:
            away_takim_loses.append(lose_sayisi.text.strip())

birlestirilmis_evdeki_kaybetme_sayilari = []
for i in range(len(home_takim_loses)):
    birlestirilmis_evdeki_kaybetme_sayilari.append((home_takim_siralamasi[i], home_takim_loses[i]))

birlestirilmis_away_kaybetme_sayilari = []
for i in range(len(away_takim_loses)):
    birlestirilmis_away_kaybetme_sayilari.append((away_takim_siralamasi[i], away_takim_loses[i]))

evdeki_kaybetme_sayilari_sirali = sorted(birlestirilmis_evdeki_kaybetme_sayilari, key=lambda x: x[0])
away_kaybetme_sayilari_sirali = sorted(birlestirilmis_away_kaybetme_sayilari, key=lambda x: x[0])

awayhome_kaybetme_listesi = []
for evdeki, deplasmandaki in zip(evdeki_kaybetme_sayilari_sirali, away_kaybetme_sayilari_sirali):
    awayhome_kaybetme_listesi.append((evdeki[0], evdeki[1], deplasmandaki[1]))



finalList = []
customList = []
finalList = [(x[0], x[1] ,x[2], x[3], x[4], x[5], x[6], int(y[1]), int(y[2]), int(z[1]), int(z[2]), int(u[1]), int(u[2]) )for x, y, z, u in zip(finalList2, awayhome_kazanma_listesi, awayhome_beraberlik_listesi, awayhome_kaybetme_listesi)]

customList = [(x[0], x[1] + x[2], int(y[1]) + int(y[2]), int(z[1]) + int(z[2]), int(u[1]) + int(u[2]), x[3] + x[4], x[5] + x[6]) for x, y, z, u in zip(finalList2, awayhome_kazanma_listesi, awayhome_beraberlik_listesi, awayhome_kaybetme_listesi)]

data = {
    "Team": [x[0] for x in customList],
    "Played Matches": [x[1] for x in customList],
    "Won Matches": [x[2] for x in customList],
    "Drew Matches": [x[3] for x in customList],
    "Lost Matches": [x[4] for x in customList],
    "Goals Scored": [x[5] for x in customList],
    "Goals Conceded": [x[6] for x in customList]
}

df = pd.DataFrame(data)

selected_columns = ["Team", "Played Matches", "Won Matches", "Drew Matches", "Lost Matches", "Goals Scored", "Goals Conceded"]
df_selected = df[selected_columns]

pd.set_option('display.max_columns', None)  # Tüm sütunları göstermek için maksimum sütun sayısını ayarlayın
print(df_selected.to_string(index=False))

while True:
    
        

    print()
    print("Type 'go' for possibility calculator")
    print("And 'exit' for shut the program down")
    inp = input()
    if inp=="exit":
        break
    print()
    print("Choose 2 teams to find out the odds for the match")




    total_played_games = 0
    total_scored_goals = 0
    total_home_games = 0
    total_home_goals = 0
    total_home_conceded = 0
    total_away_conceded = 0
    total_away_games = 0
    total_away_goals = 0


    for team in finalList:
        total_played_games += (team[1] + team[2])/2 
        total_scored_goals += team[3] + team[4]
    
        total_home_games += team[1]/2
        total_home_goals += team[3]
    
        total_away_games += team[2]/2
        total_away_goals += team[4]
    
        total_home_conceded += team[5]
        total_away_conceded += team[6]
    

    total_average_goal = total_scored_goals / total_played_games



    average_home_goal = total_home_games / total_home_goals

    average_away_goal = total_away_games / total_away_goals




    first_teamname = input("First team: ").capitalize()
    second_teamname = input("Second team: ").capitalize()


    first_team_stats = None
    second_team_stats = None

    for team in finalList:
        if first_teamname == team[0]:
            first_team_stats = team
            break

    for team in finalList:
        if second_teamname == team[0]:
            second_team_stats = team
            break

    if first_team_stats and second_team_stats:
    


        first_team_gpg_general = (first_team_stats[3] + first_team_stats[4]) / (first_team_stats[1] + first_team_stats[2])
    
        second_team_gpg_general = (second_team_stats[3] + second_team_stats[4]) / (second_team_stats[1] + second_team_stats[2])
    
        first_team_gpg_home = first_team_stats[3] / first_team_stats[1]
    
        second_team_conceded_away = second_team_stats[6] / second_team_stats[2]
    
        second_team_gpg_away = second_team_stats[4] / second_team_stats[2]
    
        first_team_conceded_home = first_team_stats[5] / first_team_stats[1]
    
    
    
        home_attack = first_team_gpg_home / first_team_gpg_general
        away_defence = second_team_conceded_away / first_team_gpg_general
        away_attack = second_team_gpg_away / second_team_gpg_general
        home_defence = first_team_conceded_home / second_team_gpg_general
    
        projected_home_goals = home_attack * away_defence * first_team_gpg_general
        projected_away_goals = away_attack * home_defence * second_team_gpg_general
        projected_total_goals = projected_home_goals + projected_away_goals
        print()
        print()
        print("Predicted goals for ", first_teamname, round(projected_home_goals,2))
        print("Projected away goals for ", second_teamname, round(projected_away_goals,2))
        print()
        print()
        giris = input("Enter the predicted match score with space for odds calculation e.g. (2 1): ")
        sayilar = giris.split()

        a = int(sayilar[0])
        b = int(sayilar[1])
        probofa = ((projected_home_goals ** a) * (2.718 **(-projected_home_goals))) / math.factorial(a)
        probofb = ((projected_away_goals ** b) * (2.718 **(-projected_away_goals))) / math.factorial(b)

        print("Odds of ", first_teamname, " scoring ", a, " goals is %{:.2f}".format(probofa*100))
        print("Odds of ", second_teamname, " scoring ", b, " goals is %{:.2f}".format(probofb*100))
        probofgameresult = probofa * probofb
        print("The odds of the ", a, "-", b, " score is %{:.2f}".format(probofgameresult*100))

        
        print()
        print()
        home_win_probability = 0
        for a in range(11):
            for b in range(a):
                probofa = ((projected_home_goals ** a) * (2.718 ** (-projected_home_goals))) / math.factorial(a)
                probofb = ((projected_away_goals ** b) * (2.718 ** (-projected_away_goals))) / math.factorial(b)
                probofgameresult = probofa * probofb
                home_win_probability += probofgameresult

        away_win_probability = 0
        for b in range(11):
            for a in range(b):
                probofa = ((projected_home_goals ** a) * (2.718 ** (-projected_home_goals))) / math.factorial(a)
                probofb = ((projected_away_goals ** b) * (2.718 ** (-projected_away_goals))) / math.factorial(b)
                probofgameresult = probofa * probofb
                away_win_probability += probofgameresult
        print()
        print("Win probability for", first_teamname, "team: %{:.2f}".format(home_win_probability * 100))
        print("So the lowest odds for home win should be {:.2f}".format ((1/home_win_probability)+0.17 ) )
        print()
        print("Draw probability: %{:.2f}".format( 100*(1-(home_win_probability+away_win_probability))))
        print("So the lowest odds for draw should be {:.2f}".format( (1/(home_win_probability+away_win_probability))+0.17) )
        print()
        print("Win probability for", second_teamname, "team: %{:.2f}".format(away_win_probability * 100))
        print("So the lowest odds for away win should be {:.2f}".format ((1/away_win_probability)+0.17) )
        print()
        print()
        print("Or there is a better way. Don't get involved in betting ;D")
    
    else:
        print("Mistake! Double check the names of your teams.")
        continue
        
    