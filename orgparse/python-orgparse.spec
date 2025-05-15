%{?!python3_pkgversion:%global python3_pkgversion 3}

%define _ver 0.4
%global srcname orgparse

%global _gitcommit da56aae64a6373ae8bab2dde9dc756f904f1d8f8
%global _gitdate 20231004

Name:           python-orgparse
Version:        %{_ver}git%{_gitdate}
Release:        1%{?dist}
Summary:        Python module for reading Emacs org-mode files
License:        BSD2-Clause
URL:            https://github.com/karlicoss/orgparse/
Source0:        https://github.com/karlicoss/orgparse/archive/%{_gitcommit}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# @note the following are for making html doc and pytest but has issues
#BuildRequires:  make graphviz
#BuildRequires:  python%{python3_pkgversion}-cogapp
#BuildRequires:  python%{python3_pkgversion}-pytest
#BuildRequires:  python%{python3_pkgversion}-sphinx

%generate_buildrequires
%pyproject_buildrequires -r

%description
%{summary}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
%autosetup -p1 -n %{srcname}-%{_gitcommit}
sed -i pyproject.toml \
  -e 's/dynamic.*"version".*/version = "%{_ver}"/' \
  -e '/^requires.*"setuptools-scm"/s/,\s\+"setuptools-scm"//'
sed -i src/orgparse/__init__.py \
  -e '/^__all__ =/i__version__ = "%{_ver}"' \
  -e '/..\/README.rst/s/README/..\/README/'
sed -i Makefile -e 's/cog.py/cog/g'


%build
%pyproject_wheel


%install
rm -rf $RPM_BUILD_ROOT
%pyproject_install


#%check
#export PYTHONPATH=${RPM_BUILD_ROOT}%{python3_sitearch}:
#%pytest || :

%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{_ver}.dist-info/


%changelog
* Fri May  3 2024 Martin RS - 0.4git20231004
- update 
