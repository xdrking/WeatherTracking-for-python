# importing module
from tkinter import *
from PIL import ImageTk, Image
import requests 
import tkinter as tk

# our necessary links
url ='https://api.openweathermap.org/data/2.5/weather'
api_key = '3b565b69f2e73f5d8bcf4efed1329231'
iconUrl = 'http://openweathermap.org/img/wn/{}@2x.png'

# this function is used for weather settings
def getWeather(city):
    params = {'q':city,'appid':api_key, 'lang':'tr'}
    data = requests.get(url,params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] -273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (city,country,temp,icon,condition)

# this function is used to output weather data    
def main():
    city = cityEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0],weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]    
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon

# creating tkinter window
app = Tk()
app.geometry('730x485')
app.resizable(width=False, height=False)
app.title('hava durumu')

# this function is used to get city information
def temp_text(e):
    cityEntry.delete(0, "end")



   
cityEntry = Entry(app,font=('inherit',30),justify='center')
cityEntry.insert(0, "Ara...")
cityEntry.pack(fill=BOTH, ipady=15,padx=15,pady=5)
cityEntry.bind("<FocusIn>", temp_text)




    
searchButton =Button(app, text='Arama',bg='white',font=('inherit' ,15),command=main,)
searchButton.pack(fill=BOTH, padx=20,pady=10)


    

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app,font=('inherit',40))
locationLabel.pack()

tempLabel = Label(app,font=('inherit',50, 'bold'))
tempLabel.pack()

conditionLabel = Label(app,font=('inherit',20))
conditionLabel.pack()

app.mainloop()

