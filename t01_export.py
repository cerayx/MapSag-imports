import arcpy
import csv
import os


class x:
    def __init__(self, ali_path, csv_path):
        self.csv_export(csv_path, ali_path)

    def csv_export(self, path, table):
        with open(path, 'wb') as mapcsv:
            writer = csv.writer(mapcsv, delimiter=',')
            mapsagfields = ['TELEPHONE_NUMBER', 'HOUSE_NUMBER',
                            'HOUSE_NUMBER_SFX', 'STREET_DIR_PREFIX',
                            'NAME', 'TYPE', 'SUFDIR', 'COMMUNITY_NAME',
                            'STATE', 'LOCATION', 'CUSTOMER_NAME',
                            'CLASS_OF_SERVICE', 'TYPE_OF_SERVICE',
                            'EXCHANGE', 'ALI_ESN', 'MAIN_NUMBER',
                            'S_ORD_NUM', 'CHANGE_DATE', 'MSAG_CUSTOMER_ID',
                            'COMPANY_ID', 'SOURCE'
                            ]
            with arcpy.da.SearchCursor(table, mapsagfields, '''"ALI_ESN" = '011' ''') as cur:
                for row in cur:
                    tn = [row[0][0:3], row[0][3:10]]
                    mtn = [row[15][0:3], row[15][3:10]]
                    data = tn + list(row[1:14]) + mtn + list(row[16:])
                    writer.writerow(data)


def main(t01_input, ouptut):
    x(t01_input, ouptut)


if __name__ == '__main__':
    t01 = r'Database Connections\SCECD.sde\SCECD.DBO.T01_ALI'
    export_location = os.path.join(os.getcwd(), 'Data', 'ALI.csv')
    main(t01, export_location)
