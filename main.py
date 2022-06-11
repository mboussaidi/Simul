from datetime import datetime
from datetime import timedelta
from uuid import uuid4
import mysql.connector
from csv import DictReader



# Var values
dataFileName = 'ETH_Data_2.csv'
qt = 0
order_size = 100
cash = 10000
ref_price = 300
profit = 1.002


# Initialize database connection
cnx = mysql.connector.connect(user='root', password="Mahdi@2025", database='Boosterz')
cursor = cnx.cursor()


'''----------------------------
    DATABASE FUNCTIONS
----------------------------'''

def getLastCentralRow():
    sql = "SELECT * " \
          "FROM CentralTab " \
          "WHERE trNumber = (" \
          "SELECT MAX(trNumber) " \
          "FROM CentralTab)"

    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getLastDataBaseCash():
    sql = "SELECT actualCash, actualCoin " \
          "FROM CentralTab " \
          "WHERE trNumber = (" \
          "SELECT MAX(trNumber) " \
          "FROM CentralTab)"

    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def initDatabaseData(cash):
    print("# STARTING DATABASE INITIALISATION ... ")
    sql_1 = "TRUNCATE `Boosterz`.`CentralTab`"
    sql_2 = "TRUNCATE `Boosterz`.`BuyTab`"
    sql_3 = "TRUNCATE `Boosterz`.`SellTab`"
    sql_4 = ("INSERT INTO CentralTab (idCentralTab, date, symbol, amount, fayda, actualCash, actualCoin) VALUES ('" + str(uuid4()) + "', '" + str(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "', 'INIT', '0', '0', '" + str(cash) + "', '0')")

    cursor.execute(sql_1)
    cursor.execute(sql_2)
    cursor.execute(sql_3)
    cursor.execute(sql_4)
    cnx.commit()
    print("# DATABASE INITIALISATION FINISHED ")

def insertTransactionToBuyTab(idBuyTab, date, symbol, amount, bPrice, orderCoinQt, isAvailable):
    sql = ("INSERT INTO BuyTab (idBuyTab, date, symbol, amount, bPrice, orderCoinQt, isAvailable) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    sql_data = (idBuyTab, date, symbol, amount, bPrice, orderCoinQt, isAvailable)
    cursor.execute(sql, sql_data)
    cnx.commit()

def updateCentral(idCentralTab, date, symbol, amount, fayda, actualCash, actualCoin, action):
    sql = ("INSERT INTO CentralTab (idCentralTab, date, symbol, amount, fayda, actualCash, actualCoin, action) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    sql_data = (idCentralTab, date, symbol, amount, fayda, actualCash, actualCoin, action)
    cursor.execute(sql, sql_data)
    cnx.commit()

def getTransactionsToSell(profit, close):
    sql = "SELECT idBuyTab, bPrice, bPrice*" + str(profit) + " as sellingPrice " \
                                                       "FROM BuyTab " \
                                                       "WHERE isAvailable ='Y' and bPrice*" + str(profit) + " < " + str(close)

    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def insertTransactionToSellTab(idSellTab, date, symbol, amount, sPrice, bPrice, fayda, orderCoinQt, isAvailable):
    sql = ("INSERT INTO SellTab (idSellTab, date, symbol, amount, sPrice, bPrice, fayda, orderCoinQt, isAvailable) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

    sql_data = (idSellTab, date, symbol, amount, sPrice, bPrice, fayda, orderCoinQt, isAvailable)
    cursor.execute(sql, sql_data)
    cnx.commit()

def updateTrToBuyStatus(trId):
    sql = "UPDATE BuyTab SET isAvailable = 'N' WHERE idBuyTab = '" + trId + "'"
    cursor.execute(sql)
    cnx.commit()




# Clear all tables and set the amount of initial cash
initDatabaseData(cash)

# Reading data file
with open(dataFileName, 'r') as dataFile:

    csv_dict_reader = DictReader(dataFile)

    # iterating over each row
    for line in csv_dict_reader:

        fileTrDate = line['Date']
        fileTrOpen = float(line['Open'])
        fileTrClose = float(line['Close'])

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #               Buying Process
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        lastCentralRow = getLastDataBaseCash()
        dbActualCash = float(lastCentralRow[0][0])
        dbActualCoin = float(lastCentralRow[0][1])

        if dbActualCash > order_size and fileTrOpen > ref_price:

            # Then Buy

            idBuyTab = str(uuid4())
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            symbol = 'ETHUSD'
            amount = order_size
            bPrice = fileTrOpen
            orderCoinQt = order_size / fileTrOpen
            isAvailable = 'Y'

            newCashAfterBuy = dbActualCash - amount
            newCoinAfterBuy = dbActualCoin + orderCoinQt

            # Update Buy Table
            insertTransactionToBuyTab(idBuyTab, date, symbol, amount, bPrice, orderCoinQt, isAvailable)

            # Update Central Table
            updateCentral(idBuyTab, date, symbol, amount, '0', newCashAfterBuy, newCoinAfterBuy, 'B')

            print("Buying "+str(orderCoinQt)+ " \t"+ symbol +" at "+str(bPrice) + "\t   - -    ACTUAL CASH : "+str(newCashAfterBuy))

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #               Selling Process
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        lastCentralRow = getLastDataBaseCash()
        dbActualCash = float(lastCentralRow[0][0])
        dbActualCoin = float(lastCentralRow[0][1])

        # Get all ready transactions to be sell
        preparedTrToSell = getTransactionsToSell(profit, fileTrClose)

        #print("LEN : " + str(len(preparedTrToSell)))

        if dbActualCoin > 0 and len(preparedTrToSell) > 0:

            # print(preparedTrToSell)
            for trToSell in preparedTrToSell:
                #print(trToSell)
                trId = trToSell[0]
                trPrice = float(trToSell[1])
                sellingPrice = float(trToSell[2])

                if trPrice < fileTrClose:
                    # Then Sell

                    idSellTab = str(uuid4())
                    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    symbol = 'ETHUSD'
                    amount = order_size
                    sPrice = fileTrClose
                    bPrice = trPrice
                    fayda = sPrice - bPrice
                    orderCoinQtToSell = order_size / bPrice
                    isAvailable = 'N'

                    newCashAfterSell = dbActualCash + sPrice
                    newCoinAfterSell = dbActualCoin - orderCoinQtToSell

                    # Update Sell Table
                    insertTransactionToSellTab(idSellTab, date, symbol, amount, sPrice, bPrice, fayda, orderCoinQtToSell, isAvailable)

                    # Update BuyTable - set transaction isAvailable = 'N'
                    updateTrToBuyStatus(trId)

                    # Update Central Table
                    updateCentral(idSellTab, date, symbol, amount, fayda, newCashAfterSell, newCoinAfterSell, 'S')

                    print("Selling " + str(orderCoinQtToSell) + " \t" + symbol + " at " + str(sPrice) + "\t   - -    ACTUAL CASH : " + str(newCashAfterSell))

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



#  CLOSE DB CONNECTION
cnx.close()

