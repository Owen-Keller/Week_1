
"""
my modules to handle imports and special functions
Advanced computer lang
Owen Keller
"""

#imports
import random, math, csv,requests, alpha_vantage, datetime, re, os

import yfinance as yf

import pandas as pd


#Stocks
#NVDA   NVIDIA Corp
#AAPL   Apple  Corp
#AMZN   Amazon Inc
#KO     Coca-Cola Company
#TM     Toyota motor
#GE     General Electric

"""
class mid_module:

    def __init__(self):
        self.array = []


    # this function will be used in a general form
    def get_stock(self, url: str):
        try:
            r = requests.get(url)
            data = r.json()

            print(data)
        except:
            #Just dont run the code if any errors occur 
            pass

    def get_API(self, Path:str):

        try: 
            file = open(Path, 'r')
            return file.readline()
        
        except:
            #if it cant open the API file just return 1
            return 1
        
    def gen_API(self, Path : str):
        return "https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=" +self.get_API(Path)

        
mm = mid_module()

    print(mm.get_stock(mm.gen_API("/run/media/Atticus/Booger_Aids1/Shepherd_Semester_2/API_Key")))
"""

class mid_module:

    def __init__(self):
        self.array = ["NVDA","AAPL","AMZN","KO","TM","GE"]

    
    def rand_stock(self):
        rand = random.randint(0, (len(self.array) -1))

        return self.array[rand]
    
    def gen_Data(self):
        #Im making private functions for these specific data points
        def get_EndDate():
            return str(datetime.date.today())
    
        def get_StartDate( range : int):
            Start_Date = get_EndDate()
            month_Day = Start_Date[4:] 
            Start_Date = Start_Date[:4]

            New_Date = int(Start_Date) -range

            if New_Date < 2000:
                 return 1
            
            
            New_Date = str(New_Date)+ month_Day

            return New_Date
        
        tick = self.rand_stock() # Gets random stock that is wihin list
        start_Date = get_StartDate(random.randint(10, 20)) #gets a random start date between 10 - 20 years ago
        end_Date = get_EndDate() #current date

        data = yf.download(tick, start_Date, end_Date)

        return data

    
    def add_Stock(self, Stock: str):
        try:
            self.array.append(Stock)
        except(TypeError):
            print("invalid data type")


    #note this is not optimized and does not check on multiple runs, because the naming sense is random when generating the stock itself ie 
    #lets say I generate data from 2003 - 2025 AAPL vs 2014 - 2025 AAPl  therefore i get multiple loops because its re-rolling the data for one stock
    #that already exists

    def write_CSV(self):
        
        pattern = []
        name = []
        count = 0
        Fname = ""
        for _ in self.array:
            pattern.append(_)


        while True:
            if count == len(pattern):
                break

            csv_Data = self.gen_Data()
        
            for i in pattern:
                x = re.search(i, str(csv_Data))
                if x == None:
                    continue
                Fname = i+"-"+str(datetime.datetime.today())[:7]+".csv"

                if Fname not in name:
                    name.append(Fname)
                    count = len(name)
                    csv_Data.to_csv(Fname)
            

        
# calculate short-term trend using pandas 
    def calc_SMA50(self):
        short_W = 50
        







#As far as im aware Ascii art is open game (I pulled it from https://emojicombos.com/panda-ascii-art)

#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣆⠀⢀⣀⣀⣤⣤⣤⣦⣦⣤⣤⣄⣀⣀⠀⢠⣾⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⠟⠀⠀⠀⠀⠀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠘⣿⡿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⣠⣾⣿⣿⣟⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⣻⣿⣿⣦⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⡟⢠⣶⣾⣿⣿⣷⣤⢽⣿⣿⣿⣿⣿⡇⠀⠀⣀⣤⣿⣷⣴⣶⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣠⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠘⠻⣿⣿⣿⡿⠋⠀⢹⣿⣿⣿⣿⡇⠀⣿⣿⣿⡏⢹⣿⠉⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠹⣿⣿⠿⠋⠀⢤⣀⢀⣼⡄⠀⣠⠀⠈⠻⣿⣿⠟⠀⢸⣿⣇⣽⣿⠿⠿⠿⣿⣅⣽⣿⡇⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣟⠁⠀⠀⠀⠈⣿⣿⣿⡇
#       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛
#⠀⠀⠀⠀⠀⠀⠘⠛⠻⢿⣿⣿⣿⣿⣿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