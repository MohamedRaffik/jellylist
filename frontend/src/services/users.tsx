import api, { Tags } from '.';
import { User } from '../types/users';

const usersApi = api.injectEndpoints({
  endpoints: (build) => ({
    getSessionUser: build.query<User, void>({
      query: () => ({
        url: '/v1/users/session/',
        method: 'GET',
      }),
      providesTags: [Tags.User],
    }),
  }),
});

export const { useGetSessionUserQuery } = usersApi;
