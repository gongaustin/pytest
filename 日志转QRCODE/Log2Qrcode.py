from watchdog.observers import Observer
from watchdog.events import *
import time
import qrcode as qr
import matplotlib.pyplot as plt


##监听类
class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
            print("文件夹被创建")
        else:
            create_qrcode()
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
            print("文件夹被删除")
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
            print("文件夹被修改")
        else:
            plt.close()
            create_qrcode()
            print("file modified:{0}".format(event.src_path))


# 读取配置日志文件的路径
def read_log_path():
    f = open('log_path.conf', 'r', encoding='utf-8')
    text = f.readlines()
    f.close()
    return text[0]


# 读取日志文件内容
def read_log_info(log_path):
    log_path = read_log_path()
    f = open(log_path, 'r', encoding='utf-8')
    text = f.readlines()
    f.close()
    return text[0]


# 生成二维码并显示
def create_qrcode():
    log_path = read_log_path()
    info = read_log_info(log_path)
    qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    img = qr.make(info)
    plt.imshow(img)
    plt.axis('off')  # 关掉坐标轴为 off
    plt.draw()
    plt.show()


if __name__ == "__main__":
    create_qrcode()
    observer = Observer()
    event_handler = FileEventHandler()
    path = read_log_path()
    observer.schedule(event_handler, path, True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
