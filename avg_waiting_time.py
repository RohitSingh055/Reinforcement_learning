import xml.etree.ElementTree as ET

try:
    # Parse tripinfo.xml file
    tree = ET.parse('tripinfo.xml')
    root = tree.getroot()

    # Collect waiting times
    waiting_times = [float(vehicle.attrib['waitingTime']) for vehicle in root.iter('tripinfo')]

    # Calculate average waiting time
    average_waiting_time = sum(waiting_times) / len(waiting_times)

    # Print or use the average waiting time as needed
    print(f"Average Waiting Time: {average_waiting_time} seconds")

except FileNotFoundError:
    print("Error: tripinfo.xml file not found.")
except ET.ParseError as e:
    print("Error parsing XML:", e)
