import allure


def allure_init(case_data):
    allure.dynamic.feature(case_data["feature"])
    allure.dynamic.story(case_data["story"])
    allure.dynamic.title(f"ID:{case_data['id']} -- {case_data['title']}")