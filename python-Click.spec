# Created by pyp2rpm-3.3.3
%global pypi_name Click

Name:           python-%{pypi_name}
Version:        7.0
Release:        1%{?dist}
Summary:        Composable command line interface toolkit

License:        BSD
URL:            https://palletsprojects.com/p/click/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
\$ click\_ Click is a Python package for creating beautiful command line
interfaces in a composable way with as little code as necessary. It's the
"Command Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box.It aims to make the process of writing command
line tools quick and fun while also preventing any frustration caused by the
inability to...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
\$ click\_ Click is a Python package for creating beautiful command line
interfaces in a composable way with as little code as necessary. It's the
"Command Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box.It aims to make the process of writing command
line tools quick and fun while also preventing any frustration caused by the
inability to...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitelib}/click
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 7.0-1
- Initial package.
