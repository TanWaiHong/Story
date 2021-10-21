import pandas
raw_data = pandas.read_csv("Untitled form.csv")
date_list = raw_data.生日日期.to_list()
name_list = raw_data.您的英文名字.to_list()
email_list = raw_data.您的gmail账号.to_list()

new_data_dict = {
    "name": [],
    "email": [],
    "year": [],
    "month": [],
    "day": []
}

for time in date_list:
    current_time = time.split("-")
    new_data_dict["year"].append(current_time[0])
    new_data_dict["month"].append(current_time[1])
    new_data_dict["day"].append(current_time[2])

for name in name_list:
    new_data_dict["name"].append(name)

for email in email_list:
    new_data_dict["email"].append(email)

new_data = pandas.DataFrame(new_data_dict)
new_data.to_csv("birthdays.csv", index=False)
