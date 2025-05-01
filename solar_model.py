# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 20:00:03 2025

@author: alpha
"""
import numpy as np

def solar_cash_flows(system_size_kw, state_price_per_kwh):
    install_cost = 2.50 * 1000 * system_size_kw
    itc = 0.30 * install_cost
    annual_gen_kwh = 1400 * system_size_kw
    o_and_m = 15 * system_size_kw

    cash_flows = []
    cumulative_savings = 0
    electricity_price = state_price_per_kwh

    for year in range(26):  # Include Year 0
        if year == 0:
            cash = -install_cost + itc
        else:
            savings = annual_gen_kwh * electricity_price
            cash = savings - o_and_m
            electricity_price *= 1.025
        cash_flows.append(cash)

    irr = np.irr(cash_flows)
    cum_cash = np.cumsum(cash_flows)
    payback_year = next((i for i, x in enumerate(cum_cash) if x > 0), None)
    
    return cash_flows, irr, payback_year, install_cost, annual_gen_kwh