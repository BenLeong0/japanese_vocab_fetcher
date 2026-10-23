from collections import defaultdict
from threading import Thread
from typing import Any, Protocol

from api.custom_types.alternative_string_types import Kaki
from api.custom_types.response_types import FullResponseItem
from api.modules import (
    forvo,
    japanesepod,
    jisho,
    ojad,
    suzuki,
    tatoeba,
    wadoku,
    wanikani,
)


class Module(Protocol):  # pylint: disable=too-few-public-methods
    NAME: str

    def main(self, word_list: list[Kaki]) -> dict: ...


MODULES = (
    forvo,
    japanesepod,
    jisho,
    ojad,
    suzuki,
    tatoeba,
    wadoku,
    wanikani,
)


MODULE_NAMES = tuple(module.NAME for module in MODULES)


def get_modules(sources: list[str] | None = None) -> tuple[Module, ...]:
    """Return the modules matching the given source names (all modules if None)"""
    if sources is None:
        return MODULES
    unknown = sorted(set(sources) - set(MODULE_NAMES))
    if unknown:
        raise ValueError(f"Unknown sources: {', '.join(unknown)}")
    return tuple(module for module in MODULES if module.NAME in sources)


def get_info(
    word_list: list[Kaki],
    sources: list[str] | None = None,
) -> list[FullResponseItem]:
    modules = get_modules(sources)
    results_dict = generate_results_dict(word_list, modules)
    response = generate_response(results_dict, word_list, modules)
    return response


def generate_results_dict(
    word_list: list[Kaki],
    modules: tuple[Module, ...] = MODULES,
) -> defaultdict[str, dict[Kaki, Any]]:
    results_dict: defaultdict[str, dict[Kaki, Any]] = defaultdict(dict)

    def call_script(module: Module, word_list: list[Kaki]) -> None:
        results_dict[module.NAME] = module.main(word_list)

    threads: list[Thread] = [
        Thread(target=call_script, args=[module, word_list]) for module in modules
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return results_dict


def generate_response(
    results_dict: defaultdict[str, dict[Kaki, Any]],
    word_list: list[Kaki],
    modules: tuple[Module, ...] = MODULES,
) -> list[FullResponseItem]:
    resp: list[FullResponseItem] = [
        {"word": word}  # type: ignore
        | {module.NAME: results_dict[module.NAME][word] for module in modules}  # type: ignore
        for word in word_list
    ]
    return resp
