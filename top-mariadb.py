import mysql.connector
import time
import psutil

conn = mysql.connector.connect(user='myuser', password='mypassword', host='localhost', database='mydb')
cursor = conn.cursor()

while True:
    cursor.execute("SHOW FULL PROCESSLIST")
    processes = cursor.fetchall()
    for process in processes:
        process_id = process[0]
        user = process[1]
        host = process[2]
        db = process[3]
        command = process[4]
        time = process[5]
        state = process[6]
        query = process[7]
        process = psutil.Process(process_id)
        cpu_percent = process.cpu_percent()
        memory_info = process.memory_info()
        io_counters = process.io_counters()
        if cpu_percent > 90:
            print("Process ID: ", process_id)
            print("User: ", user)
            print("Host: ", host)
            print("Database: ", db)
            print("Command: ", command)
            print("Time: ", time)
            print("State: ", state)
            print("Query: ", query)
            print("CPU Usage: ", cpu_percent)
            print("Memory Usage: ", memory_info.rss)
            print("Disk I/O: ", io_counters.read_bytes + io_counters.write_bytes)
    time.sleep(1)

conn.close()
