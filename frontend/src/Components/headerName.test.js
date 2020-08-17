import React from 'react';
import { render, unmountComponentAtNode } from 'react-dom';
import { act } from "react-dom/test-utils";

import Header from "./headerName";



let container = null;
beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});



it("renders with or without a name", () => {
  act(() => {
    render(<Header />, container);
  });
  expect(container.textContent).toBe("Hey there, stranger");

  act(() => {
    render(<Header name="Jenny" />, container);
  });
  expect(container.textContent).toBe("Hey there, Jenny!");

  act(() => {
    render(<Header name="Margaret" />, container);
  });
  expect(container.textContent).toBe("Hey there, Margaret!");
});