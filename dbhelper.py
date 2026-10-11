import pymysql
import streamlit as st




class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='848163', # your password
                database='dsmp'
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except:
            print('Connection error')

    def fetch_source(self):
        source_city = []
        self.mycursor.execute('SELECT DISTINCT(Source) FROM flight;')
        data = self.mycursor.fetchall()
        for i in data:
             source_city.append(i[0])
        return source_city

    def fetch_destination(self):
        destination_city = []
        self.mycursor.execute('SELECT DISTINCT(Destination) FROM flight')
        data = self.mycursor.fetchall()
        for i in data:
            destination_city.append(i[0])
        return destination_city

    def fetch_all_flight(self,source , destination ):


        query = """
        SELECT Airline,Date_of_Journey,Source,Destination,Route,Price
        FROM flight WHERE Source = %s AND Destination = %s
        """
        self.mycursor.execute(query,(source,destination))
        data = self.mycursor.fetchall()
        return data



    def fetch_airline(self):
        airline = []
        query = "SELECT distinct(Airline)FROM flight"
        self.mycursor.execute(query)
        data= self.mycursor.fetchall()

        for i in data:
            airline.append(i[0])
        return airline

    def date_vs_price(self, source, destination, airline):
        date = []
        price = []
        self.mycursor.execute("""
           SELECT 
           Date_of_Journey,
           AVG(Price) AS Avg_Price
           FROM flight
           WHERE source = '{}' 
           AND destination = '{}'
           AND Airline = '{}'
           GROUP BY Date_of_Journey
           ORDER BY STR_TO_DATE(Date_of_Journey, '%d-%m-%Y');
           """.format(source, destination, airline))
        data = self.mycursor.fetchall()
        for i in data:
            date.append(i[0])
            price.append(i[1])
        return date, price



    def fetch_airline_frequency(self):
        airline = []
        frequency = []

        self.mycursor.execute("""
                    SELECT Airline,COUNT(*) FROM flight
                    GROUP BY Airline
                    """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        city = []
        frequency = []

        self.mycursor.execute("""
                    SELECT Source,COUNT(*) FROM (SELECT Source FROM flight
            							UNION ALL
            							SELECT Destination FROM flight) t
                    GROUP BY t.Source
                    ORDER BY COUNT(*) DESC
                    """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency



    def daily_frequency(self):
        date = []
        frequency = []

        self.mycursor.execute("""
                    SELECT Date_of_Journey,COUNT(*) FROM flight
                    GROUP BY Date_of_Journey
                    """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency



    def total_flight(self):
        x=[]
        self.mycursor.execute('SELECT COUNT(*) AS total_flights FROM flight')
        data = self.mycursor.fetchall()
        for i in data:
            x.append(i[0])
        return x[0]

    def dashboard_kpis(self):

        self.mycursor.execute("SELECT COUNT(DISTINCT Airline) FROM flight")
        total_airlines = self.mycursor.fetchone()[0]

        self.mycursor.execute("""
            SELECT COUNT(DISTINCT city)
            FROM
            (
                SELECT Source AS city FROM flight
                UNION
                SELECT Destination AS city FROM flight
            ) AS cities
        """)
        total_cities = self.mycursor.fetchone()[0]

        self.mycursor.execute("SELECT ROUND(AVG(Price),2) FROM flight")
        avg_price = self.mycursor.fetchone()[0]

        return total_airlines, total_cities, avg_price






db = DB()
