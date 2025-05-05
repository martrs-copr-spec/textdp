%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname unicodedata2

Name:           python-unicodedata2
Version:        16.0.0
Release:        1%{?dist}
Summary:        Python unicodedata backport/updates
License:        Apache-2.0
URL:            https://github.com/fonttools/unicodedata2
Source0:        https://github.com/fonttools/unicodedata2/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc glibc-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest

%global _description %{expand:
Unicodedata backport for python 2/3 updated to the latest unicode version.}

%{?python_enable_dependency_generator}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
# use what your upstream is using
%{__python3} -m pytest || :

%files
%doc README.md
%license LICENSE
%{python3_sitearch}/%{srcname}.cpython*.so
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun May  4 2025 Martin RS - 16.0.0
- update
* Fri May  3 2024 Martin RS - 15.1.0
- update
* Wed Feb 15 2023 Martin RS - 15.0.0
- update
* Thu Nov 19 2020 Martin RS - 13.0.0-2
- initial for Fedora
