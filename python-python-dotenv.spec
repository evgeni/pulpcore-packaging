# Created by pyp2rpm-3.3.3
%global pypi_name python-dotenv
%global srcname dotenv

Name:           python-%{srcname}
Version:        0.10.3
Release:        1%{?dist}
Summary:        Add .env support to your django/flask apps in development and deployments

License:        None
URL:            http://github.com/theskumar/python-dotenv
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
 _______ .__ __. ____ ____ | ____|| \ | | \ \ / / | |__ | \| | \ \/ / | __| | .
| \ / __ | |____ | |\ | \ / (__)|_______||__| \__| \__/python-dotenv | [![Build
Status]( [![Coverage Status]( [![PyPI version]( [![Say Thanks!](

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3-typing
Requires:       python3-click >= 5.0
%description -n python3-%{srcname}
 _______ .__ __. ____ ____ | ____|| \ | | \ \ / / | |__ | \| | \ \/ / | __| | .
| \ / __ | |____ | |\ | \ / (__)|_______||__| \__| \__/python-dotenv | [![Build
Status]( [![Coverage Status]( [![PyPI version]( [![Say Thanks!](

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{_bindir}/dotenv
%{python3_sitelib}/dotenv
%{python3_sitelib}/python_dotenv-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 0.10.3-1
- Initial package.
