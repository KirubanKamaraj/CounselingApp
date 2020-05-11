import xlrd
import sqlite3 as sql

loc = ("Q:\Coding\Python\Projects\Counseling\TNEA_2018_Allotment_Details.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

print(sheet.row_values(1))

with sql.connect("Q:/Coding/Python/Projects/Counseling/Counseling.db") as DealerData:
    DD = DealerData.cursor()
    DD.execute(''' CREATE TABLE IF NOT EXISTS Counseling(CollegeCode TEXT, BranchCode TEXT, RoundNo TEXT, AppNo INT, Community TEXT, OverallRank INT, CommunityRank INT, MARK INT, ChoiceNo INT, CatagoryAllotted TEXT) ''')
    for i in range(1, 72649):
        sheet_input = sheet.row_values(i)
        DD.execute('''INSERT INTO Counseling(CollegeCode, BranchCode, RoundNo, AppNo, Community, OverallRank, CommunityRank, MARK, ChoiceNo, CatagoryAllotted) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(sheet_input[7], sheet_input[8], sheet_input[1], sheet_input[2], sheet_input[3], sheet_input[4], sheet_input[5], sheet_input[6], sheet_input[9], sheet_input[10]))
    DealerData.commit()

