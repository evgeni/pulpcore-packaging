# Created by pyp2rpm-3.3.3
%global pypi_name pyparsing

Name:           python-%{pypi_name}
Version:        2.4.4
Release:        1%{?dist}
Summary:        Python parsing module

License:        MIT License
URL:            https://github.com/pyparsing/pyparsing/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
PyParsing -- A Python Parsing Module |Build Status|Introduction The pyparsing
module is an alternative approach to creating and executing simple grammars,
vs. the traditional lex/yacc approach, or the use of regular expressions. The
pyparsing module provides a library of classes that client code uses to
construct the grammar directly in Python code.*[Since first writing this
description of...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PyParsing -- A Python Parsing Module |Build Status|Introduction The pyparsing
module is an alternative approach to creating and executing simple grammars,
vs. the traditional lex/yacc approach, or the use of regular expressions. The
pyparsing module provides a library of classes that client code uses to
construct the grammar directly in Python code.*[Since first writing this
description of...

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
%doc examples/0README.html README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 2.4.4-1
- Initial package.