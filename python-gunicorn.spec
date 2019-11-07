# Created by pyp2rpm-3.3.3
%global pypi_name gunicorn

Name:           python-%{pypi_name}
Version:        19.9.0
Release:        1%{?dist}
Summary:        WSGI HTTP Server for UNIX

License:        MIT
URL:            http://gunicorn.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
-- Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-
fork worker model ported from Ruby's Unicorn_ project. The Gunicorn server is
broadly compatible with various web frameworks, simply implemented, light on
server

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-eventlet >= 0.9.7
Requires:       python3-gevent >= 0.13
Requires:       python3-tornado >= 0.2
%description -n python3-%{pypi_name}
-- Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-
fork worker model ported from Ruby's Unicorn_ project. The Gunicorn server is
broadly compatible with various web frameworks, simply implemented, light on
server

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc docs/README.rst README.rst
%{_bindir}/gunicorn
%{_bindir}/gunicorn_paster
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 19.9.0-1
- Initial package.
