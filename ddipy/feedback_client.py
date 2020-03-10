import requests
from ddipy import constants


class FeedbackClient:

    def __init__(self):
        pass

    @staticmethod
    def save_feedback(search_query, satisfied, message, id, user_info):
        request_params = {
            "searchQuery": search_query,
            "satisfied": satisfied,
            "message": message,
            "id": {
                "timeSecond": id.timeSecond,
                "inc": id.inc,
                "machine": id.machine,
                "time": id.time,
                "date": id.date,
                "timestamp": id.timestamp,
                "new": id.new
            },
            "userInfo": user_info
        }
        res = requests.put(constants.FEEDBACK_URL, params=request_params, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_all_feedbacks():
        res = requests.get(constants.ALL_FEEDBACK_URL, headers=constants.HEADERS)
        return res

    @staticmethod
    def get_all_feedbacks_by_status(is_satisfied=True):
        res = requests.get(constants.FEEDBACK_BY_STATUS_URL, params={"isSatisfied": is_satisfied}, headers=constants.HEADERS)
        return res
