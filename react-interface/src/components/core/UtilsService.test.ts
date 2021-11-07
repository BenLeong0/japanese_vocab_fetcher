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
