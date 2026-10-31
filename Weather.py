import json

import pandas as pd


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


def main() -> None:
    weather_data = json.loads(SAMPLE_WEATHER_JSON)

    records = [
        {
            "Location": city["location"]["city"],
            "Temperature (C)": city["weather"]["temperature"],
            "Humidity (%)": city["weather"]["humidity"],
        }
        for city in weather_data["cities"]
    ]
    weather_table = pd.DataFrame(records)

    print("Weather details for all cities:")
    print(weather_table.to_string(index=False))

    print("\nSummarized weather report:")
    for record in records:
        print(
            f"Location: {record['Location']} | "
            f"Temperature: {record['Temperature (C)']:.1f} C | "
            f"Humidity: {record['Humidity (%)']}%"
        )

    print(
        "\nAverage temperature: "
        f"{weather_table['Temperature (C)'].mean():.1f} C"
    )
    print(f"Average humidity: {weather_table['Humidity (%)'].mean():.1f}%")


if __name__ == "__main__":
    main()
