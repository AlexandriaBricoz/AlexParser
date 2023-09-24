import sqlite3
from bs4 import BeautifulSoup
with open ("FFf.html") as file:
    src = file.read()
#print(src)
conn = sqlite3.connect('/Users/aleksey/Documents/Untitled')
cursor = conn.cursor()
cursor.execute("SELECT * FROM NewTable;")
results = cursor.fetchall()
print(results)

def Sup(b):
    ff=soup.find_all(b)
    return ff
def Plo(c,i,b):
    for a in c:
        i = i+1
        cursor.execute("INSERT INTO NewTable (id, teg, text) VALUES (?, ?, ?);", (i, b, a.text))
        conn.commit()
    return i
def hol(results,i):
    for n in range(i):
        print(results[n])

soup = BeautifulSoup(src,"lxml")
conn.row_factory = sqlite3.Row
global ID
i=0
cursor.execute(f"SELECT COUNT(*) FROM NewTable;")
count = cursor.fetchone()[0]
if count == 0:
    i = 0
else:
    cursor.execute("SELECT id FROM NewTable ORDER BY id DESC LIMIT 1;")
    i = int(cursor.fetchall()[0][0])
m = input()
i = Plo(Sup(m),i,m)
cursor.execute("SELECT * FROM NewTable;")
results = cursor.fetchall()
hol(results,i)
print("Желаете очистить таблицу?(YES or NO)")
s = input()
if s == "YES":
    cursor.execute("DELETE FROM NewTable;")
    conn.commit()
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