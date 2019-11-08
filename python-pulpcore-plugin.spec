# Created by pyp2rpm-3.3.3
%global pypi_name pulpcore-plugin

Name:           python-%{pypi_name}
Version:        0.1.0rc7
Release:        1%{?dist}
Summary:        Pulp Plugin API

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
**Pulp Plugin API**The Pulp Plugin API is an essential part of the Pulp Project
3.0+ < which provides a set of base classes that can be implemented in plugins
to manage content in a way that is consistent across plugins, while still
allowing plugin writers the freedom to define their workflows as they deem
necessary.The Pulp Plugin API allows plugin writers: - to easily define your
content...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pulpcore >= 3.0.0rc7
Requires:       python3-aiofiles
Requires:       python3-aiohttp
Requires:       python3-backoff
%description -n python3-%{pypi_name}
**Pulp Plugin API**The Pulp Plugin API is an essential part of the Pulp Project
3.0+ < which provides a set of base classes that can be implemented in plugins
to manage content in a way that is consistent across plugins, while still
allowing plugin writers the freedom to define their workflows as they deem
necessary.The Pulp Plugin API allows plugin writers: - to easily define your
content...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/pulpcore
%{python3_sitelib}/pulpcore_plugin-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Nov 08 2019 Evgeni Golov - 0.1.0rc7-1
- Initial package.
