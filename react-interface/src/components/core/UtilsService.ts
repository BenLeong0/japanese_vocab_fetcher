import QueryParams from "../../types/QueryParams";


export default class UtilsService {

    doubleURIEncode(s: string): string {
        return encodeURI(encodeURI(s));
    }

    addQueryParamsToUrl(url: string, queryParams: QueryParams): string {
        let queryString = Object.entries(queryParams)
            .map(x => x.join("="))
            .join("&");
        return url + "?" + this.doubleURIEncode(queryString);
    }

    extractWordsFromInput = (s: string): string[] => {
        return s.split(/\s+/).filter(char => char !== "");
    }

}
