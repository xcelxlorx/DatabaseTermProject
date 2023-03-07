from django.shortcuts import render
from django.db import connection
from .forms import *
from .models import *

def displayBasic(request):
    return render(request, 'myApp/index.html', {})

def displayCreate(request):
    outputProduct = []
    outputPc = []
    outputLaptop = []
    outputPrinter = []
    outputProduct2 = []
    outputPc2 = []
    outputLaptop2 = []
    outputPrinter2 = []
    with connection.cursor() as cursor:
        sqlQueryProduct = "CREATE TABLE Product (maker CHAR(100), model INT(11) NOT NULL, type CHAR(100), PRIMARY KEY (model));"
        cursor.execute(sqlQueryProduct)
        fetchResultProduct = cursor.fetchall()

        sqlQueryPc = "CREATE TABLE PC (model INT(11) NOT NULL, speed FLOAT, ram INT(11), hd INT(11), price INT(11), PRIMARY KEY (model));"
        cursor.execute(sqlQueryPc)
        fetchResultPc = cursor.fetchall()

        sqlQueryLaptop = "CREATE TABLE Laptop (model INT(11) NOT NULL, speed FLOAT, ram INT(11), hd INT(11), screen FLOAT, price INT(11), PRIMARY KEY (model));"
        cursor.execute(sqlQueryLaptop)
        fetchResultLaptop = cursor.fetchall()

        sqlQueryPrinter = "CREATE TABLE Printer (model INT NOT NULL, color TINYINT(1), type CHAR(100), price INT(11), PRIMARY KEY (model));"
        cursor.execute(sqlQueryPrinter)
        fetchResultPrinter = cursor.fetchall()

        sqlQueryProduct2 = "SELECT maker, model, type FROM Product;"
        cursor.execute(sqlQueryProduct2)
        fetchResultProduct2 = cursor.fetchall()

        sqlQueryPc2 = "SELECT model, speed, ram, hd, price FROM PC;"
        cursor.execute(sqlQueryPc2)
        fetchResultPc2 = cursor.fetchall()

        sqlQueryLaptop2 = "SELECT model, speed, ram, hd, screen, price FROM Laptop;"
        cursor.execute(sqlQueryLaptop2)
        fetchResultLaptop2 = cursor.fetchall()

        sqlQueryPrinter2 = "SELECT model, color, type, price FROM Printer;"
        cursor.execute(sqlQueryPrinter2)
        fetchResultPrinter2 = cursor.fetchall()

        for temp in fetchResultProduct:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputProduct.append(eachRow)

        for temp in fetchResultPc:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputPc.append(eachRow)

        for temp in fetchResultLaptop:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4],
                       'price': temp[5]}
            outputLaptop.append(eachRow)

        for temp in fetchResultPrinter:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputPrinter.append(eachRow)

        for temp in fetchResultProduct2:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputProduct2.append(eachRow)

        for temp in fetchResultPc2:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputPc2.append(eachRow)

        for temp in fetchResultLaptop2:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4],
                       'price': temp[5]}
            outputLaptop2.append(eachRow)

        for temp in fetchResultPrinter2:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputPrinter2.append(eachRow)

    return render(request, 'myApp/create.html',
              {"Product": outputProduct2, "Pc": outputPc2, "Laptop": outputLaptop2, "Printer": outputPrinter2})

