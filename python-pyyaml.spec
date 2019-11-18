# Created by pyp2rpm-3.3.3
%global pypi_name PyYAML
%global srcname pyyaml

Name:           python-%{srcname}
Version:        5.1.2
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            https://github.com/yaml/pyyaml
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libyaml-devel

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?rhel} == 8
BuildRequires:  python3-Cython
%endif

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}

chmod a-x examples/yaml-highlight/yaml_hl.py

# remove pre-generated file
rm -rf ext/_yaml.c

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitearch}/*

%changelog
* Mon Nov 18 2019 Evgeni Golov - 5.1.2-1
- Initial package.
