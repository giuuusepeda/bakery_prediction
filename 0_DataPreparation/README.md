# Data Preparation

Here we have imported the provided dataset and performed various transformation on it.

## The Data Source

The datasets was provided by **Open Campus**. Initially we were given three csv files -

1.  The first file contains the sales data of the bakery from 01/07/2013 to 31/07/2018.
    [*umsatzdaten_gekuerzt.csv*](https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv)
2.  The weather file contains various weather data for the time period 01/01/2012 to 01/08/2019.
   [*wetter.csv*](https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/wetter.csv)
3. The KiWo file contains the dates for Kieler Woche event between the years 2012 and 2019, along with a flag variable.
   [*kiwo.csv*](https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/kiwo.csv)

The datasets are saved inside the **Raw** subfolder.

## Data Wrangling

- **Merging** - Imported everything in python and merged three datasets. Started with the *umsatz* table as the left table and joined the *wetter* and *kiwo* tables with it. So we ended up with a merged table that contained sales data with various weather codes and Kieler Woche dates.
- **Handling Missing Values/ Inputation** - some rows from the *wetter* csv file had some missing values for the fields "Bewoelkung", "Temperatur" and "Windgeschwindigkeit".We have replaced them with mean of the previous and the next day.
- **Creating row id** - every row has a unique id in the *YYMMDDWarengruppe* format.
- **Weather code** - Almost 100 numeric weather codes were condensed into 4 broad categories : *sunny, cloudy, rainy, thunderstorm*


### Time Intelligence

As the dataset contains dates, we have extracted multiple features from it. After converting the date filed into proper datetime format, we have extracted -

-  Week Number(Woche)
-  Month Number(Monat)
-  Weekday Number(Wochentag) -*Monday : 1...Sunday : 7*
-  Season Code(Jahreszeit) -*Winter : 1, Spring : 2, Summer : 3, Autumn : 4*
-  Flags for Hoilidays(Feiertag), School Holidays(Ferien) and Kieler Woche Days - 0/1 flags were added.

 **One-hot-encoding** - for easier anlysis by the ML algorithms,the relevant categorical variables weekday,month, season, warrengruppe.
- 
<style>
r { color: Red }
o { color: Orange }
g { color: Green }
</style>

<r>TODO:</r>

<o> 
Will be updated after further modifications

- Temperatur regarding seasons ?
- Rolling averages ?
- further

</o>
