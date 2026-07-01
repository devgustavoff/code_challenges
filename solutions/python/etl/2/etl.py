"""This module solve the ETL exercise."""
def transform(legacy_data):
    """This function return a new dict within worth of each letter."""
    return {item.lower():key for key in legacy_data for item in legacy_data[key]}