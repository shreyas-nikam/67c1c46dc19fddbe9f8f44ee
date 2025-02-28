
```
# QuLab - Earnings Power Monitor

## Description

**Welcome to the Earnings Power Monitor!** 🚀

This interactive Streamlit application is designed to help you understand a company's earnings power by visualizing key performance indicators (KPIs). It serves as a valuable tool for fundamental analysts looking to quickly assess financial health and future prospects.

This application utilizes synthetic data to demonstrate data handling and visualization techniques, making complex financial analysis accessible and engaging. It is specifically created as an educational tool within the context of the **'Data Science for Long-Term Investment Decisions'** chapter of the *AI and Big Data in Investments* course (Module 3), particularly slide 12, which emphasizes long-term earnings power.

With the Earnings Power Monitor, you can:

- **Visualize KPI Trends:** Explore the historical trends of key performance indicators such as Revenue Growth, Operating Margin, and Return on Equity over time.
- **Compare Company Performance:** Benchmark a selected company against its industry peers for the most recent year to understand relative performance.
- **Calculate Earnings Power Score:** Get a simplified composite metric to assess a company's overall earnings strength based on selected KPIs and peer comparison.

This application is intended for educational purposes to illustrate data visualization and basic financial analysis concepts.

## Installation

To run the Earnings Power Monitor application, you need to have Python installed on your system. Follow these steps to set up the environment:

1.  **Install Python:** If you haven't already, download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/) (Python 3.8 or later is recommended).

2.  **Install pip:** Pip is the package installer for Python. It is usually included with Python installations. You can check if you have pip installed by opening your terminal or command prompt and typing:
    ```bash
    pip --version
    ```
    If pip is not installed, follow the instructions here: [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

3.  **Install required Python packages:** Navigate to the directory where you have saved the Streamlit application script (e.g., `your_script_name.py`) in your terminal or command prompt. Then, install the necessary Python libraries by running the following command:
    ```bash
    pip install streamlit pandas numpy plotly
    ```
    This command will install Streamlit, pandas, numpy, and plotly, which are required to run the application.

## Usage

1.  **Run the Streamlit application:** Once you have installed the required packages, you can run the Earnings Power Monitor application. In your terminal or command prompt, navigate to the directory containing the Streamlit script (e.g., `your_script_name.py`) and run the following command:
    ```bash
    streamlit run your_script_name.py
    ```
    Replace `your_script_name.py` with the actual name of your Python script file.

2.  **Access the application in your browser:** Streamlit will automatically open the application in your default web browser. If it doesn't open automatically, you will see a local URL in your terminal (usually `http://localhost:8501`). Copy and paste this URL into your browser to access the application.

3.  **Using the Earnings Power Monitor:**
    - **Step 1: Select Key Performance Indicator (KPI):**
        - Use the "Choose a KPI" dropdown menu to select the KPI you want to analyze. You can choose between:
            - **Revenue Growth**: Percentage increase in sales.
            - **Operating Margin**: Percentage of revenue after deducting operating expenses.
            - **Return on Equity (ROE)**: Profit generated from shareholders' investments.
        - Read the explanation provided below the header for more details about each KPI.

    - **Step 2: Time Series Analysis:**
        - Observe the line chart displaying the historical trend of the selected KPI for each company from 2018 to 2023.
        - Hover over the lines to see the exact KPI values for each company and year.
        - This visualization helps understand the performance trajectory of companies over time.

    - **Step 3: Peer Comparison:**
        - Use the "Select a Company for Peer Comparison" dropdown to choose a company.
        - The bar chart will display a comparison of the selected company's KPI against its defined industry peers for the most recent year (2023).
        - This section helps benchmark company performance relative to its competitors.

    - **Step 4: Earnings Power Score (Simplified):**
        - The application calculates and displays a simplified "Earnings Power Score" for the selected company based on the chosen KPI, its percentile rank among peers, and year-over-year growth.
        - The score is a composite metric to assess overall earnings strength (for demonstration purposes only).
        - A higher score generally indicates stronger earnings power. Refer to the explanation provided for the simplified formula and interpretation.

4.  **Explore and Analyze:** Interact with the application by selecting different KPIs and companies to explore the synthetic financial data and understand earnings power concepts.

## Credits

Developed and provided by:

**QuantUniversity**

[https://www.quantuniversity.com/](https://www.quantuniversity.com/)

This application is created for educational purposes as part of the *AI and Big Data in Investments* course.

## License

**Copyright © 2025 QuantUniversity. All Rights Reserved.**

This demonstration is solely for educational use and illustration. Any reproduction or commercial use of this application without prior written consent from QuantUniversity is prohibited.

For inquiries regarding commercial use or licensing, please contact QuantUniversity through their website.
```
