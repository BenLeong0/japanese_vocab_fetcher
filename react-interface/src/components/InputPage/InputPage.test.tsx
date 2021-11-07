import each from "jest-each"
import { getWords } from "./InputPage"


describe('get words', () => {
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
        expect(getWords(s)).toEqual(expected)
    });
});
