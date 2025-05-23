%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname afdko
%global antl4_ver 4.13.2

Name:		adobe-afdko
Version:	4.0.2
Release:	1%{?dist}
Summary:	Adobe Font Development Kit for OpenType
# ExternalAntlr4Cpp.cmake is BSD-3-clause
# c/makeotf/makeotf_lib/build/hotpccts/pccts/* is ANTLR-PD
# afdko-3.6.1/python/afdko/pdflib/pdfgen.py is Python-2.0.1
# python/afdko/resources/ is BSD-3-Clause
License:	Apache-2.0 AND BSD-3-Clause AND ANTLR-PD AND Python-2.0.1
URL:		https://github.com/adobe-type-tools/afdko
Source0:	https://github.com/adobe-type-tools/%{srcname}/releases/download/%{version}/%{srcname}-%{version}.tar.gz
Source1:        https://www.antlr.org/download/antlr4-cpp-runtime-%{antl4_ver}-source.zip

BuildRequires:	gcc g++
BuildRequires:	make
BuildRequires:  python%{python3_pkgversion}-cmake
BuildRequires:  python%{python3_pkgversion}-ninja
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel
BuildRequires:	utf8cpp-devel
Provides: bundled(antlr4-project) = %{antl4_ver}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-wheel >= 0.33.1
BuildRequires:  python%{python3_pkgversion}-booleanoperations >= 0.9.0
BuildRequires:  python%{python3_pkgversion}-defcon+lxml >= 0.10.3
BuildRequires:  python%{python3_pkgversion}-defcon+pens >= 0.10.3
BuildRequires:  python%{python3_pkgversion}-fontMath >= 0.9.3
BuildRequires:  python%{python3_pkgversion}-fonttools+lxml >= 4.43.0
BuildRequires:  python%{python3_pkgversion}-fonttools+ufo >= 4.43.0
BuildRequires:  python%{python3_pkgversion}-fonttools+unicode >= 4.43.0
BuildRequires:  python%{python3_pkgversion}-fonttools+woff >= 4.43.0
BuildRequires:  python%{python3_pkgversion}-scikit-build >= 0.11.1
BuildRequires:  python%{python3_pkgversion}-tqdm >= 4.66.1
BuildRequires:  python%{python3_pkgversion}-ufonormalizer >= 0.6.1
BuildRequires:  python%{python3_pkgversion}-ufoProcessor >= 1.9.0

BuildRequires:  python%{python3_pkgversion}-codecov >= 2.0.15
BuildRequires:  python%{python3_pkgversion}-Cython >= 0.29.5
BuildRequires:  python%{python3_pkgversion}-flake8 >= 3.7.6
#BuildRequires:  python%{python3_pkgversion}-flake8-bugbear >= 20.1.4
BuildRequires:  python%{python3_pkgversion}-pytest-cov >= 2.6.1
BuildRequires:  python%{python3_pkgversion}-pytest-xdist >= 2.5.0

Requires: python%{python3_pkgversion}-%{srcname}

%{?python_enable_dependency_generator}

%define _description %{expand:
Adobe Font Development Kit for OpenType (AFDKO).
The AFDKO is a set of tools for building OpenType font files
from PostScript and TrueType font data.}

%description
%_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
cp %{SOURCE1} .
sed -i CMakeLists.txt \
  -e '/set(CMAKE_CXX_STANDARD 11/s/11/17/' \
  -e 's/^#\? \(set(ANTLR.*REPOSITORY\) ".*"/\1 "\${CMAKE_CURRENT_SOURCE_DIR}\/antlr4-cpp-runtime-%{antl4_ver}-source.zip"/'
sed -i cmake/ExternalAntlr4Cpp.cmake \
  -e '/CMAKE_CACHE_ARGS/a          -DANTLR_BUILD_CPP_TESTS:BOOL=OFF' \
  -e '/set(ANTLR4_OUTPUT_DIR.*dist)/s/dist/runtime/'

%build
%set_build_flags
export XFLAGS="${CFLAGS} ${LDFLAGS}"
#%cmake
#%cmake_build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%py3_install
#%cmake_install


%check
# use what your upstream is using
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PATH=/usr/bin:/usr/sbin:%{buildroot}%{_bindir}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export TMPDIR=`pwd`/tmp; mkdir $TMPDIR
#%{__python3} -m pytest -v --verbosity=1 || :


%files
%license LICENSE.md
%doc docs/ README.md NEWS.md
%{_bindir}/*


%files -n  python%{python3_pkgversion}-%{srcname}
# For arch-specific packages: sitearch
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Thu May 22 2025 Martin RS - 4.0.2
- update, also build for python
- bundled antlr4-cpp-runtime-4.13.2, fix build

* Tue Jun 25 2024 Manish Tiwari <matiwari@redhat.com> - 4.0.1-1
- Updated to 4.0.1 release
- Switched to CMake build system 
- Bundled antlr4-cpp-runtime-4.9.3

* Fri May 03 2024 Martin RS - 3.6.2
- update, also build for python

* Thu Jan 25 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 3.6.1-10
- Fix a typo in the License expression
- Fix build not respecting distribution compiler flags; this means executables
  are now PIE, and the debuginfo package is now useful

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 3.6.1-7
- Fix C compatibility issues

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.6.1-1
- Build for latest 3.6.1 release

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.5.1-1
- Build for latest release 3.5.1

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.4.0-1
- Build for latest release 3.4.0

* Mon May 18 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.3.0-1
- Build for latest release 3.3.0

* Sat May 09 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.2.0-2
- undo the change 'Rename makeotfexe to makeotf'

* Fri Apr 3 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.2.0-1
- Build for latest release

* Mon Mar 23 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-4
- rename package name afdko to adobe-afdko

* Mon Mar 9 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-3
- Added %%set_build_flags
- Updated install script

* Mon Mar 2 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-2
- Added build dependency gcc, make
- Removed unused build dependency
- Rename makeotfexe to makeotf

* Fri Dec 13 2019 Peng Wu <pwu@redhat.com> - 3.0.1-1
- Initial Version
