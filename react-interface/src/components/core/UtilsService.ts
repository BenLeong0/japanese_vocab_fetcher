import QueryParams from "../../types/QueryParams";


export default class UtilsService {

    addQueryParamsToUrl(url: string, queryParams: QueryParams): string {
        let queryString = Object.entries(queryParams)
            .map(x => x.join("="))
            .join("&");
        return url + "?" + queryString;
    }

}
