interface QueryParams {
    [key: string]: string;
}


export default class HttpService {

    API_URL: string = "https://7z39hjjfg1.execute-api.eu-west-2.amazonaws.com";


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


    async makePostRequest(slug: string, body: any): Promise<any> {
        let headers: any = {};
        headers["Content-Type"] = "application/json";

        let url = this.API_URL + slug;
        let requestOptions = {
            headers,
            method: "POST",
            body: JSON.stringify(body),
        };

        let data: any = await fetch(url, requestOptions);
        let resp: any = await data.json();
        return resp;
    }


    async makeDeleteRequest(slug: string, body: any): Promise<any> {
        let headers: any = {};
        headers["Content-Type"] = "application/json";

        let url = this.API_URL + slug;
        let requestOptions = {
            headers,
            method: "DELETE",
            body: JSON.stringify(body),
        };

        let data: any = await fetch(url, requestOptions);
        let resp: any = await data.json();
        return resp;
    }


    async makePatchRequest(slug: string, body: any): Promise<any> {
        let headers: any = {};
        headers["Content-Type"] = "application/json";

        let url = this.API_URL + slug;
        let requestOptions = {
            headers,
            method: "PATCH",
            body: JSON.stringify(body),
        };

        let data: any = await fetch(url, requestOptions);
        let resp: any = await data.json();
        return resp;
    }
}
