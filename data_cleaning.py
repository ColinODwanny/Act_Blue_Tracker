import pandas as pd
import plotly.express as px

#returns a list.  index 0 is the daily DataFrame, index 1 is the monthly DataFrame
def read_and_clean():

    #loading and making data useable

    masterDF = pd.read_csv("ActBlue.csv")
    masterDF['Datetime'] = pd.to_datetime(masterDF['Datetime'], utc=True)

    #aggrigating data by each day to then find daily fundrasing totals

    masterDF['day'] = masterDF['Datetime'].dt.date
    dailyMinDF = masterDF.groupby('day').min()
    dailyMaxDF = masterDF.groupby('day').max()
    #changed ' Amount' to 'Amount' in next two lines
    dailyMinDF.rename(columns = {'Amount':'daily_min'}, inplace = True)
    dailyMaxDF.rename(columns = {'Amount':'daily_max'}, inplace = True)
    dailyMinMax = pd.DataFrame(data = [dailyMaxDF['daily_max'], dailyMinDF['daily_min']])
    dailyMinMax = dailyMinMax.transpose()
    dailyMinMax['daily_total'] = dailyMinMax['daily_max'] - dailyMinMax['daily_min']
    dailyMinMax['day'] = dailyMinMax.index

    #using same methodology to find monthly totals

    masterDF['month'] = masterDF['Datetime'].dt.month
    monthlyMinDF = masterDF.groupby('month').min()
    monthlyMaxDF = masterDF.groupby('month').max()
    #changed ' Amount' to 'Amount in next two lines
    monthlyMinDF.rename(columns = {'Amount':'monthly_min'}, inplace = True)
    monthlyMaxDF.rename(columns = {'Amount':'monthly_max'}, inplace = True)
    monthlyMinMax = pd.DataFrame(data = [monthlyMaxDF[ 'monthly_max'], monthlyMinDF['monthly_min']])
    monthlyMinMax = monthlyMinMax.transpose()
    monthlyMinMax['monthly_total'] = monthlyMinMax['monthly_max'] - monthlyMinMax['monthly_min']
    monthlyMinMax['month'] = monthlyMinMax.index

    fig = px.bar(dailyMinMax, x = "day", y = "daily_total")
    fig.write_html("index.html")

    fig = px.bar(monthlyMinMax, x = "month", y = "monthly_total")
    fig.write_html("Monthly_Tracker.html")

    return [dailyMinMax, monthlyMinMax]

read_and_clean()
