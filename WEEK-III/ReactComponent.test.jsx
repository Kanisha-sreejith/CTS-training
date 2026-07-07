import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import UserProfile from './ReactComponent';

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ name: 'Test User', email: 'test@example.com' }),
  })
);

test('loads and displays user on button click', async () => {
  render(<UserProfile />);

  fireEvent.click(screen.getByText('Load User'));

  expect(screen.getByText('Loading...')).toBeInTheDocument();

  const nameElement = await screen.findByText('Name: Test User');
  const emailElement = await screen.findByText('Email: test@example.com');

  expect(nameElement).toBeInTheDocument();
  expect(emailElement).toBeInTheDocument();
});

afterEach(() => {
  jest.clearAllMocks();
});
