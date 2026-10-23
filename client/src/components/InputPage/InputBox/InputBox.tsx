import React, { useState, useEffect, useRef } from "react";
import { useSearchParams } from "react-router-dom";
import TextareaAutosize from "react-textarea-autosize";
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

  const words = utilsService.extractWordsFromInput(text);

  const sendWords = useRef((forceText?: string) => {});
  sendWords.current = async (forceText?: string) => {
    const searchText = forceText || text;
    if (utilsService.extractWordsFromInput(searchText).length === 0) return;

    setIsLoading(true);
    setErrorOccurred(false);
    setSearchParams({ words: searchText });

    const wordsToSend: string[] = utilsService.extractWordsFromInput(searchText);
    const queryParams: QueryParams = { words: JSON.stringify(wordsToSend) };

    try {
      const resp = await httpService.makeGetRequest("/words", queryParams);
      setWordList(resp);
    } catch (error) {
      setErrorOccurred(true);
    } finally {
      setIsLoading(false);
    }
  };

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

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    sendWords.current();
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendWords.current();
    }
  };

  return (
    <form className="input-form" onSubmit={handleSubmit}>
      <TextareaAutosize
        name="main-input"
        className="main-input ja"
        value={text}
        minRows={2}
        placeholder="Type or paste Japanese words, separated by spaces or line breaks"
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={isLoading}
      />
      <div className="input-footer">
        <div className="word-chips">
          {words.map((word, index) => (
            <span key={index} className="chip ja">
              {word}
            </span>
          ))}
        </div>
        <button
          className="button"
          type="submit"
          disabled={isLoading || words.length === 0}
        >
          {isLoading ? <LoadingSpinner /> : "Fetch"}
        </button>
      </div>
      <p className="input-hint">Press Enter to fetch, Shift + Enter for a new line.</p>
    </form>
  );
};

export default InputBox;
