# import csv
# file_name = r"C:\test_case\test_case.csv"
# def read_data_from_csv():
#     lst = []
#     with open(file_name, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             lst.append(row)
#     print(lst)
#     return lst
#
# def convert_lst_to_str():
#     lst_n = []
#     x = read_data_from_csv()
#     for i in (x):
#         for k in i:
#             lst_n.append(k)
#     return lst_n
#
# def write_data_into_csv(data, file_path):
#         with open(file_path, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(data)
# #
# # p = read_data_from_csv(r"C:\test_case\test_case.csv")
# # print(p)
# x = convert_lst_to_str()
# print(x)
# def read_data_from_csv():
#     """
#     This function read xpath data from csv.
#     :return: list of list
#     """
#     xpath_data = []
#     with open(file_name, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             xpath_data.append(row)
#     return xpath_data
#
# def convert_lst_to_str():
#     """
#     This function convert list inside list into function.
#     :return: list of xpath
#     """
#     lst_n = []
#     x = read_data_from_csv()
#     for i in (x):
#         for k in i:
#             lst_n.append(k)
#     return lst_n

l = [1,2,3,4,5]
for i in range(len(l)):
    if i <= 3:
        print(i)