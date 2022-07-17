#imports
import pandas as pd 
import streamlit as st
from datetime import datetime
from streamlit_echarts import st_echarts

#page configuration
st.set_page_config(page_title="Maxwell Knowles Financial Planning Tool", page_icon=":dollar:", layout="wide",initial_sidebar_state="expanded")

col1, col2 = st.columns(2)
with col1:
    #income
    st.header("Income")
    st.subheader("Income from Employment")
    datem = datetime.today().strftime("%b")
    today_month = datem
    today_month_income = st.number_input("Enter your expected take-home income for this month",value=3000,min_value=0)
    months_numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    monthly_income = pd.DataFrame(
        {'month': months,
        'month number':months_numbers,
        })
    #income_modify = st.checkbox('Apply income to all months? Remove check to modify individual months',1)
    l = []
#if income_modify:
    for i in range(0,len(monthly_income)):
        income = today_month_income
        tup = (income)
        l.append(tup)
    monthly_income['income']=l
    st.write('income revenue: $'+str(sum(monthly_income['income'])))
#if not income_modify:
    with st.expander('adjust income for individual months'):
        jan = st.number_input("Modify January income...", value=today_month_income)
        feb = st.number_input("Modify February income...", value=today_month_income)
        mar = st.number_input("Modify March income...", value=today_month_income)
        apr = st.number_input("Modify April income...", value=today_month_income)
        may = st.number_input("Modify May income...", value=today_month_income)
        jun = st.number_input("Modify June income...", value=today_month_income)
        jul = st.number_input("Modify July income...", value=today_month_income)
        aug = st.number_input("Modify August income...", value=today_month_income)
        sep = st.number_input("Modify September income...", value=today_month_income)
        oct = st.number_input("Modify October income...", value=today_month_income)
        nov = st.number_input("Modify November income...", value=today_month_income)
        dec = st.number_input("Modify December income...", value=today_month_income)
        months_incomes = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
        monthly_income['income']=months_incomes
        st.write('job income: $'+str(sum(months_incomes)))
    #expenses
    st.header("Expenses")
    #rent
    st.subheader("Room & Board")
    today_month_rent = st.number_input("Enter your expected rent and food spend for this month",value=1000,min_value=0)
    #rent_modify = st.checkbox('Apply rent to all months? Remove check to modify individual months',1)
    l = []
#if rent_modify:
    for i in range(0,12):
        rent = today_month_rent
        tup = (rent)
        l.append(tup)
    monthly_income['rent']=l
    st.write('rent and food expenses: $'+str(sum(monthly_income['rent'])))
#if not rent_modify:
    with st.expander('adjust rent and food for individual months'):
        jan = st.number_input("Modify January rent...", value=today_month_rent)
        feb = st.number_input("Modify February rent...", value=today_month_rent)
        mar = st.number_input("Modify March rent...", value=today_month_rent)
        apr = st.number_input("Modify April rent...", value=today_month_rent)
        may = st.number_input("Modify May rent...", value=today_month_rent)
        jun = st.number_input("Modify June rent...", value=today_month_rent)
        jul = st.number_input("Modify July rent...", value=today_month_rent)
        aug = st.number_input("Modify August rent...", value=today_month_rent)
        sep = st.number_input("Modify September rent...", value=today_month_rent)
        oct = st.number_input("Modify October rent...", value=today_month_rent)
        nov = st.number_input("Modify November rent...", value=today_month_rent)
        dec = st.number_input("Modify December rent...", value=today_month_rent)
        months_rent = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
        monthly_income['rent']=months_rent
        st.write('car expenses $'+str(sum(months_rent)))
    #car
    st.subheader("Car")
    today_month_car = st.number_input("Enter your total car expenses for this month",value=700,min_value=0)
    #car_modify = st.checkbox('Apply car expense to all months? Remove check to modify individual months',1)
    l = []
    #if car_modify:
    for i in range(0,12):
        car = today_month_car
        tup = (car)
        l.append(tup)
    monthly_income['car']=l
    st.write('car expenses: $'+str(sum(monthly_income['car'])))
    #if not car_modify:
    with st.expander('adjust car expenses for individual months'):
        jan = st.number_input("Modify January car...", value=today_month_car)
        feb = st.number_input("Modify February car...", value=today_month_car)
        mar = st.number_input("Modify March car...", value=today_month_car)
        apr = st.number_input("Modify April car...", value=today_month_car)
        may = st.number_input("Modify May car...", value=today_month_car)
        jun = st.number_input("Modify June car...", value=today_month_car)
        jul = st.number_input("Modify July car...", value=today_month_car)
        aug = st.number_input("Modify August car...", value=today_month_car)
        sep = st.number_input("Modify September car...", value=today_month_car)
        oct = st.number_input("Modify October car...", value=today_month_car)
        nov = st.number_input("Modify November car...", value=today_month_car)
        dec = st.number_input("Modify December car...", value=today_month_car)
        months_car = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
        monthly_income['car']=months_car
        st.write('car expenses: $'+str(sum(months_car)))
    #education
    st.subheader("Education")
    today_month_edu = st.number_input("Enter your total educational cost for this month",value=100,min_value=0)
    #edu_modify = st.checkbox('Apply educational expense to all months? Remove check to modify individual months',1)
    l = []
    #if edu_modify:
    for i in range(0,12):
        edu = today_month_edu
        tup = (edu)
        l.append(tup)
    monthly_income['edu']=l
    st.write('Educational expenses: $'+str(sum(monthly_income['edu'])))
    #if not edu_modify:
    with st.expander('adjust educational expenses for individual months'):
        jan = st.number_input("Modify January education...", value=today_month_edu)
        feb = st.number_input("Modify February education...", value=today_month_edu)
        mar = st.number_input("Modify March education...", value=today_month_edu)
        apr = st.number_input("Modify April education...", value=today_month_edu)
        may = st.number_input("Modify May education...", value=today_month_edu)
        jun = st.number_input("Modify June education...", value=today_month_edu)
        jul = st.number_input("Modify July education...", value=today_month_edu)
        aug = st.number_input("Modify August education...", value=today_month_edu)
        sep = st.number_input("Modify September education...", value=today_month_edu)
        oct = st.number_input("Modify October education...", value=today_month_edu)
        nov = st.number_input("Modify November education...", value=today_month_edu)
        dec = st.number_input("Modify December education...", value=today_month_edu)
        months_edu = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
        monthly_income['edu']=months_edu
        st.write('Educational expenses:$'+str(sum(months_edu)))
