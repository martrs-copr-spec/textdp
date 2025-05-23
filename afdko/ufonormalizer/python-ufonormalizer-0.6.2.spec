%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname ufoNormalizer
%global lowname ufonormalizer

%define _description %{expand:
Provides a standard formatting so that there are meaningful diffs in
version control rather than formatting noise.

Examples of formatting applied by ufoNormalizer include:
    Changing floating-point numbers to integers where it doesn't alter
        the value (e.g. x="95.0" becomes x="95" )
    Rounding floating-point numbers to 10 digits
    Formatting XML with tabs rather than spaces
}

Name:           python-ufonormalizer
Version:        0.6.2
Release:        1%{?dist}
Summary:        A tool that will normalize XML and other data inside of a UFO
License:        BSD-3-Clause
URL:            https://github.com/unified-font-object/ufoNormalizer
Source0:        https://github.com/unified-font-object/ufoNormalizer/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pytest

%{?python_enable_dependency_generator}

%description
%_description


%package -n python%{python3_pkgversion}-%{lowname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{lowname}}

%description -n python%{python3_pkgversion}-%{lowname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%py3_install


%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
# use what your upstream is using
PYTHONPATH=build/lib %{__python3} -m pytest


%files -n  python%{python3_pkgversion}-%{lowname}
%license LICENSE.txt
%doc README.md
%{_bindir}/%{lowname}
# For noarch packages: sitelib
%{python3_sitelib}/%{lowname}/
%{python3_sitelib}/%{lowname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 20 2025 Martin RS - 0.6.2
- Update
* Thu Nov 11 2021 Martin RS - 0.6.1
- Initial for Fedora
