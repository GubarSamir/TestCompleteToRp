from bs4 import BeautifulSoup as bs
import link

# content = []
# with open(link.sum_test, encoding='utf8') as file:
#     content = file.readlines()
#     content = "".join(content)
#     bs_content = bs(content, "lxml")
#     suite = bs_content.find_all('prp')
#
#
def open_file(path):
    path = path
    content = []
    with open(path, encoding='utf8') as file:
        content = file.readlines()
        content = "".join(content)
        bs_content = bs(content, "lxml")
        suite = bs_content.find_all('prp')
    return suite


def sorted_massage(message):
    with open(message, encoding='utf8') as mess:
        content = mess.readlines()
        content = "".join(content)
        bs_content = bs(content, "lxml")
        mess_file = bs_content.find_all('node')
    unsorted_name = [i.get(key='name') for i in mess_file if i.get(key='name')[:7] == 'message']
    unsort_message = [i.get(key='value') for i in open_file(message) if i.get(key='name') == 'message']
    unsorted_dict = [{unsorted_name[i]: unsort_message[i]} for i in range(len(unsorted_name))]
    one = [unsorted_name[i] for i in range(len(unsorted_name)) if len(unsorted_name[i]) == 9]
    two = [unsorted_name[i] for i in range(len(unsorted_name)) if len(unsorted_name[i]) == 10]
    one_and_two = sorted(one) + sorted(two)
    sorted_name = []
    for details in range(len(one_and_two)):
        for i in range(len(unsorted_dict)):
            for kay, val in unsorted_dict[i].items():
                if one_and_two[details] == kay:
                    sorted_name.append(val)
                    break
    return sorted_name


def sorted_picture(picture):
    with open(picture, encoding='utf8') as mess:
        content = mess.readlines()
        content = "".join(content)
        bs_content = bs(content, "lxml")
        pic_file = bs_content.find_all('node')
    unsorted_name = [i.get(key='name') for i in pic_file if i.get(key='name')[:7] == 'message']
    unsort_picture = [i.get(key='value') for i in open_file(picture) if i.get(key='name') == 'picture']
    unsorted_dict = [{unsorted_name[i]: unsort_picture[i]} for i in range(len(unsorted_name))]
    one = [unsorted_name[i] for i in range(len(unsorted_name)) if len(unsorted_name[i]) == 9]
    two = [unsorted_name[i] for i in range(len(unsorted_name)) if len(unsorted_name[i]) == 10]
    one_and_two = sorted(one) + sorted(two)
    sorted_pic = []
    for details in range(len(one_and_two)):
        for i in range(len(unsorted_dict)):
            for kay, val in unsorted_dict[i].items():
                if one_and_two[details] == kay:
                    sorted_pic.append(val)
                    break
    return sorted_pic

def open_node_file(path):
    path = path
    content = []
    with open(path, encoding='utf8') as file:
        content = file.readlines()
        content = "".join(content)
        bs_content = bs(content, "lxml")
        suite = bs_content.find_all('node')
    return suite


def sorted_moniker_file():
    file = open_file(link.sum_test)
    ownermoniker = [i.get(key='value') for i in file if i.get(key='name') == 'ownermoniker']
    ownermoniker_file = f'{link.suit}{ownermoniker[0]}'
    moniker_file = open_node_file(f'{link.suit}{ownermoniker[0]}')
    unsort_moniker = [i.get(key='name') for i in moniker_file if i.get(key='name')[:3] == 'row']
    unsort_details = [i.get(key='value') for i in open_file(ownermoniker_file) if i.get(key='name') == 'details']
    unsorted_dict = [{unsort_moniker[i]: unsort_details[i]} for i in range(len(unsort_moniker))]
    one = [unsort_moniker[i] for i in range(len(unsort_moniker)) if len(unsort_moniker[i]) == 4]
    two = [unsort_moniker[i] for i in range(len(unsort_moniker)) if len(unsort_moniker[i]) == 5]
    one_and_two = sorted(one) + sorted(two)
    sorted_name = []
    for details in range(len(one_and_two)):
        for i in range(len(unsorted_dict)):
            for kay, val in unsorted_dict[i].items():
                if one_and_two[details] == kay:
                    sorted_name.append(val)
                    break
    return sorted_name


def sorted_name_file():
    file = open_file(link.sum_test)
    ownermoniker = [i.get(key='value') for i in file if i.get(key='name') == 'ownermoniker']
    ownermoniker_file = f'{link.suit}{ownermoniker[0]}'
    moniker_file = open_node_file(f'{link.suit}{ownermoniker[0]}')
    unsort_moniker = [i.get(key='name') for i in moniker_file if i.get(key='name')[:3] == 'row']
    unsort_name = [i.get(key='value') for i in open_file(ownermoniker_file) if i.get(key='name') == 'name']
    unsorted_dict = [{unsort_moniker[i]: unsort_name[i]} for i in range(len(unsort_moniker))]
    one = [unsort_moniker[i] for i in range(len(unsort_moniker)) if len(unsort_moniker[i]) == 4]
    two = [unsort_moniker[i] for i in range(len(unsort_moniker)) if len(unsort_moniker[i]) == 5]
    one_and_two = sorted(one) + sorted(two)
    sorted_name = []
    for details in range(len(one_and_two)):
        for i in range(len(unsorted_dict)):
            for kay, val in unsorted_dict[i].items():
                if one_and_two[details] == kay:
                    sorted_name.append(val)
                    break
    return sorted_name


for ts_name in range(len(sorted_name_file())):
    print(f'----------------------->  {sorted_name_file()[ts_name]}  <-----------------------')
    file = open_file(f'{link.suit}{sorted_moniker_file()[ts_name]}')
    message = sorted_massage(f'{link.suit}{sorted_moniker_file()[ts_name]}')
    for i in range(len(message)):
        pass
        print(f"Log Message = {message[i]}")
