# Created by pyp2rpm-3.3.3
%global pypi_name setuptools

Name:           python-%{pypi_name}
Version:        41.4.0
Release:        1%{?dist}
Summary:        Easily download, build, install, upgrade, and uninstall Python packages

License:        None
URL:            https://github.com/pypa/setuptools
Source0:        %{pypi_source %{pypi_name} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
 .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-setuptools
%description -n python3-%{pypi_name}
 .. image::

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove bundled exes
rm -f setuptools/*.exe

%build
%{__python3} bootstrap.py

%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/easy_install
%{_bindir}/easy_install-%{python3_version}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/easy_install.py
%{python3_sitelib}/pkg_resources
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Nov 08 2019 Evgeni Golov - 41.4.0-1
- Initial package.
