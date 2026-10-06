#country api

from tkinter import*
import requests
import json



root = Tk()
root.title("Capital City APP")
root.config(bg="Light Yellow")
root.geometry("600x600")

#title and city
title = Label(root,text="Capital City APP",font=('Helvetica',24,'bold'),bg="Light Yellow")
title.place(relx=0.3,rely=0.1,anchor=CENTER)

city_label = Label(root,text="Enter the city name: ")
city_label.place(relx=0.1,rely=0.2,anchor=CENTER)

city_entry = Entry(root)
city_entry.place(relx=0.35,rely=0.2,anchor=CENTER)

#data labels
country_label = Label(root,text="Country: ")
country_label.place(relx=0.1,rely=0.3,anchor=CENTER)

region_label = Label(root,text="Region: ")
region_label.place(relx=0.1,rely=0.4,anchor=CENTER)

language_label = Label(root,text="Language: ")
language_label.place(relx=0.1,rely=0.5,anchor=CENTER)

population_label = Label(root,text="Population: ")
population_label.place(relx=0.1,rely=0.6,anchor=CENTER)

area_label = Label(root,text="Area: ")
area_label.place(relx=0.1,rely=0.7,anchor=CENTER)

#data entries
country_data = Label(root)
country_data.place(relx=0.3,rely=0.3,anchor=CENTER)

region_data = Label(root)
region_data.place(relx=0.3,rely=0.4,anchor=CENTER)

language_data = Label(root)
language_data.place(relx=0.3,rely=0.5,anchor=CENTER)

population_data = Label(root)
population_data.place(relx=0.3,rely=0.6,anchor=CENTER)

area_data = Label(root)
area_data.place(relx=0.3,rely=0.7,anchor=CENTER)

#function

def cityDetails():
    try: 
        api_request = requests.get("https://restcountries.com/v3.1/capital/"+ city_entry.get())
        api_output_json = api_request.json()
        country = api_output_json[0]['name']['common']
        region = api_output_json[0]['region']
        language = list(api_output_json[0]['languages'].values())[0]
        population = api_output_json[0]['population']
        country_area = api_output_json[0]['area']
        country_data["text"]=country
        region_data["text"]=region
        language_data["text"]=language
        population_data["text"]=population
        area_data["text"]=country_area
    except Exception as e:
        country_data["text"]="Invalid Name"
        region_data["text"]=""
        language_data["text"]=""
        population_data["text"]=""
        area_data["text"]=""

#button
city_button = Button(root,text="Find City Details",command=cityDetails)
city_button.place(relx=0.2,rely=0.8,anchor=CENTER)



root.mainloop()



#homework: revise all the topics for next week