Summary:	MS Word Document reading library
Summary(pl):	Biblioteka czytaj±ca dokumenty MS Worda
Name:		wv2
Version:	0.0.9
Release:	1
License:	LGPL
Group:		Libraries
Vendor:		Caolan McNamara <Caolan.McNamara@ul.ie>
Source0:	http://dl.sourceforge.net/wvware/%{name}-%{version}.tar.bz2
Patch0:		%{name}-link.patch
URL:		http://www.wvWare.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libgsf-devel >= 1.7.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wv2 is a library that understands the Microsoft Word 8 binary
file format (Office97, Office2000).

%description -l pl
wv2 jest bibliotek±, któr± rozumie binarne dokumenty programu
Microsoft Word 8 (Office97, Office2000).

%package devel
Summary:	Include files needed to compile
Summary(pl):	Pliki nag³ówkowe do biblioteki wv2
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libgsf-devel
Requires:	libstdc++-devel

%description devel
Contains the wv2 header files.

%description devel -l pl
Pakiet tem zawiera pliki nag³ówkowe wv2.

%package static
Summary:	Static wv2 library
Summary(pl):	Biblioteka statyczna wv2
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com o wv
Group:		Libraries
Requires:	%{name}-devel = %{version}

%description static
Contains static wv2 library.

%description static -l pl
Pakiet zawiera statyczn± bibliotekê wv2.

%prep
%setup -q

# Checking for CVS specific files and removing them.
find . -type d -name 'CVS'| xargs rm -rf

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-glib \
	--with-libole2 \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/escher/*.html doc/DESIGN.html src/generator/{*.htm,spec_defects}
%attr(755,root,root) %{_bindir}/wv2-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/wv2

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
