from model import *


def create_new_ad(id, title, descr, wage, place, work_time, idpeople, idcompany):
    model_create_new_ad(id, title, descr, wage, place, work_time, idpeople, idcompany)


def get_ads():
    ads = model_get_ads()
    return ads


def get_ad_by_id(ad_id):
    ad = model_get_ad_by_id(ad_id)
    return ad


def get_people_by_id(people_id):
    people = model_get_people_by_id(people_id)
    return people


def get_company_by_id(company_id):
    company = model_get_company_by_id(company_id)
    return company


def get_ad_by_id_foreign_keys(ad_id):
    data = get_ad_by_id(ad_id)
    creator = get_people_by_id(data[6])
    company = get_company_by_id(data[7])
    lstData = list(data)
    lstData[6] = creator[1]
    lstData[7] = company[1]
    data = tuple(lstData)
    return data


def update_ad(id, title, descr, wage, place, work_time, idpeople, idcompany):
    model_update_ad(id, title, descr, wage, place, work_time, idpeople, idcompany)


def delete_ad(id):
    model_delete_ad(id)
