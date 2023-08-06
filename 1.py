def calculate_cooling_load(area, occupants, building_type, outdoor_temp, indoor_temp):
    if building_type == "residential":
        cooling_load = 100 * occupants
    elif building_type == "commercial":
        cooling_load = 150 * occupants
    else:
        raise ValueError("Invalid building type. Supported types are 'residential' and 'commercial'.")

    overall_heat_transfer_coefficient = 30  # W/m²°C

    q_conduction = overall_heat_transfer_coefficient * area * (outdoor_temp - indoor_temp)
    sensible_cooling_load = q_conduction + cooling_load

    return sensible_cooling_load

if __name__ == "__main__":
    # Get user inputs
    area = float(input("Enter the area of the building (in square meters): "))
    occupants = int(input("Enter the number of occupants in the building: "))
    building_type = input("Enter the type of building (residential/commercial): ").lower()
    outdoor_temp = float(input("Enter the outdoor temperature (in Celsius): "))
    indoor_temp = float(input("Enter the indoor desired temperature (in Celsius): "))

    try:
        cooling_load = calculate_cooling_load(area, occupants, building_type, outdoor_temp, indoor_temp)
        print(f"The sensible cooling load is: {cooling_load} W")
    except ValueError as e:
        print(str(e))
