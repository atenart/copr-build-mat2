%global NAUTILUS_MAYOR_VER  3.0
%global sname nautilus-python

Name:           python3-nautilus
Version:        1.2
Release:        1%{?dist}
Summary:        Python bindings for Nautilus

Group:          Development/Libraries
License:        GPLv2+
URL:            https://www.gnome.org/
Source0:        https://ftp.gnome.org/pub/GNOME/sources/%{sname}/%{version}/%{sname}-%{version}.tar.xz

BuildRequires:  python3-devel
BuildRequires:  nautilus-devel
BuildRequires:  pygobject3-devel
BuildRequires:  gtk-doc
BuildRequires:  autoconf automake libtool make

Requires:	python3
Requires:       nautilus >= 3.0

%description
Python bindings for Nautilus

%prep
%setup -q -n %{sname}-%{version}
find m4 -type f -not -name 'python.m4' -delete

autoreconf -if -I m4

%build
export PYTHON=/usr/bin/python3
%configure
%make_build

%install
%make_install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{sname}/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete
rm -rfv $RPM_BUILD_ROOT%{_docdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/%{sname}.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/nautilus/extensions-%{NAUTILUS_MAYOR_VER}/lib%{sname}.so
%dir %{_datadir}/%{sname}/extensions

%changelog
* Wed Jun 13 2018 Antoine Tenart <antoine.tenart@ack.tf> - 1.2-1
- Imported the python2-nautilus spec, reworked it to produce a
  python3-nautilus package, bump to 1.2, and removed the doc.
