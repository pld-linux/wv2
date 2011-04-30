#
# http://www.securityfocus.com/bid/18751/info
#
Summary:	MS Word Document reading library
Summary(pl.UTF-8):	Biblioteka czytająca dokumenty MS Worda
Name:		wv2
Version:	0.4.2
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/wvware/%{name}-%{version}.tar.bz2
# Source0-md5:	850ed8e44a84e7bf0610747827018cbc
Patch0:		%{name}-link.patch
URL:		http://wvware.sourceforge.net/
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	libgsf-devel >= 1.7.2
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wv2 is a library that understands the Microsoft Word 8 binary file
format (Office97, Office2000).

%description -l pl.UTF-8
wv2 jest biblioteką, którą rozumie binarne dokumenty programu
Microsoft Word 8 (Office97, Office2000).

%package devel
Summary:	Include files needed to compile
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki wv2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgsf-devel
Obsoletes:	wv2-static

%description devel
Contains the wv2 header files.

%description devel -l pl.UTF-8
Pakiet tem zawiera pliki nagłówkowe wv2.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog THANKS TODO
%attr(755,root,root) %{_libdir}/libwv2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwv2.so.4

%files devel
%defattr(644,root,root,755)
%doc doc/escher/*.html doc/DESIGN.html src/generator/{*.htm,spec_defects}
%attr(755,root,root) %{_bindir}/wv2-config
%attr(755,root,root) %{_libdir}/libwv2.so
%{_libdir}/libwv2.la
%{_includedir}/wv2
%{_libdir}/wvWare
