from bs4 import BeautifulSoup as bs

list_of_test = 'C:\\Users\\sa.gubar\\Documents\\ImportAutotest\\TestImportPowerOfAttorneyTab\\TestImportPowerOfAttorneyTab\\Log\\TestImportPowerOfAttorneyTab.mds.tcLogs'

def code_of_test_suite(name):
    name = name
    content = []
    with open(list_of_test, encoding='utf8') as file:
        content = file.readlines()
        content = "".join(content)
        bs_content = bs(content, "lxml")
        suite = bs_content.find_all('prp')
    name_of_test_suite = \
        [suite[i + 1].get(key='value')[:23] \
         for i in range(len(suite)) if suite[i].get(key='name') == \
         'nameofroot' and suite[i].get(key='value') == name]
    word = str(name_of_test_suite[0])
    tipe = ''
    for letter in word:
        if letter != '\\':
            tipe += letter
        else:
            break
    return tipe

file = 'C:\\Users\\sa.gubar\\Documents\\ImportAutotest\\name.txt'
with open(file, encoding='utf8') as reader:
    name = reader.read()
    test_case = code_of_test_suite(name)

describe = f'C:\\Users\\sa.gubar\\Documents\\ImportAutotest\\TestImportPowerOfAttorneyTab\\TestImportPowerOfAttorneyTab\\Log\\{test_case}\\Description.tcLog'
sum_test = f'C:\\Users\\sa.gubar\\Documents\\ImportAutotest\\TestImportPowerOfAttorneyTab\\TestImportPowerOfAttorneyTab\\Log\\{test_case}\\RootLogData.dat'
summar = f'C:\\Users\\sa.gubar\\Documents\\ImportAutotest\\TestImportPowerOfAttorneyTab\\TestImportPowerOfAttorneyTab\\Log\\{test_case}\\Summary.dat'
suit = f'C:\\Users\\sa.gubar\\Documents\\ImportAutotest\\TestImportPowerOfAttorneyTab\\TestImportPowerOfAttorneyTab\\Log\\{test_case}\\'