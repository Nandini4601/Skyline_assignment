import json

#function to calculate the bitrate for both Received and Transmitted data
def get_bitrate_value(json_data,time_interval,old_rx=0,old_tx=0):
    try:
       rx_value = float(json_data["NIC"][0]["Rx"])
       tx_value = float(json_data["NIC"][0]["Tx"])       
    except KeyError:
        print("Key not found in JSON data")
        return None
    
    tx_bitrate=int((tx_value-old_tx)/time_interval)
    rx_bitrate=int((rx_value-old_rx)/time_interval)
    return rx_bitrate,tx_bitrate

#json data input from the user
json_data =[{
    "Device": "Arista",
    "Model": "X-Video",
    "NIC": [{
        "Description": "Linksys ABR",
        "MAC": "14:91:82:3C:D6:7D",
        "Timestamp": "2020-03-23T18:25:43.511Z",
        "Rx": "3698574500",
        "Tx": "122558800"
    }]
}
] 

try:
    json_string = json.dumps(json_data, indent=4)

    print(json_string)

except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)

print("Successfully parsed json data")
p_rate=2
time_interval=1/p_rate
print("The calculated time interval for the polling rate ",p_rate,"Hz  is-",time_interval," seconds")

for data in json_data:
    rx_bitrate, tx_bitrate = get_bitrate_value(data, time_interval)
    if rx_bitrate is not None and tx_bitrate is not None:
        print("Rx bit rate is", rx_bitrate, "bytes per second")
        print("Tx bit rate is", tx_bitrate, "bytes per second")
        print("=" * 40)
 