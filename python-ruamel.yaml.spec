# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml

Name:           python-%{pypi_name}
Version:        0.16.5
Release:        1%{?dist}
Summary:        ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order

License:        MIT license
URL:            https://bitbucket.org/ruamel/yaml
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
ruamel.yaml ruamel.yaml is a YAML 1.2 loader/dumper package for
Python.:version: 0.16.5 :updated: 2019-08-18 :documentation: :repository:
:pypi: Starting with version 0.15.0 the way YAML files are loaded and dumped is
changing. See the API doc for details. Currently existing functionality will
throw a warning before being changed/removed. **For production systems you
should pin the version...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-ruamel-ordereddict
Requires:       python3-ruamel-yaml-jinja2 >= 0.2
Requires:       python3-ryd
Requires:       python3-ruamel-yaml-clib >= 0.1.2
%description -n python3-%{pypi_name}
ruamel.yaml ruamel.yaml is a YAML 1.2 loader/dumper package for
Python.:version: 0.16.5 :updated: 2019-08-18 :documentation: :repository:
:pypi: Starting with version 0.15.0 the way YAML files are loaded and dumped is
changing. See the API doc for details. Currently existing functionality will
throw a warning before being changed/removed. **For production systems you
should pin the version...

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
%doc README.rst
%{python3_sitelib}/ruamel
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 0.16.5-1
- Initial package.
