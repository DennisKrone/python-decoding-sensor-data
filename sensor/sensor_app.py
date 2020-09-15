# Runner script for all modules
from house_info import HouseInfo
from load_data import load_sensor_data

##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print(f"Loaded records: {len(data)}")
# Module 2 code here:
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id", rec_area=test_area)
print(f"\nHouse sensor records for area {test_area} = {len(recs)}")
# Module 3 code here:

# Module 4 code here:

# Module 5 code here:
