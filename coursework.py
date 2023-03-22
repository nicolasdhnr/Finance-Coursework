"""
Streamlit UI to display UI for coursework.Page should contain:
- 4 text boxes to log the number of cards remaining in each suit 
- a next round button to save the number of remaining card and save into csv 

"""

import streamlit as st
from coursework_logic import calculate_probability
import pandas as pd
# basic streamlit set up 
st.set_page_config(page_title="Coursework", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")

# create a button to save the number of cards remaining in each suit
st.sidebar.markdown("Click the button below to save the number of cards remaining in each suit")

# create a main page to display the number of cards remaining in each suit
st.title("Cards Remaining")
st.markdown("Please enter the number of cards remaining in each suit")
spades = st.number_input("Spades", min_value=0, max_value=13, value=13)
hearts = st.number_input("Hearts", min_value=0, max_value=13, value=13)
diamonds = st.number_input("Diamonds", min_value=0, max_value=13, value=13)
clubs = st.number_input("Clubs", min_value=0, max_value=13, value=13)

# create a button to save the number of cards remaining in each suit
st.markdown("Click the button below to save the number of cards remaining in each suit")
next_round = st.button("Next Round")

# calculate the probability     
probabilities = calculate_probability(spades + hearts + diamonds + clubs, spades, hearts, diamonds, clubs)

# output them on the UI with their price (probability * 100). truncate then to 2 sig figs
st.markdown("The probability of picking the card at the next round is (hence apporiximation of fair price) :")

st.markdown(f"Spades: {probabilities[0] * 100:.2f}")
st.markdown(f"Hearts: {probabilities[1] * 100:.2f}")
st.markdown(f"Diamonds: {probabilities[2] * 100:.2f}")
st.markdown(f"Clubs: {probabilities[3] * 100:.2f}")



# save the number of cards remaining in each suit into a csv file
if next_round:
    with open("game.csv", "a") as f:
        f.write(f"{spades},{hearts},{diamonds},{clubs}\n")

    # also, read the my_trades_csv to see if the same suit has been bought then sold, if so calculate the profit and display it on the UI
    

        


        
        

        


# Next in the next section, I want to keep track of my buys. Make a drop down menu with each suit, then a quantity field then price, then a buy or sell button 
# Then I want to save the data into a csv file.

# Then I want to create a page to display the data in a table.
drop_down = st.selectbox("Select a suit", ["Spades", "Hearts", "Diamonds", "Clubs"])
quantity = st.number_input("Quantity", min_value=0, max_value=100, value=0)
price = st.number_input("Price", min_value=0, max_value=100, value=0)
buy_sell = st.selectbox("Buy or Sell", ["Buy", "Sell"])
# submit button
submit = st.button("Submit")

if submit:
    with open("my_trades.csv", "a") as f:
        f.write(f"{drop_down},{quantity},{price},{buy_sell}\n")


# Then I want to create a page to display the data in a table.
st.title("My Trades")
with open("my_trades.csv", "r") as f:
    df = pd.read_csv(f)
    df.columns = ["Suit", "Quantity", "Price", "Buy/Sell"]
    st.dataframe(df)





st.title("Profit") # update at every new round 

with open("my_trades.csv", "r") as f:
        # read csv into a dataframe
        df = pd.read_csv(f)
        # group by Spades, Hearts, Diamonds and Clubs 
        df.columns = ["Suit", "Quantity", "Price", "Buy/Sell"]
    
        df = df.groupby("Suit")
        
        # calculate the profit for each suit
        for suit in df.groups:
            # get the number of buys and sells for each suit times the price
            buys = df.get_group(suit)[df.get_group(suit)["Buy/Sell"] == "Buy"]["Quantity"].sum() * df.get_group(suit)[df.get_group(suit)["Buy/Sell"] == "Buy"]["Price"].sum()
            sells = df.get_group(suit)[df.get_group(suit)["Buy/Sell"] == "Sell"]["Quantity"].sum() * df.get_group(suit)[df.get_group(suit)["Buy/Sell"] == "Sell"]["Price"].sum()

            # calculate the profit for each suit
            profit = (sells - buys)
            # display the profit for each suit
            st.markdown(f"Profit for {suit}: {profit} Cents")





