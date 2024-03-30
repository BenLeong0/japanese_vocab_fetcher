import each from "jest-each";

import QueryParams from "../../types/QueryParams";

import UtilsService from "./UtilsService";


const utilsService = new UtilsService();

describe("addQueryParamsToUrl works", () => {
    const url = "www.text.com/example";
    each([
        [{word: "hi"}, "www.text.com/example?word=hi"],
        [{word: "hi", colour: "red"}, "www.text.com/example?word=hi&colour=red"],
        [{word: "hi", colour: "red", hi: "5"}, "www.text.com/example?word=hi&colour=red&hi=5"],
    ]).it("with the params '%s'", (params: QueryParams, expected: string) => {
        expect(utilsService.addQueryParamsToUrl(url, params)).toBe(expected);
    });
});

describe('extract words from input', () => {
    each([
        ["", []],
        ["test", ["test"]],
        ["test word", ["test", "word"]],
        ["test word   ", ["test", "word"]],
        ["   test word   ", ["test", "word"]],
        ["test   word", ["test", "word"]],
        ["test\nword", ["test", "word"]],
        ["test \n word", ["test", "word"]],
        ["a     test \n word", ["a", "test", "word"]],
    ]).it("with the input '%s'", (s: string, expected: string[]) => {
        expect(utilsService.extractWordsFromInput(s)).toEqual(expected);
    });
});

describe('doubleURIEncode works', () => {
    each([
        ["", ""],
        ["Hello", "Hello"],
        ["Hello World", "Hello%2520World"],
        ["GiveIt100%", "GiveIt100%2525"],
        ["Give It 100%", "Give%2520It%2520100%2525"],
        ["100%25%20is%20good", "100%252525%252520is%252520good"],
        ["[\"学生\"]", "%255B%2522%25E5%25AD%25A6%25E7%2594%259F%2522%255D"],
        ["[\"a\", \"b\"]", "%255B%2522a%2522,%2520%2522b%2522%255D"],
    ]).it("with the input '%s'", (s: string, expected: string) => {
        expect(utilsService.doubleURIEncode(s)).toEqual(expected);
    });
});

describe('capitaliseString works', () => {
    each([
        ["", ""],
        ["Hello", "Hello"],
        ["hello", "Hello"],
        ["hello World", "Hello World"],
        ["(hello World)", "(Hello World)"],
        ["((hello World))", "((Hello World))"],
        [" hello World", " Hello World"],
        ["  hello World", "  Hello World"],
        ["( hello World)", "( Hello World)"],
        ["( ( hello World))", "( ( Hello World))"],
    ]).it("with the input '%s'", (s: string, expected: string) => {
        expect(utilsService.capitaliseString(s)).toEqual(expected);
    });
});
