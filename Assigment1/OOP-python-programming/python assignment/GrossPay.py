import re


def Grosspay(Hours,rate):
   Total_amount=Hours*rate
   return Total_amount

Hours=int(input("Enter your Working Hours: "))
rate=float(input("Enter your Rate of payment: "))
print("GrossPay: ", Grosspay(Hours,rate))
