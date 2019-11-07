# Created by pyp2rpm-3.3.3
%global pypi_name urllib3

Name:           python-%{pypi_name}
Version:        1.25.6
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
 :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Conflicts:      python3-pysocks = 1.5.7
Requires:       python3-brotlipy >= 0.6.0
Requires:       python3-ipaddress
Requires:       python3-certifi
Requires:       python3-cryptography >= 1.3.4
Requires:       python3-idna >= 2.0.0
Requires:       python3-pyOpenSSL >= 0.14
Requires:       python3-pysocks < 2.0
Requires:       python3-pysocks >= 1.5.6
%description -n python3-%{pypi_name}
 :target:

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst dummyserver/certs/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 1.25.6-1
- Initial package.
