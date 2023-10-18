# Bugi bugigigiigiiii 🦋💦
# Sever Cham 👅👅💦💦
import requests
from bs4 import BeautifulSoup as bs


# Sử dụng phương thức post của request lên web site để lấy dữ liệu
def getdata(licensekey):
    try:
        # 98E186601
        r = requests.get(
            f"https://phatnguoi.vn/api/tra-cuu.php?Xe=1&BienKS={licensekey}&g-recaptcha=NTYzMy00NTkwLTQyNzQtNjE3Ni0yODMyLTUyNTUtODcxMC05NDE1LTY3MjYtNTQ5OS0yMDA0LTQzNDMtOTY3MS0xODQwLTYyNDI%3D")

        # region Lọc Dữ Liệu Cần Lấy Bằng Thư Viện Beautifulsoup
        soup = bs(r.text, 'html.parser')
        if soup.find('h3') is not None:
            num_foul = soup.find('h3').text.split(',')[0]
            soup = soup.find_all('table')
            data = {
                'Biển kiểm soát': [],
                'Số lỗi vi phạm': [f"{num_foul.split(' ')[3]}"],
                'Màu biển': [],
                'Loại phương tiện': [],
                'Lỗi vi phạm': [],
                'Địa điểm vi phạm': [],
                'Thời gian vi phạm': [],
                'Trạng thái': [],
                'Đơn vị phát hiện vi phạm': [],
                'Nơi giải quyết vụ việc': []
            }
            for table in soup:
                for tr in table.find_all('tr'):
                    flag = True
                    role = ""
                    for td in tr.find_all('td'):
                        if flag:
                            role = td.text
                            flag = False
                        else:
                            if data[f'{role}'].count(td.text) == 0 and role != "Trạng thái":
                                data[f'{role}'].append(td.text)
                            if role == "Trạng thái":
                                data[f'{role}'].append(td.text)
            # endregion
            return data
        else:
            return "NOT VIOLATED"
    except:
        return "ERROR!"


def check_status():
    try:
        r = requests.get(
            "https://phatnguoi.vn/api/tra-cuu.php?Xe=1&BienKS=30A67581&g-recaptcha=NTYzMy00NTkwLTQyNzQtNjE3Ni0yODMyLTUyNTUtODcxMC05NDE1LTY3MjYtNTQ5OS0yMDA0LTQzNDMtOTY3MS0xODQwLTYyNDI%3D")
        if r.text.find("không phát hiện lỗi vi phạm") != -1:
            return "Active"
        else:
            return "Error"
    except:
        return "Error"
