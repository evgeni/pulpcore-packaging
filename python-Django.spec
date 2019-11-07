# Created by pyp2rpm-3.3.3
%global pypi_name Django

Name:           python-%{pypi_name}
Version:        2.2.7
Release:        1%{?dist}
Summary:        A high-level Python Web framework that encourages rapid development and clean, pragmatic design

License:        BSD
URL:            https://www.djangoproject.com/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.All documentation is in
the "docs" directory and online at If you're just getting started, here's how
we recommend you read the docs:* First, read docs/intro/install.txt for
instructions on installing Django.* Next, work through the tutorials in
order...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-argon2-cffi >= 16.1.0
Requires:       python3-bcrypt
Requires:       python3-pytz
Requires:       python3-setuptools
Requires:       python3-sqlparse
%description -n python3-%{pypi_name}
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.All documentation is in
the "docs" directory and online at If you're just getting started, here's how
we recommend you read the docs:* First, read docs/intro/install.txt for
instructions on installing Django.* Next, work through the tutorials in
order...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license django/dispatch/license.txt django/contrib/gis/gdal/LICENSE django/contrib/gis/geos/LICENSE django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE.txt django/contrib/admin/static/admin/js/vendor/jquery/LICENSE.txt django/contrib/admin/static/admin/js/vendor/select2/LICENSE.md django/contrib/admin/static/admin/css/vendor/select2/LICENSE-SELECT2.md django/contrib/admin/static/admin/fonts/LICENSE.txt django/contrib/admin/static/admin/img/LICENSE docs/_theme/djangodocs/static/fontawesome/LICENSE.txt LICENSE LICENSE.python
%doc django/contrib/admin/static/admin/fonts/README.txt django/contrib/admin/static/admin/img/README.txt docs/_theme/djangodocs/static/fontawesome/README.md tests/README.rst README.rst extras/README.TXT
%{_bindir}/django-admin
%{_bindir}/django-admin.py
%{python3_sitelib}/django
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 2.2.7-1
- Initial package.
