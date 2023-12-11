'''
target_sbcs = []
	     with open('sbc_hosts.csv') as file:
	         for sbc_details in file.readlines():
	             if sbc_details.find('sbc') > -1:
	                 sbc = sbc_details.split(',')
	                 sbc_name = sbc[0].strip()
	                 sbc_type = sbc[1].strip()
	                 sbc_ip = sbc[2].strip()
	                 target_sbcs.append((sbc_name, sbc_type, sbc_ip))

	     print('Target_Skyhook_SBCs: \n\n')
	     [print(index, sbc) for index, sbc in enumerate(target_sbcs)]
	     print(f'\nTotal: {len(target_sbcs)}')

'''


import pandas

data = pandas.read_csv("host.csv")
# print(data)
# series is equivalent to a list or a column
sbc_instance = data["sbc_instance"]
sbc_type = data["sbc_type"]
sbc_ip = data["sbc_ip"]

# print(sbc_instance)
# print(sbc_type)
print(sbc_ip)
