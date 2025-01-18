import psutil

def readCPULoad():
    return str(psutil.cpu_percent())

def readRAMLoad():
    return f"{round(psutil.virtual_memory().available / (1024*1024))}/{round(psutil.virtual_memory().used / (1024*1024))}/{round(psutil.virtual_memory().total / (1024*1024))}"

def readROMLoad():
    return f"{round(psutil.disk_usage('/').free / (1024*1024))}/{round(psutil.disk_usage('/').used / (1024*1024))}/{round(psutil.disk_usage('/').total / (1024*1024))}"