def displayInsert(request):
    outputProduct = []
    outputPc = []
    outputLaptop = []
    outputPrinter = []
    outputProduct2 = []
    outputPc2 = []
    outputLaptop2 = []
    outputPrinter2 = []
    with connection.cursor() as cursor:
        sqlQueryProduct = "INSERT INTO Product (maker, model, type) VALUES ('A', 1001, 'pc'),('A', 1002, 'pc'),('A', 1003, 'pc'),('A', 2004, 'laptop')," \
                          "('A', 2005, 'laptop'),('A', 2006, 'laptop'),('B', 1004, 'pc'),('B', 1005, 'pc'),('B', 1006, 'pc'),('B', 2007, 'laptop')," \
                          "('C', 1007, 'pc'),('D', 1008, 'pc'),('D', 1009, 'pc'),('D', 1010, 'pc'),('D', 3004, 'printer'),('E', 3005, 'printer')," \
                          "('E', 1011, 'pc'),('E', 1012, 'pc'),('E', 1013, 'pc'),('E', 2001, 'laptop'),('E', 2002, 'laptop'),('E', 2003, 'laptop')," \
                          "('E', 3001, 'printer'),('E', 3002, 'printer'),('E', 3003, 'printer'),('F', 2008, 'laptop'),('F', 2009, 'laptop')," \
                          "('G', 2010, 'laptop'),('H', 3006, 'printer'),('H', 3007, 'printer');"
        cursor.execute(sqlQueryProduct)
        fetchResultProduct = cursor.fetchall()

        sqlQueryPc = "INSERT INTO PC (model, speed, ram, hd, price) VALUES (1001, 2.66, 1024, 250, 2114),(1002, 2.10, 512, 250, 995),(1003, 1.42, 512, 80, 478)," \
                     "(1004, 2.80, 1024, 250, 649),(1005, 3.20, 512, 250, 630),(1006, 3.20, 1024, 320, 1049),(1007, 2.20, 1024, 200, 510),(1008, 2.20, 2048, 250, 770)," \
                     "(1009, 2.00, 1024, 250, 650),(1010, 2.80, 2048, 300, 770),(1011, 1.86, 2048, 160, 959),(1012, 2.80, 1024, 160, 649)," \
                     "(1013, 3.06, 512, 80, 529);"
        cursor.execute(sqlQueryPc)
        fetchResultPc = cursor.fetchall()

        sqlQueryLaptop = "INSERT INTO Laptop (model, speed, ram, hd, screen, price) VALUES (2001, 2.00, 2048, 240, 20.1, 3673),(2002, 1.73, 1024, 80, 17.0, 949)," \
                         "(2003, 1.80, 512, 60, 15.4, 549),(2004, 2.00, 512, 60, 13.3, 1150),(2005, 2.16, 1024, 120, 17.0, 2500),(2006, 2.00, 2048, 80, 15.4, 1700)," \
                         "(2007, 1.83, 1024, 120, 13.3, 1429),(2008, 1.60, 1024, 100, 15.4, 900),(2009, 1.60, 512, 80, 14.1, 680), (2010, 2.00, 2048, 160, 15.4, 2300);"
        cursor.execute(sqlQueryLaptop)
        fetchResultLaptop = cursor.fetchall()

        sqlQueryPrinter = "INSERT INTO Printer (model, color, type, price) VALUES (3001, true, 'ink-jet', 99),(3002, false, 'laser', 239),(3003, true, 'laser', 899),(3004, true, 'ink-jet', 120)," \
                          "(3005, false, 'laser', 120), (3006, true, 'ink-jet', 100), (3007, true, 'laser', 200);"
        cursor.execute(sqlQueryPrinter)
        fetchResultPrinter = cursor.fetchall()

        sqlQueryProduct2 = "SELECT maker, model, type FROM Product;"
        cursor.execute(sqlQueryProduct2)
        fetchResultProduct2 = cursor.fetchall()

        sqlQueryPc2 = "SELECT model, speed, ram, hd, price FROM PC;"
        cursor.execute(sqlQueryPc2)
        fetchResultPc2 = cursor.fetchall()

        sqlQueryLaptop2 = "SELECT model, speed, ram, hd, screen, price FROM Laptop;"
        cursor.execute(sqlQueryLaptop2)
        fetchResultLaptop2 = cursor.fetchall()

        sqlQueryPrinter2 = "SELECT model, color, type, price FROM Printer;"
        cursor.execute(sqlQueryPrinter2)
        fetchResultPrinter2 = cursor.fetchall()

        for temp in fetchResultProduct:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputProduct.append(eachRow)

        for temp in fetchResultPc:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputPc.append(eachRow)

        for temp in fetchResultLaptop:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4],
                       'price': temp[5]}
            outputLaptop.append(eachRow)

        for temp in fetchResultPrinter:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputPrinter.append(eachRow)

        for temp in fetchResultProduct2:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputProduct2.append(eachRow)

        for temp in fetchResultPc2:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputPc2.append(eachRow)

        for temp in fetchResultLaptop2:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4],
                       'price': temp[5]}
            outputLaptop2.append(eachRow)

        for temp in fetchResultPrinter2:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputPrinter2.append(eachRow)

    return render(request, 'myApp/create.html',
                  {"Product": outputProduct2, "Pc": outputPc2, "Laptop": outputLaptop2, "Printer": outputPrinter2})

