# Created by pyp2rpm-3.3.3
%global pypi_name drf-yasg

Name:           python-%{pypi_name}
Version:        1.17.0
Release:        1%{?dist}
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code

License:        BSD License
URL:            https://github.com/axnsan12/drf-yasg
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
.. role:: python(code) :language: python drf-yasg - Yet another Swagger
generator |travis| |nbsp| |codecov| |nbsp| |rtd-badge| |nbsp| |pypi-
version||bmac-button|Generate **real** Swagger/OpenAPI 2.0 specifications from
a Django Rest Framework API.Compatible with- **Django Rest Framework**: 3.8,
3.9, 3.10 - **Django**: 1.11, 2.1, 2.2 - **Python**: 2.7, 3.5, 3.6, 3.7Only the
latest patch...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-coreapi >= 2.3.3
Requires:       python3-coreschema >= 0.0.4
Requires:       python3-inflection >= 0.3.1
Requires:       python3-django >= 1.11.7
Requires:       python3-django-rest-framework >= 3.8
Requires:       python3-packaging
Requires:       python3-ruamel-yaml >= 0.15.34
Requires:       python3-six >= 1.10.0
Requires:       python3-uritemplate >= 3.0.0
%description -n python3-%{pypi_name}
.. role:: python(code) :language: python drf-yasg - Yet another Swagger
generator |travis| |nbsp| |codecov| |nbsp| |rtd-badge| |nbsp| |pypi-
version||bmac-button|Generate **real** Swagger/OpenAPI 2.0 specifications from
a Django Rest Framework API.Compatible with- **Django Rest Framework**: 3.8,
3.9, 3.10 - **Django**: 1.11, 2.1, 2.2 - **Python**: 2.7, 3.5, 3.6, 3.7Only the
latest patch...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license docs/license.rst LICENSE.rst
%doc docs/readme.rst README.rst
%{python3_sitelib}/drf_yasg
%{python3_sitelib}/drf_yasg-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 1.17.0-1
- Initial package.