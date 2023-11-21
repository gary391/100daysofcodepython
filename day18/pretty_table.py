from prettytable import PrettyTable

data1 = ['100.73.128.242', '10.14.40.76', {'100.73.132.120': '34.253.13.160'}, {'100.73.132.23': '54.195.245.120'}]
# data = [{'100.73.132.120': '34.253.13.160'}, {'100.73.132.23': '54.195.245.120'}]
x = PrettyTable()
x.field_names = ["Private_IP", "Public_IP"]

    

def is_dict (data):
    return isinstance(data, dict)
def ip_table():
    for element in data1:
        if is_dict(element):
            print(f'The element is a dictionary {element}')
            for k, v in element.items():
                x.add_row([k, v])
        else:
            print(f'Not a dictionary {element}')
            # x.add_row(["", ""])  # Add empty rows for non-dictionary elements
            x.add_row([element, ""])
    x.align = "l"
    print(x)
    
ip_table()