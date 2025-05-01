# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 20:15:09 2025

@author: angela yao
"""

import streamlit as st
import pandas as pd
from solar_model import solar_cash_flows

# Prices pulled from https://www.electricchoice.com/electricity-prices-by-state/
state_prices = state_prices = {
    "AK": 0.2041,
    "AL": 0.1437,
    "AR": 0.1093,
    "AZ": 0.1356,
    "CA": 0.2684,
    "CO": 0.1314,
    "CT": 0.2578,
    "DC": 0.1818,
    "DE": 0.1476,
    "FL": 0.1270,
    "GA": 0.1240,
    "HI": 0.4032,
    "IA": 0.1131,
    "ID": 0.0966,
    "IL": 0.1382,
    "IN": 0.1344,
    "KS": 0.1230,
    "KY": 0.1260,
    "LA": 0.1122,
    "MA": 0.2684,
    "MD": 0.1585,
    "ME": 0.2293,
    "MI": 0.1607,
    "MN": 0.1252,
    "MO": 0.1051,
    "MS": 0.1289,
    "MT": 0.1141,
    "NC": 0.1221,
    "ND": 0.0870,
    "NE": 0.0949,
    "NH": 0.2177,
    "NJ": 0.1713,
    "NM": 0.1238,
    "NV": 0.1237,
    "NY": 0.2157,
    "OH": 0.1333,
    "OK": 0.1000,
    "OR": 0.1235,
    "PA": 0.1436,
    "RI": 0.2470,
    "SC": 0.1225,
    "SD": 0.1152,
    "TN": 0.1289,
    "TX": 0.1209,
    "UT": 0.0940,
    "VA": 0.1176,
    "VT": 0.2094,
    "WA": 0.1121,
    "WI": 0.1404,
    "WV": 0.1314,
    "WY": 0.1043,
}

st.title("Solar Project Financial Dashboard")

state = st.selectbox("Select your state", list(state_prices.keys()))
roof_size = st.number_input("Enter system size (kW)", min_value=1.0, step=0.1)

if st.button("Calculate"):
    cash_flows, irr, payback, cost, gen = solar_cash_flows(roof_size, state_prices[state])
    st.write(f"**System Cost:** ${cost:,.2f}")
    st.write(f"**Annual Generation:** {gen:,.0f} kWh")
    st.write(f"**IRR:** {irr:.2%}")
    st.write(f"**Payback Period:** Year {payback}")

    df = pd.DataFrame({"Year": list(range(26)), "Cash Flow": cash_flows})
    st.dataframe(df)
