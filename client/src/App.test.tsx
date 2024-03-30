import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders title', () => {
  render(<App />);
  const linkElement = screen.getByText(/Japanese Vocab Fetcher/i);
  expect(linkElement).toBeInTheDocument();
});

test('API_URL works', () => {
  expect(process.env.API_URL).not.toBeUndefined()
  expect(process.env.BPI_URL).toBeUndefined()
})
