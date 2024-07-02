import { Link, Outlet, useLocation, useNavigate } from 'react-router-dom';
import {
  AppShell,
  Burger,
  Group,
  LoadingOverlay,
  NavLink,
  Stack,
  Title,
} from '@mantine/core';
import { useDisclosure, useMediaQuery } from '@mantine/hooks';
import { FunctionComponent, useEffect } from 'react';

import { useGetSessionUserQuery } from './services/users';

type CustomNavLinkProps = {
  label: string;
  pathname: string;
  toggle: () => void;
};

const CustomNavLink: FunctionComponent<CustomNavLinkProps> = (props) => {
  const { pathname, toggle, label } = props;

  const isMobile = useMediaQuery(`(max-width: 768px)`);

  const location = useLocation();

  return (
    <NavLink
      label={label}
      component={Link}
      to={pathname}
      active={location.pathname.startsWith(pathname)}
      onClick={() => {
        if (isMobile) toggle();
      }}
    />
  );
};

const App = () => {
  const { isError, isLoading } = useGetSessionUserQuery();

  const [opened, { toggle }] = useDisclosure(false);

  const isMobile = useMediaQuery(`(max-width: 768px)`);

  const navigate = useNavigate();

  useEffect(() => {
    if (!isLoading && isError) {
      navigate('/login');
    }
  }, [isLoading, isError]);

  if (isLoading) {
    return <LoadingOverlay visible={true} />;
  }

  return (
    <AppShell
      header={{ height: 60, collapsed: !isMobile }}
      navbar={{
        width: 300,
        breakpoint: 'sm',
        collapsed: { mobile: !opened },
      }}
      padding="md"
    >
      <AppShell.Header hiddenFrom="sm">
        <Burger opened={opened} onClick={toggle} hiddenFrom="sm" size="sm" />
      </AppShell.Header>
      <AppShell.Navbar p="md">
        <Stack>
          <Group>
            <Title>JellyList</Title>
          </Group>
          <CustomNavLink
            label="Dashboard"
            pathname="/dashboard"
            toggle={toggle}
          />
          <CustomNavLink
            label="Playlists"
            pathname="/playlists"
            toggle={toggle}
          />
          <CustomNavLink label="Media" pathname="/media" toggle={toggle} />
          <CustomNavLink label="Users" pathname="/users" toggle={toggle} />
        </Stack>
      </AppShell.Navbar>
      <AppShell.Main>
        <Outlet />
      </AppShell.Main>
    </AppShell>
  );
};

export default App;
