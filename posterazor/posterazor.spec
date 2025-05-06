Name:           posterazor
Version:        1.5
Release:        25%{?dist}
Summary:        Make your own poster

Group:          Applications/Publishing
License:        GPLv3+
URL:            https://%{name}.sourceforge.net/index.php
Source0:        https://prdownloads.sourceforge.net/%{name}/PosteRazor-%{version}-Source.zip
Source1:        %{name}.desktop
Patch0:         %{name}-%{version}-includes.patch
Patch1:         posterazor-1.5-format-security.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake freeimage-devel fltk-devel libXpm-devel
BuildRequires:  desktop-file-utils

%description
The PosteRazor cuts a raster image into pieces which can afterwards be
printed out and assembled to a poster. As input, the PosteRazor takes a
raster image. The resulting poster is saved as a multipage PDF document.
An easy to use, wizard like user interface guides through 5 steps.

%prep
%setup -q -c
%patch 0 -p1 -b .includes
%patch 1 -p1 -b .formatsec
for i in CHANGES LICENSE README
do
 sed -e 's/\r//' $i > $i.tmp
 touch -c -r $i $i.tmp
 mv $i.tmp $i
done

# Add default constructor for translation classes (required by GCC 4.6)
for i in French English German Italian Dutch BrazilianPortuguese
do
 sed -i -e "/public:/a Translation$i\(\){}" src/Translation$i.h
done 

# To build with GCC 4.7
sed -i -e '/PosteRazorWizardDialogController.h/a#include <unistd.h>' src/FlPosteRazorDialog.h

%build
cd src
%__cmake .
%__make %VERBOSE=1 %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
install -pm 755 src/PosteRazor  $RPM_BUILD_ROOT/%{_bindir}
install -Dm 644 -p src/PosteRazor.xpm  $RPM_BUILD_ROOT%{_datadir}/pixmaps/
desktop-file-install --vendor="" \
  --mode 644 \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
  %{SOURCE1}


%files
%doc CHANGES LICENSE README
%{_bindir}/PosteRazor
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/PosteRazor.xpm


%changelog
* Sat Nov 13 2021 Martin RS - 1.5-25
- for Fedora 35
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5-17
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.5-16
- rebuild (fltk)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5-14
- Fix FTBFS with -Werror=format-security (#1037255, #1106663)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.5-9
- Fix include to build with gcc 4.7
* Thu May 26 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.5-8
- Rebuild for new libfltk
* Sun Feb 13 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.5-7
- Add default constructor for Translation classes
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Sat Feb 28 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.5-4
- Fix desktop file
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Oct 29 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.5-2
- add desktop file
* Thu Oct 23 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> - 1.5-1
- initial build
