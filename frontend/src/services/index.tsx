import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const Tags = {
  User: 'User',
};

export const tags = [Tags.User];

export const parseErrorResponse = (error: any) => {
  if (
    typeof error === 'object' &&
    'data' in error &&
    typeof error.data === 'object' &&
    error.data &&
    'detail' in error.data &&
    typeof error.data.detail === 'string'
  ) {
    return error.data.detail;
  }

  return '';
};

const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  endpoints: () => ({}),
  tagTypes: tags,
});

export default api;
