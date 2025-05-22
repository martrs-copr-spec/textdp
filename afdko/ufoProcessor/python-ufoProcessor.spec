%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname ufoProcessor

%define _description %{expand:
Python package based on the designSpaceDocument from
fontTools.designspaceLib specifically to process and generate instances
for UFO files, glyphs and other data.
}

Name:           python-ufoProcessor
Version:        1.13.3
Release:        1%{?dist}
Summary:        Process and generate UFO files
License:        MIT
URL:            https://github.com/LettError/ufoProcessor
Source0:        https://github.com/LettError/ufoProcessor/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-defcon+lxml >= 0.6.0
BuildRequires:  python%{python3_pkgversion}-fontMath >= 0.4.9
BuildRequires:  python%{python3_pkgversion}-fontParts >= 0.8.2
BuildRequires:  python%{python3_pkgversion}-fonttools+lxml >= 3.32.0
BuildRequires:  python%{python3_pkgversion}-fonttools+ufo >= 3.32.0
BuildRequires:  python%{python3_pkgversion}-mutatormath >= 2.1.2
BuildRequires:  python%{python3_pkgversion}-wheel

%{?python_enable_dependency_generator}

%description
%_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
#sed -i setup.py \
#  -e 's/defcon\[.*\]>/defcon>/' -e 's/fontTools\[.*\]>/fonttools>/'


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%py3_install


%check
PYTHONPATH=./Lib %{__python3} Tests/tests.py


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 20 2025 Martin RS - 1.13.3
- update
* Fri Nov 12 2021 Martin RS - 1.9.0
- Initial for Fedora
