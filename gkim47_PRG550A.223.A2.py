#!/home/pi/software/bin/python3


import cgi, cgitb
import subprocess


def piInfo():
   print(subprocess.check_output("date", shell=True, text=True))
   print("<br>")
   print("<br>")
   print(subprocess.check_output("ps ax | grep nginx", shell=True, text=True))
   print("<br>")
   print("<br>")
   print(subprocess.check_output("uname -a", shell=True, text=True))
   print("<br>")
   print("<br>")
   print(subprocess.check_output("cat /sys/class/net/eth0/address", shell=True, text=True))
   print("<br>")
   print("<br>")
   print(subprocess.check_output("cat /proc/cpuinfo | tail -5", shell=True, text=True))
   print("<br>")
   print("<br>")
   print(subprocess.check_output("ifconfig | grep netmask", shell=True, text=True))
   print("<br>")
   print("<br>")

def checker(cards_list):

   flag = 0

   list = {
      "2h": 3, "3h": 7, "4h": 10, "5h": 15, "6h": 19, "7h": 23, "8h": 27, "9h": 31, "th": 35, "jh": 39, "qh": 43,"kh": 47, "ah": 51,
      "2c": 1, "3c": 5, "4c": 9, "5c": 13, "6c": 17, "7c": 21, "8c": 25, "9c": 29, "tc": 33, "jc": 37, "qc": 41,"kc": 45, "ac": 49,
      "2s": 4, "3s": 8, "4s": 12, "5s": 16, "6s": 20, "7s": 24, "8s": 28, "9s": 32, "ts": 36, "js": 40, "qs": 44,"ks": 48, "as": 52,
      "2d": 2, "3d": 6, "4d": 11, "5d": 14, "6d": 18, "7d": 22, "8d": 26, "9d": 30, "td": 34, "jd": 38, "qd": 42,"kd": 46, "ad": 50
   }

   for check in cards_list:
      if check in list.keys():
         flag += 1
   if(flag == 5):

      return True

   else:
      print("<hr>")
      print("<p> ERROR ! You have to pick ONLY FIVE cards!!!</p>")

      return False

def findCategory(cards):

   category = ""
   container = []
   container_2 = []

   list_2 = {
      "2h": 3, "3h": 7, "4h": 10, "5h": 15, "6h": 19, "7h": 23, "8h": 27, "9h": 31, "th": 35, "jh": 39, "qh": 43,"kh": 47, "ah": 51,
      "2c": 1, "3c": 5, "4c": 9, "5c": 13, "6c": 17, "7c": 21, "8c": 25, "9c": 29, "tc": 33, "jc": 37, "qc": 41,"kc": 45, "ac": 49,
      "2s": 4, "3s": 8, "4s": 12, "5s": 16, "6s": 20, "7s": 24, "8s": 28, "9s": 32, "ts": 36, "js": 40, "qs": 44,"ks": 48, "as": 52,
      "2d": 2, "3d": 6, "4d": 11, "5d": 14, "6d": 18, "7d": 22, "8d": 26, "9d": 30, "td": 34, "jd": 38, "qd": 42,"kd": 46, "ad": 50
   }



   list_3 = {
      3: "2h", 7: "3h", 10: "4h", 15: "5h", 19: "6h", 23: "7h", 27: "8h", 31: "9h", 35: "th", 39: "jh", 43: "qh",
      47: "kh", 51: "ah",
      1: "2c", 5: "3c", 9: "4c", 13: "5c", 17: "6c", 21: "7c", 25: "8c", 29: "9c", 33: "tc", 37: "jc", 41: "qc",
      45: "kc", 49: "ac",
      4: "2s", 8: "3s", 12: "4s", 16: "5s", 20: "6s", 24: "7s", 28: "8s", 32: "9s", 36: "ts", 40: "js", 44: "qs",
      48: "ks", 52: "as",
      2: "2d", 6: "3d", 11: "4d", 14: "5d", 18: "6d", 22: "7d", 26: "8d", 30: "9d", 34: "td", 38: "jd", 42: "qd",
      46: "kd", 50: "ad",
   }


   list = {
      "HC" : "high card",
      "1P" : "1 pair",
      "2P" : "2 pair",
      "3K" : "3 of a kind",
      "ST" : "straight",
      "FL" : "flush",
      "FH" : "full house",
      "4K" : "4 of a kind",
      "SF" : "straight flush"
   }



   print(f"<p> Unordered cards : {cards} </p>")

   if checker(cards):

      if (isHighCard(cards)):

         category = "HC"

      if (isOnePair(cards)):

         category = "1P"

      if (isTwoPair(cards)):

         category = "2P"

      if (isThreeOfAKind(cards)):

         category = "3K"

      if (isStraight(cards)):

         category = "ST"

      if(isFlush(cards)):

         category = "FL"

      if(isFullHouse(cards)):

         category = "FH"

      if(isFourOfAKind(cards)):

         category = "4K"

      if(isStraightFlush(cards)):

         category = "SF"

      if category in list.keys():

         print("<br>")

         for unsored_cards in cards:

            container_2.append(list_2[unsored_cards])

         for ordered_cards in sorted(container_2):

            container.append(list_3[ordered_cards])

         printer(container)

         print(f"<p>Ordered cards: {container}</p>")

         print("<hr>")
         print(f'<p style = "color:blue; font-size: 60px;"> Your Poker Hand represents {list[category]}</p>')

      else:

         print("<p> No Matches were found! </p>")


