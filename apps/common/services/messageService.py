# encoding:utf-8
"""
@Software:PyCharm
@Time:2022/12/1 16:12
@Author:yzx
"""
from apps.common.dao import messageDao as msgDao


def get_all_message():
    idCard = msgDao.ident_generator()  # 身份证号码
    vin = msgDao.random_vin()  # 车辆车架号
    name = msgDao.random_name()  # 姓名
    phone = msgDao.phone_num()  # 电话
    organization = msgDao.create_organization()  # 组织机构代码
    social_credit = msgDao.create_social_credit()  # 统一社会信用代码
    zzm = msgDao.ZZM()  # 中征码
    gonghang = msgDao.gen_bank_card_gonghang()  # 工商银行卡
    nonghang = msgDao.gen_bank_card_nonghang()  # 农行
    jianshe = msgDao.gen_bank_card_jainshe()  # 建设
    zhongguo = msgDao.gen_bank_card_zhongguo()  # 中国
    jiaotong = msgDao.gen_bank_card_jiaotong()  # 交通
    res_list = [name, idCard, phone, social_credit, organization, vin, zzm, gonghang, nonghang, jiaotong, zhongguo,
                jianshe]
    res = {"allMsg": res_list}
    return res


def get_message_by_type(type):
    if type is None:
        return get_all_message()
    else:
        if type == "idCard":
            return get_idCard()
        if type == "vin":
            return get_vin()
        if type == "name":
            return get_name()
        if type == "phone":
            return get_phone()
        if type == "organization":
            return get_organization()
        if type == "social_credit":
            return get_social_credit()
        if type == "zzm":
            return get_zzm()
        if type == "gonghang":
            return get_gonghang()
        if type == "nonghang":
            return get_nonghang()
        if type == "jianshe":
            return get_jianshe()
        if type == "zhongguo":
            return get_zhongguo()
        if type == "jiaotong":
            return get_jiaotong()
        return None


def get_idCard():
    idCard = msgDao.ident_generator()  # 身份证号码
    list = [idCard]
    return {"type_msg": list}


def get_vin():
    vin = msgDao.random_vin()  # 车辆车架号
    list = [vin]
    return {"type_msg": list}


def get_name():
    name = msgDao.random_name()  # 姓名
    list = [name]
    return {"type_msg": list}


def get_phone():
    phone = msgDao.phone_num()  # 电话
    list = [phone]
    return {"type_msg": list}


def get_organization():
    organization = msgDao.create_organization()  # 组织机构代码
    list = [organization]
    return {"type_msg": list}


def get_social_credit():
    social_credit = msgDao.create_social_credit()  # 统一社会信用代码
    list = [social_credit]
    return {"type_msg": list}


def get_zzm():
    zzm = msgDao.ZZM()  # 中征码
    list = [zzm]
    return {"type_msg": list}


def get_gonghang():
    gonghang = msgDao.gen_bank_card_gonghang()  # 工商银行卡
    list = [gonghang]
    return {"type_msg": list}


def get_nonghang():
    nonghang = msgDao.gen_bank_card_nonghang()  # 农行
    list = [nonghang]
    return {"type_msg": list}


def get_jianshe():
    jianshe = msgDao.gen_bank_card_jainshe()  # 建设
    list = [jianshe]
    return {"type_msg": list}


def get_zhongguo():
    zhongguo = msgDao.gen_bank_card_zhongguo()  # 中国
    list = [zhongguo]
    return {"type_msg": list}


def get_jiaotong():
    jiaotong = msgDao.gen_bank_card_jiaotong()  # 交通
    list = [jiaotong]
    return {"type_msg": list}


if __name__ == '__main__':
    print(get_message_by_type(type=None))
    print(get_message_by_type(type="idCard"))
