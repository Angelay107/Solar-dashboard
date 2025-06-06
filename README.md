# Solar Project Dashboard

This is a simple Streamlit app that gives a 25 yr cash flow, IRR, and payback period for solar projects based on the US state and size of the rooftop system.
https://solar-dashboard-debctudvdpp2rshakjhony.streamlit.app/

## Assumptions

- Installed cost: **$2.50/W**
- Annual production: **1,400 kWh/kW**, flat across all states
- Electricity price: State-specific, sourced from [Electric Choice](https://www.electricchoice.com/electricity-prices-by-state/)
- Electricity prices escalate **2.5% annually**
- O&M cost: **$15/kW/year**, no escalation
- ITC: **30%**, applied in Year 0
- All-equity financing

## Quick start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/solar-dashboard.git
cd solar-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run solardashboard.py

