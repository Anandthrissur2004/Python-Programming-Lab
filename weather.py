# Import JSON library to handle JSON data
import json

# Import Pandas library to create and analyse tables
import pandas as pd


# Store sample weather information in JSON format
SAMPLE_WEATHER_JSON = """
{
  "cities": [
    {
      "location": {"city": "Mumbai"},
      "weather": {"temperature": 31.5, "humidity": 72}
    },
    {
      "location": {"city": "Delhi"},
      "weather": {"temperature": 28.0, "humidity": 58}
    },
    {
      "location": {"city": "Bengaluru"},
      "weather": {"temperature": 24.5, "humidity": 65}
    }
  ]
}
"""


# Define the main function
def main() -> None:

    # Convert JSON string into a Python dictionary
    weather_data = json.loads(SAMPLE_WEATHER_JSON)

    # Extract city name, temperature and humidity
    # Store the extracted information as a list of dictionaries
    records = [
        {
            "Location": city["location"]["city"],
            "Temperature (C)": city["weather"]["temperature"],
            "Humidity (%)": city["weather"]["humidity"],
        }
        for city in weather_data["cities"]
    ]

    # Convert the list of dictionaries into a Pandas DataFrame
    weather_table = pd.DataFrame(records)

    # Display weather details of all cities
    print("Weather details for all cities:")

    # Print the table without row index numbers
    print(weather_table.to_string(index=False))

    # Display a summarized weather report
    print("\nSummarized weather report:")

    # Read each city record one by one
    for record in records:

        # Display location, temperature and humidity
        print(
            f"Location: {record['Location']} | "
            f"Temperature: {record['Temperature (C)']:.1f} C | "
            f"Humidity: {record['Humidity (%)']}%"
        )

    # Calculate and display the average temperature
    print(
        "\nAverage temperature: "
        f"{weather_table['Temperature (C)'].mean():.1f} C"
    )

    # Calculate and display the average humidity
    print(f"Average humidity: {weather_table['Humidity (%)'].mean():.1f}%")


# Check whether the program is executed directly
if __name__ == "__main__":

    # Call the main function
    main()
