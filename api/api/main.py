from api import utils
from api.coordinator import get_info


def lambda_handler(event, context):
    word_list = utils.get_words_from_lambda(event)
    resp = get_info(word_list)
    return resp
