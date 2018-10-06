import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('REDACTED_SERVICE_ACCOUNT_FILE.json',
                                                               scope)
gc = gspread.authorize(credentials)
wks_2 = gc.open('Retail Customers - Self Paced ').worksheet('SP 2018')
df_2 = pd.DataFrame(wks_2.get_all_records())

for index, name in enumerate(df_2['Customer Email ']):
    if name == "kavya.deepthi@gmail.com":
        existing_training_name = df_2.iloc[index]['Traininig ']
        existing_package_name = df_2.iloc[index]['Package']
        isExpired = df_2.iloc[index]['Access Expired / Not']
        print("Asdas")
        global training1
        if existing_training_name == 'None':
            training1 = existing_package_name
        if existing_package_name == 'None' or existing_package_name == 'No Package':
            training1 = existing_training_name

        return training1, isExpired

    else:
        return "None1", "None2"
