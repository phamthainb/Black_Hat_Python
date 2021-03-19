import socket

target_host = "www.google.com"
target_port = 80

# tạo đối tượng socket với SOCK_DGRAM
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# gửi dữ liệu đến host
client.sendto(b"AAABBBCCC",(target_host,target_port))

# nhận dữ liệu trả về 
data, addr = client.recvfrom(4096)

print(addr and "data" or "no thing data")
client.close()
