from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("fare6.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        print(Journey_day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # printS("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_Min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        Duration_hour = abs(Arrival_hour - Dep_hour)
        Duration_mins = abs(Arrival_min - Dep_Min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        Airline=request.form['airline']
        if(Airline=='Air Asia'):
            Air_Asia=1
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
             


        elif(Airline=='Air India'):
            Air_Asia=0
            Air_India=1
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0

        elif (Airline=='GoAir'):
            Air_Asia=0
            Air_India=0
            GoAir=1
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0

        elif (Airline=='IndiGo'):
            Air_Asia=0
            Air_India=0
            GoAir=0
            IndiGo=1
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0
            
        elif (Airline=='Jet Airways'):
            Air_Asia=0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 1
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0
            
        elif (Airline=='Jet Airways Business'):
            Air_Asia=0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=1
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0
            
        elif (Airline=='Multiple Carriers'):
            Air_Asia=0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 1
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0

        elif (Airline=='Multiple Carriers Permium economy'):
            Air_Asia=0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 1
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0

        elif (Airline=='SpiceJet'):
            Air_Asia=0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 1
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0

        elif (Airline=='Trujet'):
            Air_Asia=0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 1
            Vistara = 0
            Vistara_Premium_economy =0

        elif (Airline=='Vistara'):
            Air_Asia= 0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 1
            Vistara_Premium_economy =0
            
        elif (Airline=='Vistara Premium economy'):
            Air_Asia= 0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =1

        else:
            Air_Asia=0
            Air_India=0
            GoAir=0
            IndiGo=0
            Jet_Airways = 0
            Jet_Airways_Business=0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy =0

       

        # Source
       
        Source = request.form["Source"]


        if (Source == 'Banglore'):
            Source_Banglore = 1
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
           

        elif (Source == 'Chennai'):
         
            Source_Banglore = 0
            Source_Chennai = 1
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
           
        elif (Source == 'Delhi'):
            Source_Banglore = 1
            Source_Chennai = 0
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
           
        elif (Source == 'Kolkata'):
          
            Source_Banglore = 0
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
           
        
        elif (Source == 'Mumbai'):
          
            Source_Banglore = 0
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
           
        else:
            
            Source_Banglore = 0
            Source_Chennai = 0
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
           

        

        # Destination
        # Banglore = 0 (not in column)
        Destination = request.form["Destination"]
    
        
        if (Destination== 'Banglore'):
            d_Banglore=1
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi=0
            
            

        elif (Destination == 'Cochin'):
            d_Banglore=0
            d_Cochin = 1
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi=0

        elif (Destination== 'Delhi'):
            d_Banglore=0
            d_Cochin = 0
            d_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi=0

        elif (Destination == 'Hyderabad'):
            d_Banglore=0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
            d_New_Delhi=0


        elif (Destination == 'Kolkata'):
            d_Banglore=0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
            d_New_Delhi=0
    
      
        elif (Destination == 'New Delhi'):
            d_Banglore=0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi=1
        else:
            d_Banglore=0
            d_Cochin = 0
            d_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_New_Delhi=0

        
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_Min,
            Arrival_hour,
            Arrival_min,
            Duration_hour,
            Duration_mins,
            Air_Asia,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Source_Banglore,
            Source_Chennai,
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            d_Banglore,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)

