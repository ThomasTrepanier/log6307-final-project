import json
import xmltodict
import json
import os
import csv
import numpy as np
import pandas as pd
import sys
from collections import defaultdict
import numpy as np

def getMatches(L1, L2):
    R = set()
    for elm in L1:
        for pat in L2:
            if elm.find(pat) != -1:
                if elm.find('.', len(pat)+1) != -1:
                    R.add(elm[:elm.find('.', len(pat)+1)])
                else:
                    R.add(elm)
    return list(R)

def xml_parse(xml_file_name):
    try:
        process_xml_file = xml_file_name
        with open(process_xml_file) as xml_file:
            for xml_string in xml_file:
                """Converting the xml to Dict"""
                data_dict = xmltodict.parse(xml_string)
                """Converting the dict to Pandas DF"""
                df_processing = pd.json_normalize(data_dict)
                xml_parse_loop(df_processing)
            xml_file.close()
    except Exception as e:
        s = str(e)
        print(s)

def xml_parse_loop(df_processing_input):
    CSV_File_Name = []
    """Getting the list of csv Files to be created"""
    with open(process_config_csv, newline='') as csvfile:
        DataCaptured = csv.DictReader(csvfile)
        for row in DataCaptured:
            if row['CSV_File_Name'] not in CSV_File_Name:
                CSV_File_Name.append(row['CSV_File_Name'])
    """Iterating the list of CSV"""
    for items in CSV_File_Name:
            df_processing = df_processing_input
            df_subset_process = []
            df_subset_list_all_cols = []
            df_process_sub_explode_Level = []
            df_final_column_name = []
            print('Parsing the xml file for creating the file - ' + str(items))
            """Fetching the field list for processs from the confic File"""
            with open(process_config_csv, newline='') as csvfile:
                    DataCaptured = csv.DictReader(csvfile)
                    for row in DataCaptured:
                        if row['CSV_File_Name'] in items:
                                df_final_column_name.append(row['ColumName'])
                                """Getting the columns until the first [] """
                                df_subset_process.append(row['XPATH'].strip('/').replace("/",".").split('[]')[0])
                                """Getting the All the columnnames"""
                                df_subset_list_all_cols.append(row['XPATH'].strip('/').replace("/",".").replace("[]",""))
                                """Getting the All the Columns to explode"""
                                df_process_sub_explode_Level.append(row['XPATH'].strip('/').replace('/', '.').split('[]'))
            explode_ld = defaultdict(set)
            """Putting Level of explode and column names"""
            for x in df_process_sub_explode_Level:
                if len(x) > 1:
                    explode_ld[len(x) - 1].add(''.join(x[: -1]))
            explode_ld = {k: list(v) for k, v in explode_ld.items()}
            #print(' The All column list is for the file ' + items + " is " + str(df_subset_list_all_cols))
            #print(' The first processing for the file ' + items + " is " + str(df_subset_process))
            #print('The explode level of attributes for the file ' + items + " is " + str(explode_ld))
            """Remove column duplciates"""
            df_subset_process = list(dict.fromkeys(df_subset_process))
            for col in df_subset_process:
                if col not in df_processing.columns:
                    df_processing[col] = np.nan
            df_processing = df_processing[df_subset_process]
            df_processing_col_list = df_processing.columns.tolist()
            print ('The total levels to be exploded : %d' % len(explode_ld))
            i=0
            level=len(explode_ld)
            for i in range(level):
                print (' Exploding the Level : %d' % i )
                df_processing_col_list = df_processing.columns.tolist()
                list_of_explode=set(df_processing_col_list) & set(explode_ld[i + 1])
                #print('List to expolde' + str(list_of_explode))
                """If founc in explode list exlplode some xml doesnt need to have a list it could be column handling the same"""
                for c in list_of_explode:
                    print (' There are column present which needs to be exploded - ' + str(c))
                    df_processing = pd.concat((df_processing.iloc[[type(item) == list for item in df_processing[c]]].explode(c),df_processing.iloc[[type(item) != list for item in df_processing[c]]]))
                    print(' Finding the columns need to be fetched ')
                """From the overall column list fecthing the attributes needed to explode"""
                next_level_pro_lst = getMatches(df_subset_list_all_cols,explode_ld[ i + 1 ])
                #print(next_level_pro_lst)
                df_processing_col_list = df_processing.columns.tolist()
                for nex in next_level_pro_lst:
                    #print ("Fetching " + nex.rsplit('.', 1)[1] + ' from ' + nex.rsplit('.', 1)[0] + ' from ' + nex )
                    parent_col=nex.rsplit('.', 1)[0]
                    child_col=nex.rsplit('.', 1)[1]
                    #print(parent_col)
                    #print(df_processing_col_list)
                    if parent_col not in df_processing_col_list:
                        df_processing[nex.rsplit('.', 1)[0]] = ""
                    try:
                        df_processing[nex] = df_processing[parent_col].apply(lambda x: x.get(child_col))
                    except AttributeError:
                        df_processing[nex] = ""
                df_processing_col_list = df_processing.columns.tolist()
                if i == level-1:
                    print('Last Level nothing to be done')
                else:
                    """Extracting All columns until the next exlode column list is found"""
                    while len(set(df_processing_col_list) & set(explode_ld[i + 2]))==0:
                        next_level_pro_lst = getMatches(df_subset_list_all_cols, next_level_pro_lst)
                        #print(next_level_pro_lst)
                        for nextval in next_level_pro_lst:
                            if nextval not in df_processing_col_list:
                                #print("Fetching " + nextval.rsplit('.', 1)[1] + ' from ' + nextval.rsplit('.', 1)[0] + ' from ' + nextval)
                                if nextval.rsplit('.', 1)[0] not in df_processing.columns:
                                    df_processing[nextval.rsplit('.', 1)[0]] = ""
                                try:
                                    df_processing[nextval] = df_processing[nextval.rsplit('.', 1)[0]].apply(lambda x: x.get(nextval.rsplit('.', 1)[1]))
                                except AttributeError:
                                    df_processing[nextval] = ""

                        df_processing_col_list = df_processing.columns.tolist()


            df_processing = df_processing[df_subset_list_all_cols]
            df_processing.columns = df_final_column_name
            # if file does not exist write header
            if not os.path.isfile(items):
                print("The file does not exists Exists so writing new")
                df_processing.to_csv('{}'.format(items), header='column_names',index=None)
            else:  # else it exists so append without writing the header
                print("The file does exists Exists so appending")
                df_processing.to_csv('{}'.format(items), mode='a', header=False,index=None)


from datetime import datetime
startTime = datetime.now().strftime("%Y%m%d_%H%M%S")
startTime = str(os.getpid()) + "_" + startTime
process_task_name = ''
process_config_csv = 'config.csv'
xml_file_name = 'test.xml'
old_print = print

def timestamped_print(*args, **kwargs):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    printheader = now + " xml_parser " + " " + process_task_name + " - "
    old_print(printheader, *args, **kwargs)
print = timestamped_print

xml_parse(xml_file_name)
