# Created by pyp2rpm-3.3.3
%global pypi_name MarkupSafe

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
MarkupSafe MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are replaced
so that they display as the actual characters. This mitigates injection
attacks, meaning untrusted user input can safely be displayed on a page.
Installing -Install and update using pip_:.. code-block:: text pip install -U
MarkupSafe.....

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       python3-markupsafe
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MarkupSafe MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are replaced
so that they display as the actual characters. This mitigates injection
attacks, meaning untrusted user input can safely be displayed on a page.
Installing -Install and update using pip_:.. code-block:: text pip install -U
MarkupSafe.....

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
%{python3_sitearch}/markupsafe
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 1.1.1-1
- Initial package.
