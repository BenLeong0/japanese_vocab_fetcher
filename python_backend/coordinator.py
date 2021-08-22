


from typing import Dict, List

from modules import ojad, suzuki, wadoku


def get_info(word_list: List[str]) -> Dict:
    # multi thread!
    ojad_dict = ojad.get_accent_dict(word_list)
    suzuki_dict = suzuki.get_accent_dict(word_list)
    wadoku_dict = wadoku.get_accent_dict(word_list)

    return generate_response(
        word_list=word_list,
        ojad_dict=ojad_dict,
        suzuki_dict=suzuki_dict,
        wadoku_dict=wadoku_dict
    )



def generate_response(
    word_list: List[str],
    ojad_dict: Dict[str,str],
    suzuki_dict: Dict[str,str],
    wadoku_dict: Dict[str,str],
):
    resp = [{
        'word': word,
        'accent': {
            'ojad': ojad_dict[word],
            'suzuki': suzuki_dict[word],
            'wadoku': wadoku_dict[word],
        },
    } for word in word_list]
    return resp
