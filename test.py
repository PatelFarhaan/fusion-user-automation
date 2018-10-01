import gspread
import pandas as pd
from selenium import webdriver
from oauth2client.service_account import ServiceAccountCredentials


def existing_users_details():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('REDACTED_SERVICE_ACCOUNT_FILE.json',
                                                                   scope)
    gc = gspread.authorize(credentials)
    wks_1 = gc.open('Retail Customers - Self Paced ').worksheet('SP 2017')
    wks_2 = gc.open('Retail Customers - Self Paced ').worksheet('SP 2018')

    df_1 = pd.DataFrame(wks_1.get_all_records())
    df_2 = pd.DataFrame(wks_2.get_all_records())

    for index, name in enumerate(df_2['Customer Email ']):
        if name == "REDACTED_EMAIL":
            existing_training_name = df_2.iloc[index]['Traininig ']
            existing_package_name = df_2.iloc[index]['Package']
            isExpired = df_2.iloc[index]['Access Expired / Not']

            global training1
            if existing_training_name == 'None':
                training1 = existing_package_name
            if existing_package_name == 'None' or existing_package_name == 'No Package':
                training1 = existing_training_name

            return training1, isExpired


# def existing_users_details():
#         scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#         credentials = ServiceAccountCredentials.from_json_keyfile_name('REDACTED_SERVICE_ACCOUNT_FILE.json',
#                                                                        scope)
#         gc = gspread.authorize(credentials)
#         wks_2 = gc.open('Retail Customers - Self Paced ').worksheet('SP 2018')
#         df_2 = pd.DataFrame(wks_2.get_all_records())
#
#         for index, name in enumerate(df_2['Customer Email ']):
#             if name == "REDACTED_EMAIL":
#                 existing_training_name = df_2.iloc[index]['Traininig ']
#                 existing_package_name = df_2.iloc[index]['Package']
#                 isExpired = df_2.iloc[index]['Access Expired / Not']
#
#                 global training1
#                 if existing_training_name == 'None':
#                     training1 = existing_package_name
#                 if existing_package_name == 'None' or existing_package_name == 'No Package':
#                     training1 = existing_training_name
#
#                 return training1, isExpired
#             else:
#                 return "None1","None2"

# def block_trainings_mappings(email_address):
#     training, isExpired = existing_users_details(email_address)
#     print(training, isExpired)
#     if isExpired == "Blocked":
#         if training == 'fusion_payroll_training':
#             return [239,161,25,286]
#     else:
#         return "None"
#
# def block_training(users_emaail_address):
#     xpath_number = block_trainings_mappings(users_emaail_address)
#     print(xpath_number)
    # if not xpath_number == "None":
    #     for i in xpath_number:
    #         isChecked = driver.find_element_by_css_selector(
    #             "input[id*='1group_{no1}'][name^='jform[groups][]'][type='checkbox'][value='no2']".format(no1=i, no2=i)).get_attribute(
    #             "checked")
    #         if isChecked == 'true':
    #             oracle_fusion_financials_training = driver.find_element_by_xpath('//*[@id="1group_{no3}"]'.format(no3=i))
    #             driver.execute_script("arguments[0].click();", oracle_fusion_financials_training)

    # else:
    #     print("pass")
    #     pass


ans1, ans2 = existing_users_details()
print(ans1, ans2)