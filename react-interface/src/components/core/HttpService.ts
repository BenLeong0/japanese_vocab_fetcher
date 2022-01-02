import QueryParams from "../../types/QueryParams";
import UtilsService from "./UtilsService";


export default class HttpService {

    // API_URL: string = "https://7z39hjjfg1.execute-api.eu-west-2.amazonaws.com";
    API_URL: string = "http://3.8.95.26:5000";
    utilsService: UtilsService


    constructor() {
        this.utilsService = new UtilsService();
    }


    async makeGetRequest(slug: string, queryParams?: QueryParams): Promise<any> {
        let url: string = this.API_URL + slug;
        let cache: RequestCache = "force-cache"
        let mode: RequestMode = "cors"
        let requestOptions = {
            cache: cache,
            headers: {
              'Content-Type': 'application/json',
            },
            method: "GET",
            mode: mode,
            referrer: 'about:client',
        };

        if (typeof queryParams !== "undefined") {
            url = this.utilsService.addQueryParamsToUrl(url, queryParams)
        };

        let data: any = await fetch(url, requestOptions);
        if (data.status === 404) {
            throw new Error("An error occurred: " + data.statusText);
        }
        let resp: any = await data.json();
        return resp;
    }
}
