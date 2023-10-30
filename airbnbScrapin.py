	
import requests
from bs4 import BeautifulSoup
import mysql as pd

def get_airbnb(URL):https://www.airbnb.com.ar/s/Cordoba--Argentina/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-11-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&query=C%C3%B3rdoba%2C%20Argentina&place_id=ChIJNcbaCaHULJQRnokOgQ8wLec&date_picker_type=calendar&checkin=2023-11-01&checkout=2023-11-08&adults=2&source=structured_search_input_header&search_type=autocomplete_click
    # Cordoba -- Argentina
    Cordoba = URL.split("-")[2].split("_")[0]
    # Connection
    peticion_restaurantes = requests.get(URL)
    textourl = peticion_restaurantes.text # is a string that contains the web page source
    # Connection ok
    if peticion_alojamiento.status_code == 200:
        
        # Beautiful soup object
        soup = BeautifulSoup(textourl,"lxml") 
        
        # Initialize empty lists
        name = []
        position = []
        rating = []
        numReview = []
        usd = []
        food = []
        
        # Only look for info in bock with class shortSellDetails
        for sec in soup.find_all(class_="shortSellDetails"):
            
            # Avoid sponsored restaurants
            patro = sec.find(class_="ui_merchandising_pill")
        
            if(patro == None):
                # position
                if sec.find(class_="popIndex rebrand popIndexDefault") is not None:
                    pos = sec.find(class_="popIndex rebrand popIndexDefault").get_text(strip=True) # extract
                    pos = int(pos.split(" de ")[0].replace(".", "")) # processing
                else:
                    pos=""
                position.append(pos) # append
            
                # alojamiento name
                nam = sec.find(class_="property_title").get_text(strip=True) # extract
                name.append(nam)      
         
        
                # rating
                if sec.find(class_="ui_bubble_rating") is not None:
                    rate = sec.find(class_="ui_bubble_rating").get("alt") # extract
                    rate = float(rate.split(" de ")[0].replace(",","."))  # processing
                else:
                    rate = 0
                rating.append(rate)
            
                # number or reviews
                if sec.find(class_="reviewCount") is not None:
                    reviews = sec.find(class_="reviewCount").get_text(strip=True) # extract
                    reviews = int(reviews.replace("opiniones", "").replace("opinión","").replace(".", ""))  # processing
                else:
                    reviews = 0
                numReview.append(reviews)                
                     
                # euroscategory
                if sec.find(class_="item price") is not None:
                    price = sec.find(class_="item price").get_text(strip=True)  
                else:
                    price = " "
                euros.append(price)
            
                # food category
                typefood = [secfood.get_text() for secfood in sec.find_all(class_="item cuisine")] # extract
                typefood = ','.join(typefood) # processing
                food.append(typefood)      
          
            
                df = pd.DataFrame({'restaurants':name,"ratings":rating,"number_reviews":numReview, "price_category":euros,
                          'food_category':food,},
                         columns = ["restaurants","ratings","number_reviews","price_category","food_category"], index = position)
                df.index.name = nameCity
        return(df)       
    else:
        return(pd.DataFrame())