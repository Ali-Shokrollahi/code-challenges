from typing import Sequence
import pandas as pd

DATA_OPTIONS = ("All", "Temperature", "Humidity", "CO2")


def celcius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15


def convert_to_scale_0_1(value: float) -> float:
    return value / 100


def compensate_for_sensor_bias(value: float, bias: float = 23) -> float:
    return value + bias


def validate_option(option: str, options: Sequence[str]) -> str:
    if option not in options:
        raise ValueError(
            f"Option not valid, should be {DATA_OPTIONS} but {option} given!"
        )
    return option


def get_processing_data(csv_file_path: str, data_option: str) -> pd.DataFrame:
    data = pd.read_csv(csv_file_path)

    if data_option in ("Temperature", "Humidity", "CO2"):
        data = data.loc[data["Sensor"] == data_option]

    return data


def process_row(row: pd.Series) -> pd.Series:
    sensor: str = row["Sensor"]
    value: float = row["Value"]
    processing_fn = {
        "Temperature": celcius_to_kelvin,
        "Humidity": convert_to_scale_0_1,
        "CO2": compensate_for_sensor_bias,
    }
    row["Value"] = processing_fn[sensor](value)
    return row


def process_data(data: pd.DataFrame) -> pd.DataFrame:
    return data.apply(process_row, axis=1)


def main() -> None:
    option = validate_option("Temperature", DATA_OPTIONS)

    data = get_processing_data("sensor_data.csv", option)

    print(process_data(data))


if __name__ == "__main__":
    main()
