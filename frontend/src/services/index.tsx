import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const Tags = {
  User: 'User',
};

export const tags = [Tags.User];

const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  endpoints: () => ({}),
  tagTypes: tags,
});

export default api;
