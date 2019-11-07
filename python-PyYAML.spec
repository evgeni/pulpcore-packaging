# Created by pyp2rpm-3.3.3
%global pypi_name PyYAML

Name:           python-%{pypi_name}
Version:        5.1.2
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            https://github.com/yaml/pyyaml
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  libyaml-devel

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?rhel} == 8
BuildRequires:  python3-Cython
%endif

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages. PyYAML is a YAML parser and emitter for
Python.PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages. PyYAML supports
standard YAML tags and provides Python-specific tags that allow to represent an
arbitrary...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
YAML is a data serialization format designed for human readability and
interaction with scripting languages. PyYAML is a YAML parser and emitter for
Python.PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages. PyYAML supports
standard YAML tags and provides Python-specific tags that allow to represent an
arbitrary...

%prep
%autosetup -n %{pypi_name}-%{version}

chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitearch}/*

%changelog
* Thu Nov 07 2019 Evgeni Golov - 5.1.2-1
- Initial package.