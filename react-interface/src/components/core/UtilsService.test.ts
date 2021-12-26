import each from "jest-each"

import QueryParams from "../../types/QueryParams";
import UtilsService from "./UtilsService";


const utilsService = new UtilsService();

describe("addQueryParamsToUrl works", () => {
    const url = "www.text.com/example"
    each([
        [{word: "hi"}, "www.text.com/example?word=hi"],
        [{word: "hi", colour: "red"}, "www.text.com/example?word=hi&colour=red"],
        [{word: "hi", colour: "red", hi: "5"}, "www.text.com/example?word=hi&colour=red&hi=5"],
    ]).it("with the params '%s'", (params: QueryParams, expected: string) => {
        expect(utilsService.addQueryParamsToUrl(url, params)).toBe(expected)
    });
});

describe('extract words from input', () => {
    each([
        ["", []],
        ["test", ["test"]],
        ["test word", ["test", "word"]],
        ["test word   ", ["test", "word"]],
        ["test   word", ["test", "word"]],
        ["test\nword", ["test", "word"]],
        ["test \n word", ["test", "word"]],
        ["a     test \n word", ["a", "test", "word"]],
    ]).it("with the input '%s'", (s: string, expected: string[]) => {
        expect(utilsService.extractWordsFromInput(s)).toEqual(expected)
    });
});
