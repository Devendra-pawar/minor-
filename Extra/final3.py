# importing required libraries
import requests 
from bs4 import BeautifulSoup
from csv import writer
import openpyxl
import pandas

a = ["tata","kia","volkswagen","skoda","jaguar","renault","jeep","volvo","Nissan","Lamborghini"]
# a=["Lamborghini"]
for brand_name in a:
    url2 = "https://www.cartrade.com/"+ brand_name + "-cars/"
    print(f'This is the website: {url2}')

    r = requests.get(url2)
    r.status_code

    soup = BeautifulSoup(r.content,'html.parser')



    link1 = "carBrands_list"
    cars = soup.find_all('div', class_=link1)
    # cars
    len(cars)


    c = []
    for name in cars:  
      a = name.find("div", class_="makeblktlt")
   
      if a != None:
        b = a.get_text()
        # print(b)
        if b != None:
           c.append(b)
    print(c)
    print("This are the names of all models")



        # converting into csv
    with open("Model_name.csv","w",encoding="utf8", newline="")as file:
     Writer = writer(file)
     header = ["Model name:"]
     Writer.writerow(header)
    #  for i in names :
    #       Writer.writerow(i)
     Writer.writerow(c)

    print("All model name are in Model_name.csv file")
    ####################################################
    x = []
    for dif in c:
        dif = dif.split()
        x.append(dif)
    print(x," here")

    ###################################
    for model_name in x:
        url3 = ("https://www.cartrade.com/"+'tata'+"-cars/"+model_name[1]+"/")
        # print(url3)
        # print(model_name)

        r = requests.get(url3)
        r.status_code



        soup = BeautifulSoup(r.content,'html.parser')

        link3 = "keySpecsBody"
        cars = soup.find('tbody', class_=link3).find_all('tr')
        # cars = soup.find('tbody', class_=link3)
        # print(cars)


        # cars
        ##len(cars)


        if cars != None :
        
            # Car_Name         = Brand_name +" "+ Model_name
            Car_Name = model_name[1]
            Price            = cars[0].find("td").get_text()
            Fuel_Type        = cars[1].find("td").get_text()
            Seating_Capacity = cars[2].find("td").get_text()
            Safety_Rating    = cars[3].find("td").get_text()
            Warranty         = cars[4].find("td").get_text()
            Engine_Size      = cars[5].find("td").get_text()
            Transmission     = cars[6].find("td").get_text()
            Size             = cars[7].find("td").get_text()
            Fuel_Tank        = cars[8].find("td").get_text()
            Ground_Clearance = cars[9].find("td").get_text()

            Info =[Car_Name,Price,Fuel_Type,Seating_Capacity,Safety_Rating,Warranty,Engine_Size,Transmission,Size,Fuel_Tank,Ground_Clearance]
        
            print('done')
          # print(Car_Name)   
          # print(price) 
    #     print(fuel_type)   
            print(Info)


        # with open("Car_Details.csv","w",encoding="utf8", newline="")as file:
        #         Writer = writer(file)
        #         header = ["Car_Name","Price","Fuel_Type","Seating_Capacity","Safety_Rating","Warranty","Engine_Size","Transmission","Size","Fuel_Tank","Ground_Clearance"]
        #         Writer.writerow(header)
            Writer.writerow(Info)