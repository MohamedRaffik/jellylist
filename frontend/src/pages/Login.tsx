import {
  Alert,
  AppShell,
  Button,
  Group,
  LoadingOverlay,
  PasswordInput,
  Stack,
  TextInput,
  Title,
} from '@mantine/core';
import { useForm } from '@mantine/form';

import { useLoginMutation } from '../services/users';
import { useMemo } from 'react';
import { parseErrorResponse } from '../services';

const Login = () => {
  const [login, { error, isError, isLoading }] = useLoginMutation();

  const form = useForm({
    mode: 'uncontrolled',
    initialValues: {
      email: '',
      password: '',
    },
    validate: {
      email: (value) => (value.includes('@') ? null : 'Invalid email'),
      password: (value) =>
        value.length > 8 ? null : 'Password should be at least 8 characters',
    },
  });

  const errorMessage = useMemo(() => parseErrorResponse(error), [error]);

  return (
    <AppShell header={{ height: 60 }} padding="md">
      <AppShell.Header px="md">
        <Group>
          <Title>JellyList</Title>
        </Group>
      </AppShell.Header>
      <AppShell.Main>
        <Group w="50vw" mx="auto">
          <LoadingOverlay visible={isLoading} />
          <form onSubmit={form.onSubmit(login)} style={{ width: '100%' }}>
            <Stack
              gap="md"
              p="md"
              bd="1px solid violet"
              style={{ borderRadius: '4px' }}
            >
              <Title order={3}>Login</Title>
              {isError && errorMessage && (
                <Alert variant="light" color="red" title="Error">
                  {errorMessage}
                </Alert>
              )}
              <TextInput
                width="50vw"
                label="Email"
                placeholder="Email"
                withAsterisk
                key={form.key('email')}
                {...form.getInputProps('email')}
              />
              <PasswordInput
                label="Password"
                placeholder="Password"
                type="password"
                withAsterisk
                key={form.key('password')}
                {...form.getInputProps('password')}
              />
              <Group justify="end">
                <Button type="submit" variant="light">
                  Login
                </Button>
              </Group>
            </Stack>
          </form>
        </Group>
      </AppShell.Main>
    </AppShell>
  );
};

export default Login;
