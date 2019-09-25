import sqlite3
from openpyxl import *
from sqlite3 import Error


def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def check_str(string):
	
	if string is None:
		return string
	string = str(string)
	if '"' in string:
		string = string.replace('"', '\"')
	if "'" in string:
		string = string.replace("'", "\'")
	
	return string


if __name__ == '__main__':
    create_table_inspections = "CREATE TABLE if not exists inspections(" \
                               "i_id INTEGER primary key," \
                               "activity_date DATE NOT NULL," \
                               "employee_id VARCHAR(15) NOT NULL," \
                               "facility_address VARCHAR(100) NOT NULL," \
                               "facility_city VARCHAR(80) NOT NULL," \
                               "facility_id VARCHAR(15) NOT NULL," \
                               "facility_name VARCHAR(100) NOT NULL," \
                               "facility_state VARCHAR(10) NOT NULL," \
                               "facility_zip VARCHAR(15) NOT NULL," \
                               "grade VARCHAR(1) NOT NULL," \
                               "owner_id VARCHAR(15) NOT NULL," \
                               "owner_name VARCHAR(80) NOT NULL," \
                               "pe_description VARCHAR(80) NOT NULL," \
                               "program_element_pe VARCHAR(4) NOT NULL," \
                               "program_name VARCHAR(80) NOT NULL," \
                               "program_status VARCHAR(10) NOT NULL," \
                               "record_id VARCHAR(15) NOT NULL," \
                               "score VARCHAR(10) NOT NULL," \
                               "serial_number VARCHAR(20) NOT NULL," \
                               "service_code VARCHAR(15) NOT NULL," \
                               "service_description VARCHAR(80) NOT NULL);"


    conn = create_db("data2.db")

    if conn is not None:

        execute_sql(conn, create_table_inspections)
        print("loading inspections")
        data_inspections = load_workbook("inspections(1).xlsx")
        data_inspections_ws = data_inspections['inspections']

        print("done")
        print("read inspections")
        for i in data_inspections_ws:
            print(i[0].value)
            sql = "insert into inspections(activity_date,employee_id,facility_address,facility_city," \
                  "facility_id, facility_name, facility_state, facility_zip, grade," \
                  "owner_id,owner_name,pe_description,program_element_pe,program_name," \
                  "program_status,record_id,score,serial_number,service_code,service_description) values(?,?,?,?,?,?,?,?,?,?," \
                  "?,?,?,?,?,?,?,?,?,?)"
            curs = conn.cursor()
            print(curs)
            curs.execute(sql, [i[j].value for j in range(20)])
        conn.commit()
        conn.close()
