import os

import pandas as pd


def load_and_merge_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_dir = os.path.join(base_dir, '../../resources/f1_dataset')

    # Construct full paths to the CSV files
    races = pd.read_csv(os.path.join(dataset_dir, 'races.csv'))
    drivers = pd.read_csv(os.path.join(dataset_dir, 'drivers.csv'))
    circuits = pd.read_csv(os.path.join(dataset_dir, 'circuits.csv'))
    constructors = pd.read_csv(os.path.join(dataset_dir, 'constructors.csv'))
    status = pd.read_csv(os.path.join(dataset_dir, 'status.csv'))
    results = pd.read_csv(os.path.join(dataset_dir, 'results.csv'))

    # Drop unnecessary tables and rename columns
    drivers.drop(columns=['url'], inplace=True)
    circuits.drop(columns=['lat', 'lng', 'alt', 'url'], inplace=True)
    constructors.drop(columns=['url'], inplace=True)

    drivers.rename(columns={'number': 'driver_number',
                            'code': 'driver_code',
                            'nationality': 'driver_nationality'}, inplace=True)
    circuits.rename(columns={'name': 'circuit_name',
                             'location': 'circuit_location',
                             'country': 'circuit_country'}, inplace=True)
    constructors.rename(columns={'name': 'constructor_name',
                                 'nationality': 'constructor_nationality'}, inplace=True)

    # Merge datasets based on their relationships
    races_merged = races.merge(circuits, on='circuitId')
    merged_data = results.merge(races_merged, on='raceId') \
        .merge(drivers, on='driverId') \
        .merge(constructors, on='constructorId') \
        .merge(status, on='statusId')
    return merged_data