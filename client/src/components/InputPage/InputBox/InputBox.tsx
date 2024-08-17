import React, { useState, useEffect, useRef } from "react";
import { useSearchParams } from "react-router-dom";
import LoadingSpinner from "../../../shared/LoadingSpinner/LoadingSpinner";

import FullResponseItem from "../../../types/FullResponseItem";
import QueryParams from "../../../types/QueryParams";

import HttpService from "../../core/HttpService";
import UtilsService from "../../core/UtilsService";

import "./InputBox.css";

interface InputBoxProps {
  setWordList: (s: FullResponseItem[]) => void;
  setErrorOccurred: (x: boolean) => void;
}

const InputBox: React.FC<InputBoxProps> = ({
  setWordList,
  setErrorOccurred,
}) => {
  const [searchParams, setSearchParams] = useSearchParams();

  const httpService = new HttpService();
  const utilsService = new UtilsService();

  const [text, setText] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const sendWords = useRef((forceText?: string) => {});
  sendWords.current = async (forceText?: string) => {
    setIsLoading(true);
    setErrorOccurred(false);

    const searchText = forceText || text;
    setSearchParams({ words: searchText });

    const words: string[] = utilsService.extractWordsFromInput(searchText);
    const queryParams: QueryParams = { words: JSON.stringify(words) };

    try {
    //   const resp = await httpService.makeGetRequest("/words", queryParams);
      const resp = await httpService.makeGetRequest("", queryParams);
      setWordList(resp);
      console.log(resp);
    } catch (error) {
      setErrorOccurred(true);
      console.log(error);
    } finally {
      setIsLoading(false);
    }
  };

  // Check for query params and search if present
  const searchQueryParams = useRef(() => {});
  searchQueryParams.current = () => {
    let words = searchParams.get("words");
    if (words === null || words === "") return;
    setText(words);
    sendWords.current(words);
  };
  useEffect(() => {
    searchQueryParams.current();
  }, []);

  return isLoading ? (
    <LoadingSpinner />
  ) : (
    <form className="input-form">
      <input
        name="main-input"
        className="main-input mplus"
        value={text}
        onChange={(e: any) => setText(e.target.value)}
        onSubmit={(_) => sendWords.current()}
      />
      <div className="words-display vertical-separation-small">
        {utilsService.extractWordsFromInput(text).map((word, index) => (
          <div key={index} className="word-display">
            {word}
          </div>
        ))}
      </div>
      <button
        className="button-primary vertical-separation-medium"
        type="submit"
        onClick={(_) => sendWords.current()}
      >
        Submit
      </button>
    </form>
  );
};

export default InputBox;
