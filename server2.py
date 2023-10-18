# @author imbigjetplane 😘
# @2023 copyright 😱 🐉
# Sever nhanh
import requests
import json


def getdata(license_key):
    payload = {
        "data": {
            "BienKS": f"{license_key}",
            "Xe": "1"
        }
    }

    data = json.dumps(payload)

    header = {
        'Content-Type': 'application/json'
    }
    # $$$$$$$$$$$$$$$$$$$
  

    '''
    result_data = {'result': {'isSuccess': True, 'violations': [
        {'licenseNumber': '98E1-866.01',
         'specs': 'Nền mầu trắng, chữ và số màu đen',
         'vehicleType': 'Ô tô',
         'violationTime': '10:07, 13/08/2023',
         'violationAddress': 'Km 39+900, Quốc lộ 31, Thị trấn Chũ, Huyện Lục Ngạn, Tỉnh Bắc Giang',
         'behavior': 'Không chấp hành hiệu lệnh của đèn tín hiệu giao thông',
         'status': 'Chưa xử phạt',
         'provider': 'Đội Cảnh sát giao thông, Trật tự, Công an huyện Lục Ngạn - Công an huyện Lục Ngạn - Tỉnh Bắc Giang',
         'contactPhone': '',
         'contactAddress': '1. Đội Cảnh sát giao thông, Trật tự, Công an huyện Lục Ngạn - Công an huyện Lục Ngạn - Tỉnh Bắc Giang\nĐịa chỉ: huyện Lục Ngạn\n'},
        {'licenseNumber': '98E1-866.01',
         'specs': 'Nền mầu trắng, chữ và số màu đen',
         'vehicleType': 'Ô tô',
         'violationTime': '17:44, 10/05/2023', 'violationAddress': 'Km 39+ 900, Quốc lộ 31',
         'behavior': 'Chở người ngồi trên xe không đội “mũ bảo hiểm cho người đi mô tô, xe máy”',
         'status': 'Chưa xử phạt',
         'provider': 'Đội Cảnh sát giao thông, Trật tự, Công an huyện Lục Ngạn - Công an huyện Lục Ngạn - Tỉnh Bắc Giang',
         'contactPhone': '',
         'contactAddress': '1. Đội Cảnh sát giao thông, Trật tự, Công an huyện Lục Ngạn - Công an huyện Lục Ngạn - Tỉnh Bắc Giang\nĐịa chỉ: huyện Lục Ngạn\n'}]}}
    '''

    result_data = p.json()
    is_success = result_data['result']['isSuccess']
    if is_success == True:
        num_foul = len(result_data['result']['violations'])
        if num_foul > 0:
            data = {
                'licenseNumber': [],
                'Số lỗi vi phạm': [f"{num_foul}"],
                'specs': [],
                'vehicleType': [],
                'behavior': [],
                'violationAddress': [],
                'violationTime': [],
                'status': [],
                'provider': [],
                'contactAddress': []
            }
            for data_violated in result_data['result']['violations']:
                for key,value in data_violated.items():
                    if key != 'contactPhone' and data[f'{key}'].count(value) == 0 and key != "Trạng thái":
                        data[f'{key}'].append(value)
                    if key == "Trạng thái":
                        data[f'{key}'].append(value)
            return data

        else:
            return "NOT VIOLATED"

    else:
        return "ERROR"


def check_status():
    try:
        payload = {
            "data": {
                "BienKS": "98E186601",
                "Xe": "1"
            }
        }

        data = json.dumps(payload)

        header = {
            'Content-Type': 'application/json'
        }
        # $$$$$$$$$$$$$$$$$$$
        result_data = p.json()
        is_success = result_data['result']['isSuccess']
        if is_success == True:
            return "Active"
        else:
            return "Error"
    except:
        return "Error"
