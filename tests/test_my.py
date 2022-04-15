from bs4 import BeautifulSoup as bs
from datetime import datetime
from datetime import timedelta
import link


def get_time():
    suite = open_file(link.describe)
    time_start = [i.get(key='value') for i in suite if i.get(key='name') == 'start time' or i.get(key='name') == 'stop time']
    summa = str(float(time_start[1]) - float(time_start[0]))
    date_from = '30.12.1899'
    date_time_str = summa
    parts = date_time_str.split(".")
    first_part = int(parts[0])
    all_data = datetime.strptime('1899-12-30', '%Y-%m-%d') + timedelta(first_part)
    numberBufer = float('0.' + parts[1])
    numberBufer = numberBufer * 86400000
    ms_part = (numberBufer % 1000)
    numberBufer = int(numberBufer / 1000)
    s_part = numberBufer % 60
    numberBufer = int(numberBufer / 60)
    min_part = numberBufer % 60
    numberBufer = int(numberBufer / 60)
    h_part = numberBufer % 24
    numberBufer = int(numberBufer / 24)
    all_time = (str(h_part) + ":" + str(min_part) + ":" + str(s_part))
    return all_time


def open_screen(pic):
    pic = pic
    screen = link.suit
    with open(f'{screen}{pic}', "rb") as fh:
        image = fh.read()
    return image


def open_file(path):
    path = path
    content = []
    with open(path, encoding='utf8') as file:
        content = file.readlines()
        content = "".join(content)
        bs_content = bs(content, "lxml")
        suite = bs_content.find_all('prp')
    return suite


def descriptions(value):
    value = value
    description = open_file(path = link.describe)
    result = [i.get(key='value') for i in description if i.get(key='name') == value]
    return str(result[0])


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


def test_open(rp_logger):
    summary = open_file(link.summar)
    failedtests = [summary[i].get(key='value') for i in range(len(summary)) if summary[i].get(key='name') == 'failedtests']
    alltests = [summary[i].get(key='value') for i in range(len(summary)) if summary[i].get(key='name') == 'tests']
    rp_logger.info(f"TestCase = {descriptions('root logdata name')}")
    rp_logger.info(f"Time of test = {get_time()}")
    rp_logger.info(f"Count of test = {str(alltests[0])}")
    rp_logger.info(f"Failed tests = {str(failedtests[0])}")
    sorted_name = sorted_name_file()
    sorted_moniker = sorted_moniker_file()
    for ts_name in range(len(sorted_name)):
        rp_logger.info(f'                              {sorted_name[ts_name]}                              ')
        message = sorted_massage(f'{link.suit}{sorted_moniker[ts_name]}')
        picture = sorted_picture(f'{link.suit}{sorted_moniker[ts_name]}')
        for i in range(len(message)):
            if picture[i] == '':
                rp_logger.info(f"{message[i]}")
            else:
                rp_logger.info(f"{message[i]}",
                               attachment={"data": open_screen(picture[i]), "mime": "image/png"})
    return None









# def test_open(rp_logger):
#     summary = open_file(link.summar)
#     failedtests = [summary[i].get(key='value') for i in range(len(summary)) if summary[i].get(key='name') == 'failedtests']
#     alltests = [summary[i].get(key='value') for i in range(len(summary)) if summary[i].get(key='name') == 'tests']
#     rp_logger.info(f"TestCase = {descriptions('root logdata name')}")
#     rp_logger.info(f"Time of test = {get_time()}")
#     rp_logger.info(f"Count of test = {str(alltests[0])}")
#     rp_logger.info(f"Failed tests = {str(failedtests[0])}")
#     sorted_name = sorted_name_file()
#     sorted_moniker = sorted_moniker_file()
#     for ts_name in range(len(sorted_name)):
#         rp_logger.info(f'                              {sorted_name[ts_name]}                              ')
#         message = sorted_massage(f'{link.suit}{sorted_moniker[ts_name]}')
#         picture = sorted_picture(f'{link.suit}{sorted_moniker[ts_name]}')
#         for i in range(len(message)):
#             if picture[i] == '':
#                 rp_logger.info(f"{message[i]}")
#             else:
#                 rp_logger.info(f"{message[i]}",
#                                attachment={"data": open_screen(picture[i]), "mime": "image/png"})
#     return None