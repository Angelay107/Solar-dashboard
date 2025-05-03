# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 20:00:03 2025

@author: alpha
"""
import numpy as np
import numpy_financial as npf

def solar_cash_flows(system_size_kw, electricity_price):
    install_cost = 2.50 * 1000 * system_size_kw
    itc = 0.30 * install_cost
    annual_gen_kwh = 1400 * system_size_kw
    o_and_m = 15 * system_size_kw

    cash_flows = []
    cumulative_savings = 0


    for year in range(26):  # Include Year 0
        if year == 0:
            cash = -install_cost + itc
        else:
            savings = annual_gen_kwh * electricity_price
            cash = savings - o_and_m
            electricity_price *= 1.025
        cash_flows.append(cash)

    irr = npf.irr(cash_flows)
    cum_cash = npf.cumsum(cash_flows)
    payback_year = next((i for i, x in enumerate(cum_cash) if x > 0), None)
    
    return cash_flows, irr, payback_year, install_cost, annual_gen_kwh
