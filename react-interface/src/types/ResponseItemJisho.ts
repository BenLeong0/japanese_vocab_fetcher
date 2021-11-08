export interface JishoAPIItemJapanese {
    word: string;
    reading: string;
}

export interface JishoAPIItemLink {
    text: string;
    url: string;
}

export interface JishoAPIItemSense {
    english_definitions: string[];
    parts_of_speech: string[];
    links: JishoAPIItemLink[];
    tags: string[];
    restrictions: string[];
    see_also: string[];
    antonyms: string[];
    source: string[];
    info: string[];
    sentences: string[];
}

export interface JishoAPIItemAttribution {
    jmdict: boolean;
    jmnedict: boolean;
    dbpedia: string | boolean;
}

export interface JishoAPIItem {
    slug: string;
    is_common: boolean;
    tags: string[];
    jlpt: string[];
    japanese: JishoAPIItemJapanese[];
    senses: JishoAPIItemSense[];
    attribution: JishoAPIItemAttribution;
}

export interface JishoAPIMeta {
    status: number;
}

export interface JishoExtraItem {
    slug: string;
    japanese: JishoAPIItemJapanese[];
}

export interface JishoMainData {
    results: JishoAPIItem[];
    extra: JishoExtraItem[];
}

export default interface ResponseItemJisho {
    main_data: JishoMainData;
    success: boolean;
}
