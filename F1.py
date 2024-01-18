import requests, re
from bs4 import BeautifulSoup as bs
import csv, codecs, copy
import pandas as pd


# ----------------------------------------------------------------------
# Parser 2023

url = requests.get(
    "https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0-1_%D0%B2_%D1%81%D0%B5%D0%B7%D0%BE%D0%BD%D0%B5_2023")
print(f"Status connect: {url.status_code}")
soup = bs(url.text, "html.parser")

# Parser main table:
search_columns_table1 = soup.find("table", {"class": "wikitable"}).findAll("th")
search_info_table1 = soup.find("table", {"class": "wikitable"}).findAll("td")

# Parser table result:
search_columns_table2 = soup.find("div", {"style": "overflow-x: auto; margin: 1em 0"}) \
    .find("table", {"class": "wikitable"}).findAll("th")
search_info_table2 = soup.find("div", {"style": "overflow-x: auto; margin: 1em 0"}) \
    .find("table", {"class": "wikitable"}).findAll("td")

# ----------------------------------------------------------------------
# Parser main table:

# for a in search_columns_table1:
#     print(a.text)
#
# for b in search_info_table1:
#     print(b.text)

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Parser table result:

# Name columns
names_columns = []
for a in search_columns_table2:
    if a.text.replace("\n", "") not in names_columns:
        names_columns.append(a.text.replace("\n", ""))

# Info in columns
info_columns = []
for b in search_info_table2:
    info_columns.append(b.text.replace("\n", "").strip())

# Result info
info_columns_lists = []
spam = []
for c in range(len(info_columns)):
    modul = re.compile(r"(\[П \d\d?\])(\[П \d\])?$")
    meaning = info_columns[c].replace(modul.search(info_columns[c]).group(), "") \
        if type(modul.search(info_columns[c])) == re.Match else info_columns[c]
    spam.append(meaning)
    if len(spam) == 25:
        if len(spam) != 0:
            #print(spam)
            info_columns_lists.append(spam.copy())
            spam.clear()

# Edit "Result info" and "Info in columns" - concat numbers of pilots
number = names_columns[-len(info_columns_lists):]
del names_columns[-len(info_columns_lists):]
for d in range(len(info_columns_lists)):
    info_columns_lists[d].insert(0, number[d])

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Save to cvs:

# Save to cvs file
with codecs.open("F1.csv", "w") as file_csv:
    writer = csv.writer(file_csv)
    writer.writerow(names_columns)
    for i in info_columns_lists:
        writer.writerow(i)

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Sorted:

# Open DataFrame
import pandas as pd
import codecs
import numpy as np

df = pd.read_csv(codecs.open("F1.csv"))
position_info = {}

# Sorted position race
for a in range(22):
    place_finish = {}
    position_info.setdefault(df.values[a, 1], 0)
    for b in df.values[a, 3:-1]:
        if type(b) == str:
            if b.isdecimal():
                place_finish.setdefault("Position: " + str(b), 0)
                place_finish["Position: " + str(b)] += 1
            else:
                b = 0
                place_finish.setdefault("Position: " + str(b), 0)
                place_finish["Position: " + str(b)] += 1
        else:
            if str(b).isalpha():
                b = 0
                place_finish.setdefault("Position: " + str(b), 0)
                place_finish["Position: " + str(b)] += 1
            else:
                place_finish.setdefault("Position: " + str(int(b)), 0)
                place_finish["Position: " + str(int(b))] += 1
    position_info[df.values[a, 1]] = place_finish

# ----------------------------------------------------------------------



# ----------------------------------------------------------------------
# Parser 2022

url = requests.get("https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0-1_%D0%B2_%D1%81%D0%B5%D0%B7%D0%BE%D0%BD%D0%B5_2022")
print(f"Status connect: {url.status_code}")
soup = bs(url.text, "html.parser")

# Parser main table:
search_columns_table1 = soup.find("table", {"class":"wikitable"}).findAll("th")
search_info_table1 = soup.find("table", {"class":"wikitable"}).findAll("td")

# Parser table result:
search_columns_table2 = soup.find("div", {"style":"overflow-x: auto; margin: 1em 0"})\
    .find("table", {"class":"wikitable"}).findAll("th")
