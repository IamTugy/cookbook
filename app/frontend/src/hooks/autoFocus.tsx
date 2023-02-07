import React, { useRef, useEffect } from "react";

const useAutoFocus = () => {
  const inputRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    if (inputRef.current) {
      inputRef?.current.scrollIntoView();
    }
  }, [inputRef]);

  return inputRef;
};

export default useAutoFocus;
