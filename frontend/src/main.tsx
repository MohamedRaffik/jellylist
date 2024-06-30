import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { Provider } from 'react-redux';
import { MantineProvider } from '@mantine/core';

import App from './App.tsx';
import store from './store.ts';
import theme from './theme.ts';

import '@mantine/core/styles.css';
import Login from './pages/Login.tsx';

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    children: [
      {
        path: 'dashboard',
        element: <p style={{ color: 'white' }}>Dashboard</p>,
      },
      {
        path: 'media',
        element: <p style={{ color: 'white' }}>Media</p>,
      },
      {
        path: 'playlists',
        element: <p style={{ color: 'white' }}>Playlists</p>,
      },
      {
        path: 'users',
        element: <p style={{ color: 'white' }}>Users</p>,
      },
    ],
  },
  {
    path: '/login',
    element: <Login />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <MantineProvider theme={theme} defaultColorScheme="dark">
      <Provider store={store}>
        <RouterProvider router={router} />
      </Provider>
    </MantineProvider>
  </React.StrictMode>
);