with col2:
    st.header("Results")
    l=[]
    cummulative_income = 0
    cummulative_rent = 0
    cummulative_car = 0
    cummulative_edu = 0
    for i in range(0,len(monthly_income)):
        cummulative_month_number = monthly_income['month number'][i]
        cummulative_income += int(monthly_income['income'][i])
        cummulative_rent += int(monthly_income['rent'][i])
        cummulative_car += int(monthly_income['car'][i])
        cummulative_edu += int(monthly_income['edu'][i])
        cummulative_delta = int(cummulative_income - (cummulative_rent + cummulative_car + cummulative_edu))
        tup = (cummulative_month_number, cummulative_income, cummulative_rent, cummulative_car, cummulative_edu, cummulative_delta)
        l.append(tup)
    cummulative = pd.DataFrame(l, columns=['month', 'income to date', 'rent and food expenses to date', 'car expenses to date', 'educational expenses to date', 'cash after expenses'])
    cummulative = cummulative.set_index('month')
    st.metric(label="Projected Take-Home Income & Cash After Expenses", value='$'+str(cummulative['income to date'][11]), delta='$'+str(cummulative['cash after expenses'][11]))

    chart = st.selectbox("Select the visualizer you'd prefer...",("Pie Chart", "Area Chart", "Line Chart"))
    if chart == 'Pie Chart':
        options = {"tooltip": {"formatter": "{a} <br/>{b} : ${c}"},"series": [{"data": [{"value": cummulative_income, "name": "Cummulative Income"}, {"value": cummulative_rent, "name": "Cummulative Rent & Food"}, {"value": cummulative_car, "name": "Cummulative Car Expenses"}, {"value": cummulative_edu, "name": "Cummulative Educational Expenses"}, {"value": cummulative_delta, "name": "Cummulative Extra Cash"}], "type": "pie"}],}
        st_echarts(options=options)
    elif chart == "Area Chart":
        st.area_chart(cummulative)
    elif chart == 'Line Chart':
        st.line_chart(cummulative)

    l=[]
    for i in range(0,12):
        month = monthly_income['month'][i]
        income1 = monthly_income['income'][i]
        rent1 = monthly_income['rent'][i]
        car1 = monthly_income['car'][i]
        edu1 = monthly_income['edu'][i]
        income = '$'+str(monthly_income['income'][i])
        rent = '$'+str(monthly_income['rent'][i])
        car = '$'+str(monthly_income['car'][i])
        edu = '$'+str(monthly_income['edu'][i])
        delta = '$'+str(income1 - (rent1+car1+edu1))
        tup = (month,income,rent,car,edu,delta)
        l.append(tup)
    summary=pd.DataFrame(l, columns=['Month','Income','Rent & Food','Car Expenses','Educational Expenses','Extra Cash Available'])
    st.table(summary)
