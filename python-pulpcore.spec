# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore

Name:           python-%{pypi_name}
Version:        3.0.0rc7
Release:        1%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
[![Build Status]( [![PyPI]( [![codecov]( [![Code Quality: Python]( [![Total
Alerts](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-coreapi >= 2.3.3
Requires:       python3-djangorestframework-queryfields >= 1.0.0
Requires:       python3-drf-nested-routers >= 0.91
Requires:       python3-drf-yasg >= 1.17.0
Requires:       python3-psycopg2
Requires:       python3-rq >= 1.1.0
Requires:       python3-django >= 2.2.3
Requires:       python3-django-filter >= 2.2.0
Requires:       python3-django-rest-framework >= 3.10.2
Requires:       python3-dynaconf >= 2.1.0
Requires:       python3-gunicorn >= 19.9.0
Requires:       python3-pyyaml >= 5.1.1
Requires:       python3-redis >= 3.1.0
Requires:       python3-setuptools
Requires:       python3-whitenoise >= 4.1.3
%description -n python3-%{pypi_name}
[![Build Status]( [![PyPI]( [![codecov]( [![Code Quality: Python]( [![Total
Alerts](

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's/psycopg2-binary/psycopg2/g' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pulp-content
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 3.0.0rc7-1
- Initial package.
