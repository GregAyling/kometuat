import pyodbc
# c=pyodbc.connect('mssql+pyodbc://admin:KardoiTownship@sample-instance.cogfvgnac9bx.ap-southeast-2.rds.amazonaws.com/sandpit?driver=SQL+Server')
cs = (
    r'DRIVER={SQL Server};'
    r'SERVER=sample-instance.cogfvgnac9bx.ap-southeast-2.rds.amazonaws.com;'
    r'DATABASE=sandpit;'
    r'UID=admin;'
    r'PWD=KardoiTownship'
)

c =  pyodbc.connect(cs)