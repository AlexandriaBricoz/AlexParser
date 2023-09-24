import sqlite3
from bs4 import BeautifulSoup
with open ("FFf.html") as file:
    src = file.read()
conn = sqlite3.connect('/Users/aleksey/Documents/Untitled')
cursor = conn.cursor()


def Ii(i):
    cursor.execute(f"SELECT COUNT(*) FROM NewTable;")
    count = cursor.fetchone()[0]
    if count == 0:
        i = 0
    else:
        cursor.execute("SELECT id FROM NewTable ORDER BY id DESC LIMIT 1;")
        i = int(cursor.fetchall()[0][0])
    return i
def Perebor(f):
    with open(f, 'r') as file:
        lines = file.readlines()
    l = []
    for j in lines:
        l.append(j.rsplit('\n', 1)[0])
    print(l)
    print("Желаете добавить тег?(YES or NO)")
    k = input()
    while k == "YES":
        l.append(input())
        print("Желаете добавить тег?(YES or NO)")
        k = input()
        print(l)
    return l

def Sup(i,l):
    c = []
    for st in l:
        c = soup.find_all(st)
        i = Plo(i,st,c)
    return c
def Plo(i,st,c):
    for a in c:
        i = i+1
        cursor.execute("INSERT INTO NewTable (id, teg, text) VALUES (?, ?, ?);", (i, st, a.text))
    conn.commit()
    return i
def hol(results,i):
    for n in range(i):
        print(results[n])

def delete():
    print("Желаете очистить таблицу?(YES or NO)")
    s = input()
    if s == "YES":
        cursor.execute("DELETE FROM NewTable;")
        conn.commit()

cursor.execute("SELECT * FROM NewTable;")
results = cursor.fetchall()
soup = BeautifulSoup(src,"lxml")
conn.row_factory = sqlite3.Row
i = 0
i=Ii(i)
hol(results,i)
l = Perebor('pereborH.txt')
print(l)
Sup(i,l)
cursor.execute("SELECT * FROM NewTable;")
results = cursor.fetchall()
hol(results,i)
delete()
cursor.close()
conn.close()

#SELECT MAX(id) FROM NewTable;

# title = soup.title
# print(title.text,"\n")
# find = soup.find("div", class_="user__data").find("span").text
# print(find,"\n")
# find2 = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text
#
# print(find2 ,"\n")
# find3 = soup.find("div", class_="user__info").find_all("span")
# for Gg in find3:
#     print(Gg.text.strip())
# print("\n")
# print(find3[4].text)
# find4 = soup.find("div", class_="social__networks").find("ul").find_all("a")
# for Gg in find4:
#     jh = Gg.text
#     hl = Gg.get("href")
#     print(f"{jh}: {hl}")
# find5 = soup.find("span", class_="city__label").find_parent()
# print(find5,"\n")
# find6 = soup.find("span", class_="city__label").next_element.next_element.next_element
# print(find6)