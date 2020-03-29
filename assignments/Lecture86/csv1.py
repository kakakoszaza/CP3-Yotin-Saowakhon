import csv

def friendS():
    with open("myfriendS.csv", "w", newline="") as f:
        fw = csv.writer(f)
        fw.writerow(["Freinds Name","Favorite movie","Favorite Pet"])
        fw.writerow(["Sun","Avenger","Cat"])
        fw.writerow(["Mix","Harry Potter",'Cat'])
        fw.writerow(["Jay","SpiderMan","Dog"])
friendS()