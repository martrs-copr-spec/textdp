%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname fontParts

Name:           python-%{srcname}
Version:        0.12.5
Release:        1%{?dist}
Summary:        API for interacting with the parts of fonts
License:        MIT
URL:            https://github.com/robotools/%{srcname}
Source0:        https://github.com/robotools/%{srcname}/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-pytest
# was ==0.9.4
BuildRequires:  python%{python3_pkgversion}-fontMath >= 0.6.0
BuildRequires:  python%{python3_pkgversion}-booleanoperations >= 0.9.0
# was ==0.10.3
BuildRequires:  python%{python3_pkgversion}-defcon >= 0.10.2
# was ==4.55.2
BuildRequires:  python%{python3_pkgversion}-fonttools+ufo >= 4.50.0
BuildRequires:  python%{python3_pkgversion}-fonttools+lxml >= 4.50.0
BuildRequires:  python%{python3_pkgversion}-fonttools+unicode >= 4.50.0

%{?python_enable_dependency_generator}

%global _description %{expand:
An API for interacting with the parts of fonts during the font development process.}
%description
%_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i setup.py \
  -e 's/[fF]ont[tT]ools[^>]*>=/fonttools>=/' \
  -e 's/defcon[^>]*>=/defcon>=/'


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%py3_install


%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
# issue with circular dependency
#PYTHONPATH=Lib %{__python3} -m pytest


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc documentation CONTRIBUTING.rst NEWS.rst README.rst
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Sun May  4 2025 Martin RS - 0.12.5
- update
* Fri May  3 2024 Martin RS - 0.12.1
- update
* Wed Feb 15 2023 Martin RS - 0.11.0
- initial for Fedora
