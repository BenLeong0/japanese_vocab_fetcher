interface QueryParams {
    [key: string]: string;
}


export default class HttpService {

    // API_URL: string = "https://7z39hjjfg1.execute-api.eu-west-2.amazonaws.com";
    API_URL: string = "http://127.0.0.1:5000";


    async makeGetRequest(slug: string, queryParams?: QueryParams): Promise<any> {
        let url = this.API_URL + slug;
        let requestOptions = {
            method: "GET"
        };

        if (typeof queryParams !== "undefined") {
            let reducer = (accumulator: string, currValue: string[]) => (
                accumulator + '&' + currValue[0] + '=' + currValue[1]
            );
            let queryString =  Object.entries(queryParams).reduce(reducer, '');
            url += '?' + queryString;
        };

        let data: any = await fetch(url, requestOptions);
        let resp: any = await data.json();
        return resp;
    }
}
