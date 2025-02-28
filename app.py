import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="QuCreate Streamlit Lab - Earnings Power Monitor", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab - Earnings Power Monitor")
st.divider()

# Explanation of the Application
st.write("""
    **Welcome to the Earnings Power Monitor!** 🚀 

    This interactive application is designed to help you understand a company's earnings power by visualizing key performance indicators (KPIs). 
    It's a tool for fundamental analysts to quickly assess financial health and future prospects. 
    This lab uses synthetic data to demonstrate data handling and visualization techniques, making complex financial analysis accessible and engaging.

    **Course Context**: This application aligns with the concepts discussed in the **'Data Science for Long-Term Investment Decisions'** chapter of the *AI and Big Data in Investments* course (Module 3), particularly slide 12, which emphasizes long-term earnings power. 
    Here, we operationalize those concepts by enabling you to interactively explore KPIs and benchmark company performance.

    Let's dive in and explore the earnings power! 
    Use the dropdown menus and interactive charts below to analyze different KPIs and compare companies. 
    Hover over data points and chart elements for detailed explanations and insights.
""")
st.divider()

# --- Data Generation ---
@st.cache_data
def generate_synthetic_data():
    """Generates synthetic financial data for demonstration purposes."""
    companies = ["TechCorp", "MediGoods", "GreenEnergi", "FinServInc", "RetailMax"]
    peers_group = {
        "TechCorp": ["MediGoods", "RetailMax"],
        "MediGoods": ["TechCorp", "FinServInc"],
        "GreenEnergi": ["RetailMax", "FinServInc"],
        "FinServInc": ["MediGoods", "GreenEnergi"],
        "RetailMax": ["TechCorp", "GreenEnergi"],
    }
    kpis = ["Revenue Growth", "Operating Margin", "Return on Equity"]
    years = pd.date_range(start="2018", end="2024", freq="Y").year.tolist()
    data = []
    for company in companies:
        for kpi in kpis:
            for year in years:
                # Base values and trends - making it somewhat realistic
                if kpi == "Revenue Growth":
                    base_value = np.random.uniform(0.02, 0.15) # 2% to 15% growth
                    trend = np.random.uniform(-0.02, 0.02) # Slight trend up or down
                elif kpi == "Operating Margin":
                    base_value = np.random.uniform(0.10, 0.25) # 10% to 25% margin
                    trend = np.random.uniform(-0.01, 0.01)
                elif kpi == "Return on Equity":
                    base_value = np.random.uniform(0.08, 0.20) # 8% to 20% ROE
                    trend = np.random.uniform(-0.015, 0.015)

                value = base_value + trend * (year - 2018) + np.random.normal(0, 0.03) # Adding some noise
                data.append({"Company": company, "KPI": kpi, "Year": year, "Value": max(0, value)}) # Ensure non-negative values

    df = pd.DataFrame(data)
    return df, companies, kpis, peers_group

df, companies, kpis, peers_group = generate_synthetic_data()

# --- KPI Selection ---
st.header("1. Select Key Performance Indicator (KPI)")
kpi_explanation = """
Select a KPI from the dropdown to visualize its trend over time and compare it against industry peers. 
**KPIs available:**
- **Revenue Growth**: Indicates the percentage increase in a company's sales over a period. A higher growth rate often suggests strong market demand and business expansion.
- **Operating Margin**: Represents the percentage of revenue remaining after deducting operating expenses. A higher margin indicates efficient cost management and profitability from core operations.
- **Return on Equity (ROE)**: Measures how much profit a company generates with the money shareholders have invested. A higher ROE suggests effective use of shareholder investments to generate profits.
"""
st.write(kpi_explanation)
selected_kpi = st.selectbox("Choose a KPI", kpis, help="Select a KPI to analyze.", index=0)

st.divider()

# --- Time Series Visualization ---
st.header("2. Time Series Analysis")
time_series_explanation = f"""
The line chart below displays the historical trend of **{selected_kpi}** for each company from 2018 to 2023. 
This visualization helps in understanding the performance trajectory of companies over time. 
**Hover over the lines to see the exact values for each year.**
"""
st.write(time_series_explanation)

