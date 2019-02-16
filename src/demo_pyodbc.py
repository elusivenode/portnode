import pyodbc
import pandas as pd

cnxn = pyodbc.connect(driver='{SQL Server}', server='curium-dev-db\db01', database='CuriumData_dev', trusted_connection='yes')
cursor = cnxn.cursor()
df = pd.DataFrame(cursor.execute("select BusinessDate, ForeignCCY, DailyReturnSpot from CuriumData_dev.Master.FXRate where BusinessDate = '13Feb2019'").fetchall())
cnxn.close()
test = 1