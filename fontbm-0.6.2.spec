%global _gitcommit 7b49ddb4ed8b1ed227f668ea54bc5240bf66517c
%global _gitdate   20250307

%global _package_note_flag %nil

Name:           fontbm
Version:        0.6.2git%{_gitdate}
Release:        1%{?dist}

Summary:        command line bitmap font generator

Group:          Utilities/Font
License:        MIT
Source0:        https://github.com/vladimirgamalyan/fontbm/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake pkgconfig pkgconfig(freetype2) gcc-c++

%description
BMFont compatible, command line bitmap font generator

%prep
%autosetup -n %{name}-%{_gitcommit}
sed -i src/FontInfo.h -e '/^#include.*string/a#include <cstdint>'


%build
%cmake
%cmake_build


%install
%{__install} %{__cmake_builddir}/fontbm -D -t %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/fontbm
cp -pr tests %{buildroot}%{_datadir}/fontbm/

%files
%license LICENSE
%doc README.md
%{_bindir}/fontbm
%{_datadir}/fontbm/*


%changelog
* Mon May  5 2025 Martin RS - 0.6.2git20250307
- update
* Fri May  3 2024 Martin RS - 0.6.2git20230525
- update
* Wed Feb 15 2023 Martin RS - 0.6.2git20230113
- update
* Fri Nov 12 2021 Martin RS - 0.3.1git20210221
- update
* Sat Jun 27 2020 Martin RS - 0.1.8git20200516
- Fedora
