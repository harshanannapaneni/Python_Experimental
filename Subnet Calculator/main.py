from unittest import result
import streamlit as st
import ipaddress

def calculate_subnet(ip, subnet_mask):
    try:
        network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}",strict=False)
        data = {
            "Network Address": str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
            "First Usable IP": str(list(network.hosts())[0]) if network.num_addresses > 2 else "NA",
            "Last Usable IP": str(list(network.hosts())[-1]) if network.num_addresses >2 else "NA",
            "Total Usable Hosts": network.num_addresses - 2 if network.num_addresses > 2 else 0,
            "Subnet Mask": str(network.netmask),
            "Wildcard Mask": str(network.hostmask),
        }
        return data
    except Exception as e:
        return {"Error": str(e)}
    

# Streamlit app:
st.title(body="Subnet Calculator")
st.markdown("Enter the IP address and subnet mask to calculate the network details.")

# User input for IP and subnet mask
ip_address = st.text_input("IP Address (e.g.,192.168.1.1)", value="192.168.1.1")
subnet_mask = st.number_input("Subnet mask (e.g., 24 for /24)",min_value=0,max_value=32,value=24,step=1)

if st.button("Calculate"):
    if ip_address:
        result = calculate_subnet(ip_address,subnet_mask)
        if "Error" in result.keys():
            st.error(result["Error"])
        else:
            st.success("Subnet Calculations Completed!")
            for key, value in result.items():
                st.write(f"**{key}** {value}")
    else:
        st.error("Please enter valid IP address.")