def displayDrop(request) :
    outputProduct = []
    outputPc = []
    outputLaptop = []
    outputPrinter = []

    with connection.cursor() as cursor:
        sqlQueryProduct = "drop table product;"
        cursor.execute(sqlQueryProduct)
        fetchResultProduct = cursor.fetchall()

        sqlQueryPc = "drop table pc;"
        cursor.execute(sqlQueryPc)
        fetchResultPc = cursor.fetchall()

        sqlQueryLaptop = "drop table laptop;"
        cursor.execute(sqlQueryLaptop)
        fetchResultLaptop = cursor.fetchall()

        sqlQueryPrinter = "drop table printer;"
        cursor.execute(sqlQueryPrinter)
        fetchResultPrinter = cursor.fetchall()

        for temp in fetchResultProduct:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputProduct.append(eachRow)

        for temp in fetchResultPc:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputPc.append(eachRow)

        for temp in fetchResultLaptop:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4],
                       'price': temp[5]}
            outputLaptop.append(eachRow)

        for temp in fetchResultPrinter:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputPrinter.append(eachRow)

    return render(request, 'myApp/create.html',
              {"Product": outputProduct, "Pc": outputPc, "Laptop": outputLaptop, "Printer": outputPrinter})

def display(request) :
    outputProduct = []
    outputPc = []
    outputLaptop = []
    outputPrinter = []
    outputOfQuery1 = []
    outputOfQuery2 = []
    outputOfQuery3 = []
    outputOfQuery4 = []

    with connection.cursor() as cursor:
        sqlQuery1 = "SELECT AVG(PC.hd) FROM PC;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()

        sqlQuery2 = "SELECT product.maker, AVG(laptop.speed) FROM laptop, product where laptop.model = product.model " \
                    "AND product.type = 'laptop' group by product.maker ORDER BY maker ASC; SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));"
        cursor.execute(sqlQuery2)
        fetchResultQuery2 = cursor.fetchall()

        sqlQuery3 = " SELECT product.maker, laptop.price FROM product, laptop where product.model = laptop.model GROUP BY product.maker " \
                    "having count(laptop.model) = 1 ORDER BY maker ASC;"
        cursor.execute(sqlQuery3)
        fetchResultQuery3 = cursor.fetchall()

        sqlQuery4 = "select product.maker, printer.model, max(price) from product, printer " \
                    "where printer.model=product.model group by product.maker ORDER BY maker ASC;"
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery1:
            eachRow = {'AVG': temp[0]}
            outputOfQuery1.append(eachRow)

        for temp in fetchResultQuery2:
            eachRow = {'maker': temp[0], 'AVG': temp[1]}
            outputOfQuery2.append(eachRow)

        for temp in fetchResultQuery3:
            eachRow = {'maker': temp[0], 'price': temp[1]}
            outputOfQuery3.append(eachRow)

        for temp in fetchResultQuery4:
            eachRow = {'maker': temp[0], 'model': temp[1], 'max': temp[2]}
            outputOfQuery4.append(eachRow)

    return render(request, 'myApp/query.html', {"Product": outputProduct, "Pc": outputPc, "Laptop": outputLaptop, "Printer": outputPrinter,
                                                "output1": outputOfQuery1, "output2": outputOfQuery2, "output3": outputOfQuery3, "output4": outputOfQuery4})
