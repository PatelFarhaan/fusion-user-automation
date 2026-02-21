import os
import gspread
import pandas as pd
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials


def google_sheet_update(customer_name, customer_username, customer_password, isFusion, customer_email, customer_training, isPackage):

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(os.environ.get('GOOGLE_SERVICE_ACCOUNT_JSON'),
                                                                   scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('Retail Customers - Self Paced ').worksheet('SP 2018')
    df = pd.DataFrame(wks.get_all_records())

    start_date = datetime.now().date().strftime('%d %b %Y')
    end_date = (datetime.now().date() + timedelta(days=366)).strftime('%d %b %Y')

    global instance_duration, fusion_instance_end_date, sheet_package, sheet_single_training

    if isPackage == True:
        instance_duration = datetime.now().date().strftime('%d %b %Y')
        fusion_instance_end_date = (datetime.now().date() + timedelta(days=366)).strftime('%d %b %Y')
    else:
        instance_duration = datetime.now().date().strftime('%d %b %Y')
        fusion_instance_end_date = (datetime.now().date() + timedelta(days=121)).strftime('%d %b %Y')

    if isFusion == True:
        isFusion = 'Fusion'
    elif isFusion == False:
        isFusion = 'EBS'
    else:
        isFusion = 'Fusion + EBS'

    if isPackage == True:
        sheet_package = customer_training
        sheet_single_training = "None"
    else:
        sheet_package = "None"
        sheet_single_training = customer_training


    for index, instance in enumerate(df['Access Expired / Not']):
        if instance == 'Expired' and df.iloc[index]['Traininig '] == 'None':
            row_no = index + 2
            wks.update_cell(row_no, 2, customer_name)
            wks.update_cell(row_no, 3, customer_username)
            wks.update_cell(row_no, 4, customer_password)
            wks.update_cell(row_no, 5, start_date)
            wks.update_cell(row_no, 6, end_date)
            wks.update_cell(row_no, 7, isFusion)
            wks.update_cell(row_no, 9, instance_duration)
            wks.update_cell(row_no, 10, fusion_instance_end_date)
            wks.update_cell(row_no, 11, customer_email)
            wks.update_cell(row_no, 12, sheet_single_training)
            wks.update_cell(row_no, 13, sheet_package)
            wks.update_cell(row_no, 14, 'Valid')
            break