def isHighCard(cards):

   if (isOnePair(cards)):
      return False

   if (isTwoPair(cards)):
      return False

   if (isThreeOfAKind(cards)):
      return False

   if (isStraight(cards)):
      return False

   if (isFlush(cards)):
      return False

   if (isFullHouse(cards)):
      return False

   if (isFourOfAKind(cards)):
      return False

   if (isStraightFlush(cards)):
      return False

   else:
      return True

def isOnePair(cards):

   flag = 0
   rank_List = []

   for rank in cards:
      rank_List.append(rank[0])

   for rank_check in rank_List:

      for rank_check_2 in rank_List:
         if(rank_check == rank_check_2):
            flag += 1

   if(int(flag) == 7):

      return True

   else:

      return False

def isTwoPair(cards):

   flag = 0
   rank_List = []

   for rank in cards:

      rank_List.append(rank[0])

   for rank_check in rank_List:

      for rank_check_2 in rank_List:

         if(rank_check == rank_check_2):

            flag += 1

   if(int(flag) == 9):

      return True

   else:

      return False


def isThreeOfAKind(cards):

   flag = 0
   rank_List = []

   for rank in cards:

      rank_List.append(rank[0])

   for rank_check in rank_List:

      for rank_check_2 in rank_List:

         if(rank_check == rank_check_2):

            flag += 1

   if(int(flag) == 11):

      return True

   else:

      return False


def isStraight(cards):

   tenAce = {
      "t" : 10,
      "j" : 11,
      "q" : 12,
      "k" : 13,
      "a" : 14
   }
   flag =0

   rank_List = []
   shape_List = []

   for rank in cards:

      if rank[0] in tenAce.keys():
         rank_List.append(int(tenAce[rank[0]]))
         shape_List.append(rank[1])
      else:
         rank_List.append(int(rank[0]))
         shape_List.append(rank[1])

   for shape_check in shape_List:

      for shape_check_2 in shape_List:

         if(shape_check == shape_check_2):

            flag += 1

   if (((max(rank_List)) - int(min(rank_List))) == 4) and (int(flag) < 25):
      return True
   else:
      return False

def isFlush(cards):

   tenAce = {
      "t" : 10,
      "j" : 11,
      "q" : 12,
      "k" : 13,
      "a" : 14
   }
   flag =0

   rank_List = []
   shape_List = []

   for rank in cards:

      if rank[0] in tenAce.keys():
         rank_List.append(int(tenAce[rank[0]]))
         shape_List.append(rank[1])
      else:
         rank_List.append(int(rank[0]))
         shape_List.append(rank[1])

   for shape_check in shape_List:

      for shape_check_2 in shape_List:

         if(shape_check == shape_check_2):

            flag += 1

   if (((max(rank_List)) - int(min(rank_List))) != 4) and (int(flag) >= 25):
      return True
   else:
      return False

def isFullHouse(cards):

   flag = 0
   rank_List = []


   for rank in cards:

      rank_List.append(rank[0])

   for rank_check in rank_List:

      for rank_check_2 in rank_List:

         if(rank_check == rank_check_2):

            flag += 1

   if(int(flag) == 13):

      return True

   else:

      return False


def isFourOfAKind(cards):

   flag = 0
   rank_List = []

   for rank in cards:

      rank_List.append(rank[0])

   for rank_check in rank_List:

      for rank_check_2 in rank_List:

         if(rank_check == rank_check_2):

            flag += 1

   if(int(flag) == 17):

      return True

   else:

      return False


def isStraightFlush(cards):


   tenAce = {
      "t" : 10,
      "j" : 11,
      "q" : 12,
      "k" : 13,
      "a" : 14
   }
   flag =0

   rank_List = []
   shape_List = []

   for rank in cards:

      if rank[0] in tenAce.keys():
         rank_List.append(int(tenAce[rank[0]]))
         shape_List.append(rank[1])
      else:
         rank_List.append(int(rank[0]))
         shape_List.append(rank[1])

   for shape_check in shape_List:

      for shape_check_2 in shape_List:

         if(shape_check == shape_check_2):

            flag += 1

   if (((max(rank_List)) - int(min(rank_List))) == 4) and (int(flag) == 25):
      return True
   else:
      return False


def printer(cards):
   str_1 = "<img src = '/../"
   str_2 = ".png' />"

   for p in cards:
      print(str_1+p+str_2)


cgitb.enable( )



form = cgi.FieldStorage( )
cards = form.getvalue('cards')

print("Content-type: text/html\n\n");

print("<html>\n")
print("<head>\n")
print("<title> check </title>\n")
print("</head>\n")
print("<body style = 'background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(149,199,20,1) 0%, rgba(0,212,255,1) 95%);'>\n")
findCategory(cards)
print("<hr>")
print("</body>\n")
print("</html>\n")

piInfo( )
