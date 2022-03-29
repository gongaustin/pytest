import qrcode as qr

def read_info(path):
    f = open('log_path.conf', 'r', encoding='utf-8')
    text = f.readlines()
    f.close
    return text[0]

def create_qrcode(info):
    qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    img = qr.make(info)
    img.show()

if __name__ == '__main__':
    path = 'log_path.conf'
    create_qrcode(read_info("log_path.conf"))
