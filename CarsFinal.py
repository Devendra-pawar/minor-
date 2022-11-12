# importing required libraries
import requests 
from bs4 import BeautifulSoup
from csv import writer
import pandas

# Selected Brands Name
a = ["Tata","Kia","Volkswagen","Skoda","Jaguar","Renault","Jeep","Volvo","Nissan","Lamborghini","Porsche","MINI","Citroen","Maserati","Bentley","McLaren"]


with open("CarsFinal.csv","w",encoding="utf8", newline="")as file:
    Writer = writer(file)
    header = ["Brand_Name","Model_Name","Price","Fuel_Type","Mileage","Seating_Capacity","Safety_Rating","Warranty","Engine_Size","Transmission","Size","Fuel_Tank"]
    Writer.writerow(header)

    for Brand_name in a:
        # Store website in a variable
        url2 = "https://www.cartrade.com/"+ Brand_name + "-cars/"
        print(f'This is the website: {url2}')
        
        # HTTP request
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
        
        
        x = []
        for dif in c:
            dif = dif.split()
            x.append(dif)
        print(x," here")

        
        for model_name in x:
            url3 = ("https://www.cartrade.com/"+Brand_name+"-cars/"+model_name[1]+"/")
            # print(url3)
            # print(model_name)

            r = requests.get(url3)
            r.status_code

            soup = BeautifulSoup(r.content,'html.parser')

            link3 = "keySpecsBody"
            cars = soup.find('tbody', class_=link3).find_all('tr')
            # cars = soup.find('tbody', class_=link3)
            # print(cars)

            if cars != None :
                        
                Brand_Name       = Brand_name
                Model_Name       = model_name[1]
                Price            = cars[0].find("td").get_text()
                Fuel_Type        = cars[1].find("td").get_text()
                Mileage          = cars[2].find("td").get_text()
                Seating_Capacity = cars[3].find("td").get_text()
                Safety_Rating    = cars[4].find("td").get_text()
                Warranty         = cars[5].find("td").get_text()
                Engine_Size      = cars[6].find("td").get_text()
                Transmission     = cars[7].find("td").get_text()
                Size             = cars[8].find("td").get_text()
                Fuel_Tank        = cars[9].find("td").get_text()

                Info =[Brand_Name,Model_Name,Price,Fuel_Type,Mileage,Seating_Capacity,Safety_Rating,Warranty,Engine_Size,Transmission,Size,Fuel_Tank]
        
                print('done')  
                print(Info)

                Writer.writerow(Info)
print("Done")