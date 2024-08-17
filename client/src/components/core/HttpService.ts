import QueryParams from "../../types/QueryParams";
import UtilsService from "./UtilsService";


export default class HttpService {

    // API_URL: string = "http://localhost:9090"
    // API_URL: string = "http://3.8.95.26:5000";
    // API_URL: string = "https://7z39hjjfg1.execute-api.eu-west-2.amazonaws.com/dev";
    API_URL: string = "https://u36f77yj2mm3q5tk43d7vbmxeu0rccvk.lambda-url.eu-west-2.on.aws"
    utilsService: UtilsService


    constructor() {
        this.utilsService = new UtilsService();
    }


    async makeGetRequest(slug: string, queryParams?: QueryParams): Promise<any> {
        let url: string = this.API_URL + slug;
        let requestOptions = {
            headers: {
              'Content-Type': 'application/json',
            },
            method: "GET",
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
