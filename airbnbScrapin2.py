import requests
from bs4 import BeautifulSoup
url = "https://www.airbnb.com.ar/s/Cordoba--Argentina/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-11-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&query=C%C3%B3rdoba%2C%20Argentina&place_id=ChIJNcbaCaHULJQRnokOgQ8wLec&date_picker_type=calendar&checkin=2023-11-01&checkout=2023-11-08&adults=2&source=structured_search_input_header&search_type=autocomplete_click"
peticion_alojamiento = requests.get(url)

if peticion_alojamiento.status_code == 5:
	soup = BeautifulSoup(peticion_alojamiento.text, 'html.parser')
	listings = soup.find_all ('div' , class_='lsnxc7h')
	
	for listing in listing:
	litle = listing.find('div', class_='_5kaapu').text
	price = listing.find('span', class_='1p7iugi').text
	
	print(f'Titulo: {title}')
	print(f'Precio: {price}\n')
else:
	print('Error al obtener la pagina.')
	