search_info_table2 = soup.find("div", {"style":"overflow-x: auto; margin: 1em 0"})\
    .find("table", {"class":"wikitable"}).findAll("td")

# ----------------------------------------------------------------------
# Parser main table:

# for a in search_columns_table1:
#     print(a.text)
#
# for b in search_info_table1:
#     print(b.text)

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Parser table result:

# Name columns
names_columns = []
for a in search_columns_table2:
    if a.text.replace("\n", "") not in names_columns:
        names_columns.append(a.text.replace("\n", ""))

# Info in columns
info_columns = []
for b in search_info_table2:
    info_columns.append(b.text.replace("\n", "").strip())

# Result info
info_columns_lists = []
spam = []
for c in range(len(info_columns)):
    modul = re.compile(r"(\[П \d\d?\])(\[П \d\])?$")
    meaning = info_columns[c].replace(modul.search(info_columns[c]).group(), "") \
        if type(modul.search(info_columns[c])) == re.Match else info_columns[c]
    spam.append(meaning)
    if len(spam) == 25:
        if len(spam) != 0:
            #print(spam)
            info_columns_lists.append(spam.copy())
            spam.clear()

# Edit "Result info" and "Info in columns" - concat numbers of pilots
number = names_columns[-len(info_columns_lists):]
del names_columns[-len(info_columns_lists):]
for d in range(len(info_columns_lists)):
    info_columns_lists[d].insert(0, number[d])

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Save to cvs:

# Save to cvs file
with codecs.open("F1_history.csv", "w") as file_csv:
    writer = csv.writer(file_csv)
    writer.writerow(names_columns)
    for i in info_columns_lists:
        writer.writerow(i)

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Sorted:

# Open DataFrame
import pandas as pd
import codecs
df_history = pd.read_csv(codecs.open("F1_history.csv"))
position_info_history = {}

# Sorted position race
for a in range(22):
    place_finish = {}
    position_info_history.setdefault(df_history.values[a, 1], 0)
    for b in df_history.values[a, 3:-1]:
        if type(b) == str:
            if b.isdecimal():
                place_finish.setdefault("Position: " + str(b), 0)
                place_finish["Position: " + str(b)] += 1
            else:
                b = 0
                place_finish.setdefault("Position: " + str(b), 0)
                place_finish["Position: " + str(b)] += 1
        else:
            if str(b).isalpha():
                b = 0
                place_finish.setdefault("Position: " + str(b), 0)
                place_finish["Position: " + str(b)] += 1
            else:
                place_finish.setdefault("Position: " + str(int(b)), 0)
                place_finish["Position: " + str(int(b))] += 1
    position_info_history[df_history.values[a, 1]] = place_finish

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Results history:

# Results all history F1
history_total = copy.deepcopy(position_info)
for a, b in position_info_history.items():
    if a in history_total:
        for c, d in b.items():
            history_total[a].setdefault(c, 0)
            history_total[a][c] += b[c]


names = []
for a in history_total.keys():
    names.append(a)

list_meaning = []
for b in history_total.values():
    x = sorted(b.items())
    list_meaning.append([dict(x)])


# Get index for DataFrame
index_for_df = set()
for a in history_total.values():
    for b in a.keys():
        index_for_df.add(b)

ready_index = []
for b in range(len(index_for_df)):
    ready_index.append("Position: " + str(b))

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# DataFrame:

# DataFrame Final
df_clear = pd.DataFrame(np.zeros((len(names), len(ready_index))), dtype=int, columns=ready_index)
df_names = pd.DataFrame(names, columns=["Names"])
df_final = df_clear.join(df_names).set_index("Names")


for a in names:
    for b in ready_index:
        if b in history_total[a]:
            df_final.loc[a, b] = history_total[a][b]


points_1 = pd.read_csv(codecs.open("F1_history.csv"))
points_2 = pd.read_csv(codecs.open("F1.csv"))
number = pd.read_csv(codecs.open("F1.csv"))["№"]
points = points_1["Очки"] + points_2["Очки"]
df_final = df_final.reset_index().join([points, number]).set_index(["Names", "№"])

print(df_final)