time_series_data = df[df['KPI'] == selected_kpi]
fig_time_series = px.line(time_series_data, x='Year', y='Value', color='Company',
                     title=f'{selected_kpi} Trend Over Time',
                     labels={'Value': selected_kpi, 'Year': 'Year'},
                     hover_name='Company',
                     hover_data=['Value']) # Added hover_data for clarity

fig_time_series.update_layout(
    xaxis_title="Year",
    yaxis_title=selected_kpi,
    legend_title="Company",
    hovermode="x unified" # To show tooltip for all companies at the same x position
)
st.plotly_chart(fig_time_series, use_container_width=True)

st.divider()

# --- Peer Comparison ---
st.header("3. Peer Comparison")
peer_comparison_explanation = f"""
This section allows you to compare a selected company's **{selected_kpi}** against its industry peers for the most recent year (2023). 
Benchmarking against peers is crucial for understanding relative performance within the industry. 
Select a company to see how it stacks up against its peers in terms of the chosen KPI.
"""
st.write(peer_comparison_explanation)

selected_company = st.selectbox("Select a Company for Peer Comparison", companies, index=0, help="Choose a company to compare with its peers.")
current_year = df['Year'].max()
company_peers = peers_group[selected_company]
peer_companies = [selected_company] + company_peers

peer_data = df[(df['KPI'] == selected_kpi) & (df['Company'].isin(peer_companies)) & (df['Year'] == current_year)]

if not peer_data.empty:
    fig_peer_comparison = px.bar(peer_data, x='Company', y='Value',
                                title=f'{selected_kpi} Peer Comparison for {selected_company} ({current_year})',
                                labels={'Value': selected_kpi, 'Company': 'Company'},
                                color='Company',
                                category_orders={"Company": peer_companies}) # Ensure order of companies in bar chart

    fig_peer_comparison.update_layout(
        xaxis_title="Company",
        yaxis_title=selected_kpi,
        legend_title="Company",
        showlegend=False # Since company names are on x-axis
    )
    st.plotly_chart(fig_peer_comparison, use_container_width=True)
else:
    st.warning("No data available for peer comparison in the selected year.")

st.divider()

# --- Earnings Power Score ---
st.header("4. Earnings Power Score (Simplified)")
earnings_score_explanation = """
The Earnings Power Score provides a simplified composite metric to assess a company's overall earnings strength. 
It's calculated based on the selected KPI for the latest year and its relative performance compared to peers. 
**Note:** This is a demonstration score and is not intended for actual financial analysis. 
It uses a basic weighted average approach for illustrative purposes.

**Formula (Simplified):**
- Score = (KPI Value Percentile Rank among peers + (Year-over-year KPI Growth) ) / 2

**Interpretation:**
- Higher score generally indicates stronger earnings power.
- Use this score as a starting point for further in-depth analysis.
"""
st.write(earnings_score_explanation)

if not peer_data.empty:
    # Calculate percentile rank for peer comparison
    peer_data['Rank'] = peer_data['Value'].rank(pct=True)
    company_rank = peer_data[peer_data['Company'] == selected_company]['Rank'].iloc[0]

    # Calculate year-over-year growth for the selected company
    company_historical_data = time_series_data[time_series_data['Company'] == selected_company].sort_values(by='Year')
    if len(company_historical_data) >= 2:
        latest_value = company_historical_data.iloc[-1]['Value']
        previous_value = company_historical_data.iloc[-2]['Value']
        YoY_growth = (latest_value - previous_value) / previous_value if previous_value != 0 else 0
    else:
        YoY_growth = 0 # Not enough historical data

    # Calculate a simplified earnings power score
    earnings_power_score = ((company_rank + YoY_growth) / 2) * 100 # Scale to 100 for easier interpretation

    st.metric(label=f"{selected_company} Earnings Power Score ({current_year})",
              value=f"{earnings_power_score:.2f}",
              help=f"Earnings Power Score based on {selected_kpi}, Peer Rank, and Year-over-year Growth.")
else:
    st.info("Earnings Power Score not available. Please select a company and KPI to calculate the score.")


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
