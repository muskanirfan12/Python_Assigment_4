import streamlit as st
import requests

# Custom CSS
st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .info-box {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .info-text {
            font-size: 20px;
            color: #34495e;
            line-height: 1.6;
        }
        input {
            border-radius: 8px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def fetch_Country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data["capital"][0]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currencies"]
        region = country_data["region"]
        return name, capital, population, area, currency, region
    else:
        return None

def main():
    st.markdown('<h1 class="main-title">🌍 Country Information App</h1>', unsafe_allow_html=True)

    country_name = st.text_input("Enter a country name")

    if country_name:
        country_info = fetch_Country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region = country_info
            currency_name = list(currency.values())[0]["name"]
            currency_symbol = list(currency.values())[0]["symbol"]

            st.markdown(
                f"""
                <div class="info-box">
                    <div class="info-text"><b>Name:</b> {name}</div>
                    <div class="info-text"><b>Capital:</b> {capital}</div>
                    <div class="info-text"><b>Population:</b> {population:,}</div>
                    <div class="info-text"><b>Area:</b> {area:,} sq km</div>
                    <div class="info-text"><b>Currency:</b> {currency_name} ({currency_symbol})</div>
                    <div class="info-text"><b>Region:</b> {region}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
