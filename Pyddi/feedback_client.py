import requests

from models.request.feedback.GetFeedbackByStatus import GetFeedbackByStatus
from models.request.feedback.SaveFeedBack import SaveFeedBack


class FeedbackClient:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    feedbackUrl = "https://www.omicsdi.org:443/ws/feedback/saveFeedback"
    getAllFeedbacksUrl = "https://www.omicsdi.org:443/ws/feedback/getAllFeedbacks"
    getFeedbackByStatusUrl = "https://www.omicsdi.org:443/ws/feedback/getFeedbackByStatus"

    def __init__(self):
        pass

    def save_feedback(self, searchQuery, satisfied, message, id, userInfo):
        request_params = {
            "searchQuery": searchQuery,
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
            "userInfo": userInfo
        }
        res = requests.put(self.feedbackUrl, params=request_params, headers=self.headers)
        return res

    def get_all_feedbacks(self):
        res = requests.get(self.getAllFeedbacksUrl, headers=self.headers)
        return res

    def get_all_feedbacks_by_status(self, is_satisfied):
        res = requests.get(self.getFeedbackByStatusUrl, params={"isSatisfied": is_satisfied}, headers=self.headers)
        return res
