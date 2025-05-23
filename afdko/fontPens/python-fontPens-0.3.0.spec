%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname fontPens

Name:           python-fontPens
Version:        0.3.0
Release:        1%{?dist}
Summary:        implement the pen protocol for manipulating glyphs
License:        BSD
URL:            https://github.com/robotools/fontPens
Source0:        https://github.com/robotools/fontPens/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-fonttools >= 3.32.0
BuildRequires:  python%{python3_pkgversion}-fontParts >= 0.8.4
BuildRequires:  python%{python3_pkgversion}-pytest-runner

%{?python_enable_dependency_generator}

%define _description %{expand:
A collection of classes implementing the pen protocol for manipulating
glyphs.}
%description
%_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif
#Requires:  python%{python3_pkgversion}-fonttools >= 3.32.0
#Requires:  python%{python3_pkgversion}-fontParts >= 0.8.4


%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i Lib/fontPens/penTools.py \
  -e 's/107\.70329614269008/107\.70329614269009/'
grep -l -R -e 'version.*=.*0\.2\.5\.dev0' | while read f; do \
  sed -i $f -e 's/0\.2\.5\.dev0/%{version}/'; done


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
%{__python3} -m pytest


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed May 21 2025 Martin RS - 0.3.0
- update
* Fri Nov 12 2021 Martin RS - 0.2.4
- Initial for Fedora
