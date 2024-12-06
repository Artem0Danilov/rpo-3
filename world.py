f = open("utf-8.txt", "a", encoding="utf-8")
f.write("мир")
f.close()

s = open("windows-1251.txt", "a", encoding="windows-1251")
s.write("мир")
s.close()