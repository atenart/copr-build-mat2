%global NAUTILUS_MAYOR_VER  3.0

Name:           nautilus-python
Version:        1.2
Release:        1%{?dist}
Summary:        Python bindings for Nautilus

Group:          Development/Libraries
License:        GPLv2+
URL:            http://www.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  python3-devel
BuildRequires:  nautilus-devel
BuildRequires:  pygobject3-devel
BuildRequires:  gtk-doc
BuildRequires:  autoconf automake libtool make

%global _description\
Python bindings for Nautilus\


%description %_description

%package -n python3-nautilus
Summary: %summary
Requires:       nautilus >= 3.0
%{?python_provide:%python_provide python3-nautilus}
# Remove before F30
Provides: nautilus-python = %{version}-%{release}
Provides: nautilus-python%{?_isa} = %{version}-%{release}
Obsoletes: nautilus-python < %{version}-%{release}

%description -n python3-nautilus %_description

%package -n python3-nautilus-devel
Summary:        Python bindings for Nautilus
Group:          Development/Libraries
Requires:       python3-nautilus = %{version}-%{release}
Requires:       pkgconfig

%description -n python3-nautilus-devel
Python bindings for Nautilus


%prep
%setup -q
find m4 -type f -not -name 'python.m4' -delete

autoreconf -if -I m4

%build
export PYTHON=/usr/bin/python3
%configure
%make_build


%install
%make_install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete
rm -rfv $RPM_BUILD_ROOT%{_docdir}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -n python3-nautilus
%license COPYING
%{_libdir}/nautilus/extensions-%{NAUTILUS_MAYOR_VER}/lib%{name}.so
%dir %{_datadir}/%{name}/extensions

%files -n python3-nautilus-devel
%license COPYING
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jun 13 2018 Antoine Tenart <antoine.tenart@ack.tf> - 1.2-1
- Imported the python2-nautilus spec, reworked it to produce a
  python3-nautilus package, bump to 1.2, and removed the doc.
