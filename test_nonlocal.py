from app1.utils import is_nonlocal_ip

ip_address = ["10.0.0.1", "192.168.1.1", "25.1.1.1", "172.16.13.1", "172.19.1.1", "172.33.51.1"]

filtered_ips = list(filter(is_nonlocal_ip,ip_address))
print(filtered_ips)