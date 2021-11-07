import QueryParams from "../../types/QueryParams";
import UtilsService from "./UtilsService";


export default class HttpService {

    // API_URL: string = "https://7z39hjjfg1.execute-api.eu-west-2.amazonaws.com";
    API_URL: string = "http://127.0.0.1:5000/words";
    utilsService: UtilsService


    constructor() {
        this.utilsService = new UtilsService();
    }


    async makeGetRequest(slug: string, queryParams?: QueryParams): Promise<any> {
        let url = process.env.API_URL + slug;
        let requestOptions = {
            method: "GET"
        };

        if (typeof queryParams !== "undefined") {
            url = this.utilsService.addQueryParamsToUrl(url, queryParams)
        };

        let data: any = await fetch(url, requestOptions);
        let resp: any = await data.json();
        return resp;
    }
}
