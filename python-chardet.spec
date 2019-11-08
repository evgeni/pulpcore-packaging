# Created by pyp2rpm-3.3.3
%global pypi_name chardet

Name:           python-%{pypi_name}
Version:        3.0.4
Release:        1%{?dist}
Summary:        Universal encoding detector for Python 2 and 3

License:        LGPL
URL:            https://github.com/chardet/chardet
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Chardet: The Universal Character Encoding Detector -- - ASCII, UTF-8, UTF-16 (2
variants), UTF-32 (4 variants)

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-setuptools
%description -n python3-%{pypi_name}
Chardet: The Universal Character Encoding Detector -- - ASCII, UTF-8, UTF-16 (2
variants), UTF-32 (4 variants)

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
%doc docs/README.md README.rst tests/README.txt
%exclude %{_bindir}/chardetect
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 3.0.4-1
- Initial package.
