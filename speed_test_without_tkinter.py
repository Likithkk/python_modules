import speedtest

test =speedtest.Speedtest()

print("Loading server list")
test.get_servers() #get list of server available for test
print("getting the best server")
best = test.get_best_server()
# print(best)
download_result = test.download() #to check for download speed
print(download_result) #returns in bits per sec
# for bits to mbps divide by 2^20
upload_result = test.upload() #to check for upload speed 
print(upload_result) #returns in bits per sec
ping_result = test.results.ping
print(ping_result) #milli seconds